from models import Group, Pair
from peewee import DoesNotExist


def add_group(group_number):
    group, status = Group.get_or_create(number=group_number)
    if status:
        return 'Group added successfully', True
    else:
        return 'A Group already exists', False


def add_pair(group_number, pair_name, pair_date, pair_duration):
    try:
        group = Group.get(Group.number == group_number)
    except DoesNotExist:
        return 'Group does not exist', False

    pair, status = Pair.get_or_create(group=group, name=pair_name, date=pair_date, duration=pair_duration)

    if status:
        return 'Pair added successfully', True
    else:
        return 'A Pair already exists', False


def get_pairs(group_number, date):
    query = Pair.select().join(Group).where(Group.number == group_number, Pair.date == date)

    if query:
        return query, True
    else:
        return None, False
