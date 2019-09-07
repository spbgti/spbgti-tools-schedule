import pytest

from core.models import Location

pytestmark = pytest.mark.django_db


@pytest.mark.smoke
def test_one_location(client, snapshot):
    Location.objects.create(
        name='каф. СА',
    )
    response = client.get('/api/locations').json()
    snapshot.assert_match(response)


def test_few_locations(client, snapshot):
    for location_name in ['каф. СА', 'Главный корпус', '1', 'Latin location']:
        Location.objects.create(
            name=location_name,
        )
    response = client.get('/api/locations').json()
    snapshot.assert_match(response)


def test_no_one_locations(client, snapshot):
    response = client.get('/api/locations').json()
    snapshot.assert_match(response)


def test_basic_filtering(client, snapshot):
    Location.objects.create(
        name='каф. СА',
    )
    Location.objects.create(
        name='Главный корпус',
    )
    response = client.get(
        '/api/locations',
        data={'name': 'каф. СА'},
    ).json()
    snapshot.assert_match(response)


def test_case_sensitive_filtering(client, snapshot):
    Location.objects.create(
        name='каф. СА',
    )
    Location.objects.create(
        name='каф. Са',
    )
    response = client.get(
        '/api/locations',
        data={'name': 'каф. СА'},
    ).json()
    snapshot.assert_match(response)


def test_empty_filtering(client, snapshot):
    Location.objects.create(
        name='каф. СА',
    )
    response = client.get(
        '/api/locations',
        data={'name': 'совсем другая кафедра'},
    ).json()
    snapshot.assert_match(response)


def test_lookup_access(client, snapshot):
    Location.objects.create(
        name='каф. СА',
    )
    Location.objects.create(
        name='Главный корпус',
    )
    response = client.get(
        '/api/locations/1',
    ).json()
    snapshot.assert_match(response)
