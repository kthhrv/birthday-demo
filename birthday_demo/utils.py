import datetime


def get_days_to_next_birthday(dob_str: str) -> int:
    '''
    Return the days until a users next birthday

        dob_str (str): YYYY-MM-DD formatted date

        Returns:
            days (int): days until next birthday
    '''
    today = datetime.date.today()
    dob = datetime.datetime.strptime(dob_str, "%Y-%m-%d")
    birthday = datetime.date(today.year, dob.month, dob.day)
    if birthday < today:
        birthday = birthday.replace(year=today.year + 1)

    return (birthday - today).days
