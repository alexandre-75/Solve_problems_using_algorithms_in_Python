import time


class Time():
    def __init__(self):
        pass

    def time(self):

        """Returns the current time as a timestamp.
        Uses the time() function from the time module to get the current time
        as a number of seconds since the UNIX epoch (00:00:00 UTC, January 1, 1970).
        The time is returned as a floating-point number representing the timestamp.
        Returns:
            float: The timestamp corresponding to the current time.
        """

        now = time.time()
        return now
