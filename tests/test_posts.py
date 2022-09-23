import pytest
from rest_framework import status


@pytest.mark.django_db
class TestCreatePost:
    def test_successful_post_create(self,client):
        """
        Test for successful post creation


        """
        data = {
            "content": "This is a new post for testing..."
        }

        response = client.post("hacker-news/api/", data=data)
        response_data = response.json()
        assert response.status_code == 201

