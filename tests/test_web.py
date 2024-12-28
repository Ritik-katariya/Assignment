from src.web.app import app

def test_web_client():
    with app.test_client() as client:
        response = client.get('/')
        assert response.status_code == 200

        response = client.get('/run-script')
        assert response.status_code == 200
