import RPi.GPIO as GPIO
import time
import logging

# Logging konfigurieren
logging.basicConfig(filename='/home/plant-server-user/Desktop/pump_control.log', level=logging.INFO,
                    format='%(asctime)s - %(levelname)s - %(message)s')

# GPIO-Pins für die Relaismodule (je eine Pumpe pro Pin)
RELAY_PIN_PUMPE1 = 13  # GPIO 13
# RELAY_PIN_PUMPE2 = 27  # GPIO 27, physischer Pin 13
# RELAY_PIN_PUMPE3 = 22  # GPIO 22, physischer Pin 15

# GPIO-Setup
GPIO.setmode(GPIO.BCM)
GPIO.setup(RELAY_PIN_PUMPE1, GPIO.OUT)
# GPIO.setup(RELAY_PIN_PUMPE2, GPIO.OUT)
# GPIO.setup(RELAY_PIN_PUMPE3, GPIO.OUT)

# Pumpensteuerung mit Logging
def pumpe_an(pin, pumpe_name):
    GPIO.output(pin, GPIO.LOW)  # Relais schaltet bei LOW
    logging.info(f"{pumpe_name} eingeschaltet")

def pumpe_aus(pin, pumpe_name):
    GPIO.output(pin, GPIO.HIGH)  # Relais schaltet bei HIGH
    logging.info(f"{pumpe_name} ausgeschaltet")

try:
    logging.info("Warte 30 Sekunden bevor Pumpen angesteuert werden")
    time.sleep(30)  # Warte 30 Sekunden nach dem Start
    while True:
        # Steuerung für Pumpe 1
        pumpe_an(RELAY_PIN_PUMPE1, "Pumpe 1")
        time.sleep(10)  # Pumpe 1 für 10 Sekunden an
        pumpe_aus(RELAY_PIN_PUMPE1, "Pumpe 1")
        time.sleep(345600)  # Wartezeit für 4 Tage

        # # Steuerung für Pumpe 2
        # pumpe_an(RELAY_PIN_PUMPE2, "Pumpe 2")
        # time.sleep(15)  # Pumpe 2 für 15 Sekunden an
        # pumpe_aus(RELAY_PIN_PUMPE2, "Pumpe 2")
        # time.sleep(345600)  # Wartezeit für 4 Tage

        # # Steuerung für Pumpe 3
        # pumpe_an(RELAY_PIN_PUMPE3, "Pumpe 3")
        # time.sleep(20)  # Pumpe 3 für 20 Sekunden an
        # pumpe_aus(RELAY_PIN_PUMPE3, "Pumpe 3")
        # time.sleep(345600)  # Wartezeit für 4 Tage

except Exception as e:
    logging.error(f"Ein Fehler ist aufgetreten: {e}")

finally:
    GPIO.cleanup()
    logging.info("GPIO-Pins wurden bereinigt und das Programm wurde beendet")