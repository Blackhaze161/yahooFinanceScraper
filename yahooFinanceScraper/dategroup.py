import time


def get_time_group():

    start_date = -2208985200  # 01/01/1900
    end_date = int(time.time())  # Epoch time when invoked
    date = {'start_date': start_date, 'end_date': end_date}
    return date
