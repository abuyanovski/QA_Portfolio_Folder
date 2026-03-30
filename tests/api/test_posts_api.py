
import pytest


pytestmark = pytest.mark.api


class TestPostsApi:
    def test_get_all_posts(self, api_client):
        response = api_client.get("/posts")
        assert response.status_code == 200
        posts = response.json()
        assert isinstance(posts, list)
        assert len(posts) > 0
        assert "userId" in posts[0]
        assert "id" in posts[0]
        assert "title" in posts[0]
        assert "body" in posts[0]

    def test_get_single_post(self, api_client):
        post_id = 1
        response = api_client.get(f"/posts/{post_id}")
        assert response.status_code == 200
        post = response.json()
        assert post["id"] == post_id
        assert "title" in post

    def test_create_post(self, api_client):
        new_post = {
            "title": "foo",
            "body": "bar",
            "userId": 1
        }
        response = api_client.post("/posts", json=new_post)
        assert response.status_code == 201
        created_post = response.json()
        assert created_post["title"] == new_post["title"]
        assert created_post["body"] == new_post["body"]
        assert created_post["userId"] == new_post["userId"]
        assert "id" in created_post

    def test_delete_post(self, api_client):
        post_id = 1
        response = api_client.delete(f"/posts/{post_id}")
        assert response.status_code == 200
        assert response.json() == {}
