
import RPi.GPIO as GPIO
import time
  
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)


  
class CarInfrared(object):
    def __init__(self):
        self.GPIO_Infrared_right = 8
        self.GPIO_Infrared_left = 7

        GPIO.setup(self.GPIO_Infrared_right, GPIO.IN)
        GPIO.setup(self.GPIO_Infrared_left, GPIO.IN)
  
    def InfraredMeasure(self):
        left_measure = GPIO.input(self.GPIO_Infrared_left)
        right_measure = GPIO.input(self.GPIO_Infrared_right)
    
        return [left_measure, right_measure]
  

if __name__ == '__main__':
    try:
        car = CarInfrared()
        while True:
            [left, right] = car.InfraredMeasure()
            print(left, right)
            time.sleep(1)
  
        # Reset by pressing CTRL + C
    except KeyboardInterrupt:
        print("Measurement stopped by User")
        GPIO.cleanup()