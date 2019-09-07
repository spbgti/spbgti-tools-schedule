# -*- coding: utf-8 -*-
# snapshottest: v1 - https://goo.gl/zC4yUc
from __future__ import unicode_literals

from snapshottest import Snapshot


snapshots = Snapshot()

snapshots['test_one_room 1'] = [
    {
        'location_id': 1,
        'name': '9 каб.',
        'room_id': 1
    }
]

snapshots['test_name_filtering 1'] = [
    {
        'location_id': 1,
        'name': '9 каб.',
        'room_id': 1
    }
]

snapshots['test_name_case_sensitive_filtering 1'] = [
]

snapshots['test_empty_filtering 1'] = [
]

snapshots['test_lookup_access 1'] = {
    'location_id': 1,
    'name': '9 каб.',
    'room_id': 1
}

snapshots['test_filter_by_location 1'] = [
    {
        'location_id': 1,
        'name': '9 каб.',
        'room_id': 1
    }
]
