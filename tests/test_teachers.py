import pytest

from core.models import Teacher

pytestmark = pytest.mark.django_db


@pytest.mark.smoke
def test_one_teacher(client, snapshot):
    Teacher.objects.create(
        name='Гайков А.В.',
    )
    response = client.get('/api/teachers').json()
    snapshot.assert_match(response)


def test_few_teachers(client, snapshot):
    for teacher_name in ['Гайков А.В.', 'Халимон В.И.', 'Проститенко О.В.', 'Чумаков С.И.']:
        Teacher.objects.create(
            name=teacher_name,
        )
    response = client.get('/api/teachers').json()
    snapshot.assert_match(response)


def test_no_one_locations(client, snapshot):
    response = client.get('/api/teachers').json()
    snapshot.assert_match(response)


def test_basic_filtering(client, snapshot):
    Teacher.objects.create(
        name='Гайков А.В.',
    )
    Teacher.objects.create(
        name='Халимон В.И.',
    )
    response = client.get(
        '/api/teachers',
        data={'name': 'Халимон В.И.'},
    ).json()
    snapshot.assert_match(response)


def test_empty_filtering(client, snapshot):
    Teacher.objects.create(
        name='Гайков А.В.',
    )
    response = client.get(
        '/api/teachers',
        data={'name': 'Who is it?'},
    ).json()
    snapshot.assert_match(response)


def test_lookup_access(client, snapshot):
    Teacher.objects.create(
        name='Гайков А.В.',
    )
    Teacher.objects.create(
        name='Халимон В.И.',
    )
    response = client.get(
        '/api/teachers/1',
    ).json()
    snapshot.assert_match(response)
