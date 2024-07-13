from datetime import datetime


class MyGreeter:

    def __init__(self):
        pass

    def greeting(self, current_time=None):
        """
        Returns a greeting based on the current time.
        If current_time is not provided, it uses the current system time.

        :param current_time: Optional, datetime object representing the current time.
        :return: str, a greeting based on the time of day.
        """
        

        # If current_time is not provided, use the current system time
        if current_time is None:
            current_time = datetime.now()

        # Extract the hour from the current time
        hour = current_time.hour

        # Determine the greeting based on the hour
        if 6 <= hour < 12:
            print("Good morning")
            return "Good morning"
        elif 12 <= hour < 18:
            print("Good afternoon")
            return "Good afternoon"
        else:
            print("Good evening")
            return "Good evening"