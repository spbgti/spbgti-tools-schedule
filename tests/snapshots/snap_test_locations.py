# -*- coding: utf-8 -*-
# snapshottest: v1 - https://goo.gl/zC4yUc
from __future__ import unicode_literals

from snapshottest import Snapshot


snapshots = Snapshot()

snapshots['test_one_location 1'] = [
    {
        'geo_position': None,
        'location_id': 1,
        'name': 'каф. СА'
    }
]

snapshots['test_few_locations 1'] = [
    {
        'geo_position': None,
        'location_id': 1,
        'name': 'каф. СА'
    },
    {
        'geo_position': None,
        'location_id': 2,
        'name': 'Главный корпус'
    },
    {
        'geo_position': None,
        'location_id': 3,
        'name': '1'
    },
    {
        'geo_position': None,
        'location_id': 4,
        'name': 'Latin location'
    }
]

snapshots['test_no_one_locations 1'] = [
]

snapshots['test_basic_filtering 1'] = [
    {
        'geo_position': None,
        'location_id': 1,
        'name': 'каф. СА'
    }
]

snapshots['test_case_sensitive_filtering 1'] = [
    {
        'geo_position': None,
        'location_id': 1,
        'name': 'каф. СА'
    }
]

snapshots['test_empty_filtering 1'] = [
]

snapshots['test_lookup_access 1'] = {
    'geo_position': None,
    'location_id': 1,
    'name': 'каф. СА'
}
