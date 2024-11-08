from mock.board import I2C


class VEML7700:

    def __init__(self, i2c_bus: I2C, address: int = 0x10):
        pass

    @property
    def lux(self) -> float:
        """Light value in lux."""
        return self.lux

    @lux.setter
    def lux(self, value):
        self.lux = value