from datetime import datetime, timedelta


def generate_time_array(start_time: str, end_time: str, delta_minutes: int):
    """
    Generates an array of datetime.time objects from start_time to end_time with a step of delta_minutes.

    :param start_time: Start time in HH:MM format
    :param end_time: End time in HH:MM format
    :param delta_minutes: Interval in minutes
    :return: List of datetime.time objects
    """
    start_dt = datetime.strptime(start_time, "%H:%M")
    end_dt = datetime.strptime(end_time, "%H:%M")
    delta = timedelta(minutes=delta_minutes)

    times = []
    current_dt = start_dt
    while current_dt <= end_dt:
        times.append(current_dt.time())
        current_dt += delta

    return times
