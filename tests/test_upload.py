import os
import pytest
from uploader import upload
from io import BytesIO

@pytest.fixture
def client():
    upload.app.config['TESTING'] = True
    client = upload.app.test_client()
    yield client

def test_home(client):
    response = client.get('/')
    assert response.status_code == 200

def test_upload_success(client):
    data = dict(file=(BytesIO(b'abcdef'), 'test.jpg'),)
    response = client.post(
        '/img', data=data, follow_redirects=True,
        content_type='multipart/form-data'
    )
    assert response.status_code == 200

def test_upload_bad_request(client):
    response = client.get('/img')
    assert response.status_code == 405

def test_upload_missing_image(client):
    response = client.post(
        '/img', data=None, follow_redirects=True,
        content_type='multipart/form-data'
    )
    assert response.status_code == 400
