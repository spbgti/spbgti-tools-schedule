import pytest

from core.models import Group

pytestmark = pytest.mark.django_db



@pytest.mark.smoke
def test_one_group(client, snapshot):
    Group.objects.create(
        number='446',
    )
    response = client.get('/api/groups').json()
    snapshot.assert_match(response)


def test_few_groups(client, snapshot):
    for group_number in ['443', '446', '1020']:
        Group.objects.create(
            number=group_number,
        )
    response = client.get('/api/groups').json()
    snapshot.assert_match(response)


def test_many_groups(client, snapshot):
    for group_number in range(200):
        Group.objects.create(
            number=str(group_number),
        )
    response = client.get('/api/groups').json()
    snapshot.assert_match(response)


def test_no_one_groups(client, snapshot):
    response = client.get('/api/groups').json()
    snapshot.assert_match(response)


def test_not_only_numeric_group(client, snapshot):
    Group.objects.create(
        number='446м',
    )
    response = client.get('/api/groups').json()
    snapshot.assert_match(response)


def test_basic_filtering(client, snapshot):
    Group.objects.create(
        number='444',
    )
    Group.objects.create(
        number='445',
    )
    response = client.get(
        '/api/groups',
        data={'number': '444'},
    ).json()
    snapshot.assert_match(response)


def test_case_sensitive_filtering(client, snapshot):
    Group.objects.create(
        number='444м',  # russian 'м'
    )
    Group.objects.create(
        number='444М',  # russian 'М'
    )
    Group.objects.create(
        number='444M',  # english 'М'
    )
    response = client.get(
        '/api/groups',
        data={'number': '444м'},  # russian 'м'
    ).json()
    snapshot.assert_match(response)


def test_empty_filtering(client, snapshot):
    Group.objects.create(
        number='444',
    )
    response = client.get(
        '/api/groups',
        data={'number': '445'},
    ).json()
    snapshot.assert_match(response)


def test_lookup_access(client, snapshot):
    Group.objects.create(
        number='444',
    )
    Group.objects.create(
        number='445',
    )
    response = client.get(
        '/api/groups/1',
    ).json()
    snapshot.assert_match(response)
