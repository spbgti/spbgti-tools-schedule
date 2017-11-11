from datetime import datetime, timedelta
from typing import Tuple, List

from main.exceptions import GroupAlreadyExistsError, GroupDoesNotExistError, PairAlreadyExistsError
from main.models import Group, Pair, db
from main.utils import get_end_semester_date, generate_pair_dicts, Days
from peewee import DoesNotExist, Query


def _add_group(group_number: int) -> Tuple[str, bool]:
    """Create new Group
    :param group_number: number of group"""

    group, status = Group.get_or_create(number=group_number)
    if status:
        return group
    else:
        raise GroupAlreadyExistsError


def _add_pair(group_number: int, pair_name: str, pair_date: datetime, pair_duration: int) -> Tuple[str, bool]:
    """Create new Pair
    :param group_number: number of group
    :param pair_name: pair name
    :param pair_date: datetime object
    :param pair_duration: duration of pair"""

    try:
        group = Group.get(Group.number == group_number)
    except DoesNotExist:
        raise GroupDoesNotExistError

    pair, status = Pair.get_or_create(group=group, name=pair_name, date=pair_date, duration=pair_duration)

    if status:
        return pair
    else:
        raise PairAlreadyExistsError


def get_pairs_query_by_date(group_number: int, date: datetime) -> Query:
    """Return all Pairs by date"""
    query = Pair.select().join(Group).where(Group.number == group_number,
                                            Pair.date.year == date.year,
                                            Pair.date.month == date.month,
                                            Pair.date.day == date.day)
    return query


def get_pairs_query_for_a_week(group_number: int, date: datetime) -> List[Query]:
    """Return all Pairs by date for a whole week in which this date is"""
    date = date - timedelta(date.weekday())  # Find start of the current week
    query = []
    for weekday in range(7):
        query.extend(get_pairs_query_by_date(group_number, date + timedelta(weekday)))
    return query


def fill_pairs(group_number: int, pair_name: str, pair_duration: int, pair_start_date: datetime, days: Days, period: int,
               pair_end_date=get_end_semester_date()) -> bool:
    try:
        group = Group.get(Group.number == group_number)
    except DoesNotExist:
        raise GroupDoesNotExistError

    # TODO: From this moment we don't have any validation for creating new Pairs
    pair_dicts = generate_pair_dicts(group, pair_name, pair_duration, pair_start_date, pair_end_date, days, period)
    with db.atomic():
        Pair.insert_many(pair_dicts)
    # TODO: Create handling insertion status
    return True
