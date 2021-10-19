import spidev
class SPI(object):
    def __init__(self, bus, device,max_speed_hz=500000,no_cs=True):
        spi = spidev.SPiDev()
        spi.open(bus, device)


def test():
    from time import sleep

    while True:
        spi = SPI(0,0)
        val = spi.xfer([0xff,0xff])
        print(val)
        sleep(0.005)
    

if __name__ == "__main__":
    test()