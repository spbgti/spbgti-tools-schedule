from models import Group, Pair, db
from peewee import DoesNotExist
from utils import get_end_semester_date, generate_pair_dicts


def _add_group(group_number):
    """Create new Group
    :param group_number: number of group"""

    group, status = Group.get_or_create(number=group_number)
    if status:
        return 'Group added successfully', True
    else:
        return 'A Group already exists', False


def _add_pair(group_number, pair_name, pair_date, pair_duration):
    """Create new Pair
    :param group_number: number of group
    :param pair_name: pair name
    :param pair_date: datetime object
    :param pair_duration: duration of pair"""

    try:
        group = Group.get(Group.number == group_number)
    except DoesNotExist:
        return 'Group does not exist', False

    pair, status = Pair.get_or_create(group=group, name=pair_name, date=pair_date, duration=pair_duration)

    if status:
        return 'Pair added successfully', True
    else:
        return 'A Pair already exists', False


def _get_pairs_by_date(group_number, date):
    """Return all Pairs by date"""
    query = Pair.select().join(Group).where(Group.number == group_number, Pair.date == date)

    if query:
        return query, True
    else:
        return None, False


def fill_pairs(group_number, pair_name, pair_duration, pair_start_date, days, pair_end_date=get_end_semester_date()):
    try:
        group = Group.get(Group.number == group_number)
    except DoesNotExist:
        return 'Group does not exist', False

    # TODO: From this moment we don't have any validation for creating new Pairs
    pair_dicts = generate_pair_dicts(group_number, pair_name, pair_duration, pair_start_date, pair_end_date, days)

    with db.atomic():
        Pair.insert_many(pair_dicts)
