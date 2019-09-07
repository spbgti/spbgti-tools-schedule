# -*- coding: utf-8 -*-
# snapshottest: v1 - https://goo.gl/zC4yUc
from __future__ import unicode_literals

from snapshottest import Snapshot


snapshots = Snapshot()

snapshots['test_one_teacher 1'] = [
    {
        'name': 'Гайков А.В.',
        'position': None,
        'rank': None,
        'teacher_id': 1
    }
]

snapshots['test_few_teachers 1'] = [
    {
        'name': 'Гайков А.В.',
        'position': None,
        'rank': None,
        'teacher_id': 1
    },
    {
        'name': 'Халимон В.И.',
        'position': None,
        'rank': None,
        'teacher_id': 2
    },
    {
        'name': 'Проститенко О.В.',
        'position': None,
        'rank': None,
        'teacher_id': 3
    },
    {
        'name': 'Чумаков С.И.',
        'position': None,
        'rank': None,
        'teacher_id': 4
    }
]

snapshots['test_no_one_locations 1'] = [
]

snapshots['test_basic_filtering 1'] = [
    {
        'name': 'Халимон В.И.',
        'position': None,
        'rank': None,
        'teacher_id': 2
    }
]

snapshots['test_empty_filtering 1'] = [
]

snapshots['test_lookup_access 1'] = {
    'name': 'Гайков А.В.',
    'position': None,
    'rank': None,
    'teacher_id': 1
}
