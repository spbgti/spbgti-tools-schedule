import pytest

from api import models

pytestmark = pytest.mark.django_db


def test_group(client, snapshot):
    models.Group.objects.create(
        number='446',
    )
    response = client.get('/api/groups').json()
    snapshot.assert_match(response)