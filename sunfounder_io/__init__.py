from .adc import ADC
from .i2c import I2C
from .pin import Pin
from .pwm import PWM
from .servo import Servo
from .spi import SPI

I2C().reset_mcu()

def __main__():
    print("Thanks for using Sunfounder IO !")
    I2C().reset_mcu()