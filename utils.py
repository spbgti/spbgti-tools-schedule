from datetime import datetime, timedelta, time
from settings import SEMESTER_ENDS, FIRST_SEMESTER_START
from models import Group


def _get_dates_by_weekday_between_two_dates(weekday, start_date, end_date):
    """Generate datetimes which represent weekdays in given period
    :param weekday: weekday index <0-6>
    :param start_date: datetime object <left bound of period>
    :param end_date: datetime object <right bound of period>"""
    current_weekday_date = start_date + timedelta(days=weekday-start_date.weekday())  # Find first date by weekday

    if current_weekday_date < start_date:
        current_weekday_date += timedelta(days=7)

    while start_date <= current_weekday_date <= end_date:
        yield current_weekday_date
        current_weekday_date += timedelta(days=7)

    if start_date <= current_weekday_date <= end_date:
        yield current_weekday_date


def get_end_semester_date():
    """Return datetime object which represents the end of current semester"""
    now = datetime.now()
    now_tuple = now.timetuple()[1:3]

    if FIRST_SEMESTER_START < now_tuple < SEMESTER_ENDS[0]:
        return datetime(year=now.year, month=SEMESTER_ENDS[0][1], day=SEMESTER_ENDS[0][0])
    else:
        return datetime(year=now.year, month=SEMESTER_ENDS[1][1], day=SEMESTER_ENDS[1][0])


def generate_pair_dicts(group, pair_name, duration, start_date, end_date, days):
    """Generate dictionaries which represent Pair object (for insert_many method)
    :param group: Group object
    :param pair_name: pair name
    :param duration: duration of pair
    :param start_date: datetime object <left bound of period>
    :param end_date: datetime object <right bound of period> or None
    :param days: container with containers which contain week index and container with time
    Example:
        days = [
            (weekday, (hour, minutes)
        ]
        where weekday is index of week <0-6>
    """
    for day in days:
        weekday = day[0]
        hour = day[1][0]
        minute = day[1][1]
        # TODO: Add pair cheks, if allowed to create new pair
        dates = _get_dates_by_weekday_between_two_dates(weekday, start_date, end_date)

        for date in dates:
            yield {'group': group,
                   'name': pair_name,
                   'date': date.replace(hour=hour, minute=minute),
                   'duration': duration,
                   }