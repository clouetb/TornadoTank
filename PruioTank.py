import pruio
import threading
import logging

log = logging.getLogger(__name__)
log.setLevel(logging.DEBUG)
ch = logging.StreamHandler()
ch.setLevel(logging.DEBUG)
log.addHandler(ch)

class Tank:
    def __init__(self, ldirection, lpwm, rdirection, rpwm):
        self.__io = pruio.pruio_new(pruio.PRUIO_DEF_ACTIVE, 0x98, 0, 1)
        self.__lock = threading.Lock()
        self.__ldirection = getattr(pruio, ldirection)
        self.__lpwm = getattr(pruio, lpwm)
        self.__rdirection = getattr(pruio, rdirection)
        self.__rpwm = getattr(pruio, rpwm)
        pruio.pruio_gpio_config(self.__io, self.__ldirection, pruio.PRUIO_GPIO_OUT0)
        pruio.pruio_gpio_config(self.__io, self.__rdirection, pruio.PRUIO_GPIO_OUT0)
        pruio.pruio_gpio_config(self.__io, self.__lpwm, pruio.PRUIO_GPIO_OUT0)
        pruio.pruio_gpio_config(self.__io, self.__rpwm, pruio.PRUIO_GPIO_OUT0)
        pruio.pruio_pwm_setValue(self.__io, self.__lpwm, 31250, 0.0)
        pruio.pruio_pwm_setValue(self.__io, self.__rpwm, 31250, 0.0)
        pruio.pruio_config(self.__io, 1, 0x1FE, 0, 4)
        self.__speed = float(0)
        self.__direction_dict = {
            "n": self.north,
            "s": self.south,
            "w": self.west,
            "e": self.east,
            "nw": self.northwest,
            "ne": self.northeast,
            "sw": self.southwest,
            "se": self.southeast,
            "stop": self.stop
        }
        self.__direction = self.__direction_dict["n"]

    def __del__(self):
        log.info("Destroying pruio instance %s", self.__io)
        print("+++ Destroy")
        pruio.pruio_destroy(self.__io)

    def run(self, lspeed, rspeed):
        with self.__lock:
            if lspeed > 0:
                pruio.pruio_gpio_setValue(self.__io, self.__ldirection, pruio.PRUIO_GPIO_OUT1)
                pruio.pruio_pwm_setValue(self.__io, self.__lpwm, 31250, lspeed)
            elif lspeed < 0:
                pruio.pruio_gpio_setValue(self.__io, self.__ldirection, pruio.PRUIO_GPIO_OUT0)
                pruio.pruio_pwm_setValue(self.__io, self.__lpwm, 31250, lspeed)
            else:
                pruio.pruio_pwm_setValue(self.__io, self.__lpwm, 31250, 0)

            if rspeed > 0:
                pruio.pruio_gpio_setValue(self.__io, self.__rdirection, pruio.PRUIO_GPIO_OUT1)
                pruio.pruio_pwm_setValue(self.__io, self.__rpwm, 31250, rspeed)
            elif rspeed < 0:
                pruio.pruio_gpio_setValue(self.__io, self.__rdirection, pruio.PRUIO_GPIO_OUT0)
                pruio.pruio_pwm_setValue(self.__io, self.__rpwm, 31250, rspeed)
            else:
                pruio.pruio_pwm_setValue(self.__io, self.__rpwm, 31250, 0)

    def set_speed(self, speed):
        self.__speed = float(speed)
        self.__direction()

    def set_direction(self, direction):
        self.__direction = self.__direction_dict[direction]
        self.__direction()

    def north(self):
        self.run(self.__speed, self.__speed)

    def south(self):
        self.run(-self.__speed, -self.__speed)

    def west(self):
        self.run(self.__speed, -self.__speed)

    def east(self):
        self.run(-self.__speed, self.__speed)

    def northwest(self):
        self.run(self.__speed/float(2), self.__speed)

    def northeast(self):
        self.run(self.__speed, self.__speed/float(2))

    def southwest(self):
        self.run(-self.__speed/float(2), -self.__speed)

    def southeast(self):
        self.run(-self.__speed, -self.__speed/float(2))

    def stop(self):
        self.run(0, 0)
