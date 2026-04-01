
import pytest


pytestmark = pytest.mark.api


class TestPostsApi:
    def test_get_all_posts(self, api_client, progress_step):
        progress_step("Send a request to retrieve all posts.")
        response = api_client.get("/posts")

        progress_step("Validate the response status and payload structure.")
        assert response.status_code == 200
        posts = response.json()
        assert isinstance(posts, list)
        assert len(posts) > 0
        assert "userId" in posts[0]
        assert "id" in posts[0]
        assert "title" in posts[0]
        assert "body" in posts[0]

    def test_get_single_post(self, api_client, progress_step):
        post_id = 1

        progress_step(f"Send a request to retrieve post {post_id}.")
        response = api_client.get(f"/posts/{post_id}")

        progress_step("Validate the response status and returned post content.")
        assert response.status_code == 200
        post = response.json()
        assert post["id"] == post_id
        assert "title" in post

    def test_create_post(self, api_client, progress_step):
        new_post = {
            "title": "foo",
            "body": "bar",
            "userId": 1
        }

        progress_step("Send a request to create a new post.")
        response = api_client.post("/posts", json=new_post)

        progress_step("Validate the created post response payload.")
        assert response.status_code == 201
        created_post = response.json()
        assert created_post["title"] == new_post["title"]
        assert created_post["body"] == new_post["body"]
        assert created_post["userId"] == new_post["userId"]
        assert "id" in created_post

    def test_delete_post(self, api_client, progress_step):
        post_id = 1

        progress_step(f"Send a request to delete post {post_id}.")
        response = api_client.delete(f"/posts/{post_id}")

        progress_step("Validate the delete response status and empty response body.")
        assert response.status_code == 200
        assert response.json() == {}
