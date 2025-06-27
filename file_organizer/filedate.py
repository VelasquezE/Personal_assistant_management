import datetime
import time
import os

def is_file_old(file_path, maximum_days = 120):
    """
    Checks if the modification time is greater than 
    the maximum days.
    """
    last_modification = os.path.getmtime(file_path)
    actual_time = time.time()
    days_since_modification = (actual_time - last_modification) / 86400

    if (days_since_modification > maximum_days):
        return True
    else:
        return False
    
def give_modification_date(file_path):
    """
    Gives the modification date of a file (Year- month-day)
    Returns:
        modification_date_string (String)
    """
    modification_date = datetime.date.fromtimestamp(os.path.getmtime(file_path))
    modification_date_string = modification_date.strftime("%Y-%m-%d")

    return modification_date_string