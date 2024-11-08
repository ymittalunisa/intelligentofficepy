import time

DEPLOYMENT = False # This variable is to understand whether you are deploying on the actual hardware

try:
    import RPi.GPIO as GPIO
    DEPLOYMENT = True
except:
    import mock.GPIO as GPIO


class IntelligentOffice:

    def __init__(self):
        pass


    def check_quadrant_occupancy(self, pin: int) -> bool:
        pass

    def manage_blinds_based_on_time(self) -> None:
        pass

    def manage_light_level(self) -> None:
        pass

    def monitor_air_quality(self) -> None:
        pass

    def change_servo_angle(self, duty_cycle):
        """
        Changes the servo motor's angle by passing it the corresponding PWM duty cycle
        :param duty_cycle: the PWM duty cycle (it's a percentage value)
        """
        self.servo.ChangeDutyCycle(duty_cycle)
        if DEPLOYMENT:  # Sleep only if you are deploying on the actual hardware
            time.sleep(1)
        self.servo.ChangeDutyCycle(0)


class IntelligentOfficeError(Exception):
    pass
