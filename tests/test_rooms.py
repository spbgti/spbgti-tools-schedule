import pytest
from pytest import fixture

from core.models import Location, Room

pytestmark = pytest.mark.django_db


@fixture
def locations(db):
    sa = Location.objects.create(
        name='каф. СА',
    )
    main_campus = Location.objects.create(
        name='Главный корпус'
    )
    yield sa, main_campus


@pytest.mark.smoke
def test_one_room(client, snapshot, locations):
    sa, _ = locations
    Room.objects.create(
        location=sa,
        name='9 каб.',
    )
    response = client.get('/api/rooms').json()
    snapshot.assert_match(response)


def test_name_filtering(client, snapshot, locations):
    sa, _ = locations
    Room.objects.create(
        location=sa,
        name='9 каб.',
    )
    Room.objects.create(
        location=sa,
        name='10 каб.',
    )
    response = client.get(
        '/api/rooms',
        data={'name': '9 каб.'},
    ).json()
    snapshot.assert_match(response)


def test_name_case_sensitive_filtering(client, snapshot, locations):
    sa, _ = locations
    Room.objects.create(
        location=sa,
        name='9 каб.',
    )
    Room.objects.create(
        location=sa,
        name='10 каб.',
    )
    response = client.get(
        '/api/rooms',
        data={'name': '9 КАБ.'},
    ).json()
    snapshot.assert_match(response)


def test_empty_filtering(client, snapshot, locations):
    sa, _= locations
    Room.objects.create(
        location=sa,
        name='9 каб.',
    )
    response = client.get(
        '/api/rooms',
        data={'name': 'where is the fucking cab???'},
    ).json()
    snapshot.assert_match(response)


def test_filter_by_location(client, snapshot, locations):
    sa, main_campus = locations
    Room.objects.create(
        location=sa,
        name='9 каб.',
    )
    Room.objects.create(
        location=main_campus,
        name='221 каб.',
    )
    response = client.get(
        '/api/rooms',
        data={'location': 1},
    ).json()
    snapshot.assert_match(response)


def test_lookup_access(client, snapshot, locations):
    sa, _ = locations
    Room.objects.create(
        location=sa,
        name='9 каб.',
    )
    Room.objects.create(
        location=sa,
        name='10 каб.',
    )
    response = client.get(
        '/api/rooms/1',
    ).json()
    snapshot.assert_match(response)
