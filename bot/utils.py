from datetime import datetime


def check_date_format(input_date):
    try:
        date_format = "%d.%m.%Y"
        datetime.strptime(input_date, date_format)
        return True
    except ValueError:
        return False
