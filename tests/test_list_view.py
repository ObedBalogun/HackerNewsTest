import pytest
from rest_framework import status


@pytest.mark.django_db
class TestGetPost:
    def test_successful_get_list_of_posts(self, client):
        """
        Test for successful list of posts retrieval
        """

        response = client.get('hacker-news/api/', client)
        assert response.status_code == 200
        assert isinstance(response.json(), list)

    def test_unsuccessful_get_list_of_posts(self, client):
        """
        Test for unsuccessful list of posts retrieval

        """

        response = client.get('hacker-news/api/', client)
        assert response.status_code == 401
        assert response.json()['detail'] == "Unable to get posts."

