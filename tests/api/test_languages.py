from chispas import create_app

def test_languages_list():
    app = create_app()

    with app.test_client() as client:
        resp = client.get('/api/languages/list')

        assert resp.status_code == 200
        assert resp.json == { 'data': { 'languages': ['en', 'es', 'ru', 'th'] } }
