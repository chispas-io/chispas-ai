import pytest

@pytest.mark.usefixtures('test_user')
def test_authenticate(app):
    with app.test_client() as client:
        resp = client.post('/api/account/authenticate', data={
            'username': 'charlie',
            'password': 'is_a_cat',
        })

        assert resp.status_code == 200
        # pylint:disable-next=line-too-long
        assert resp.json == { 'authentication_token': 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpYXQiOjE2OTU3ODk4MDUsInN1YiI6IlBUQmw2WkdzMUs5UkJBcXUzVTRNRGxZajZKa0FPd2Rla0wxYjdRSWd4Y2JTRjR6NzVZT3ZnRlFxc3ZwbWRFSnZZRnRXQjJTN2ljdTE2V0pSZE5mMFVBIiwiZXhwIjoxNjk4MzgxODA1fQ.qk9E7o_n0lNrsffHa3jgEfLUKVOB8Houxo5wG09LWxk' }

@pytest.mark.usefixtures('test_user')
def test_login(app):
    with app.test_client() as client:
        resp = client.post('/api/account/login', data={
            'username': 'charlie',
            'password': 'is_a_cat',
        })

        # test session in this method here?

        assert resp.status_code == 200
        # pylint:disable-next=line-too-long
        assert resp.json == { 'authentication_token': 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpYXQiOjE2OTU3ODk4MDUsInN1YiI6IlBUQmw2WkdzMUs5UkJBcXUzVTRNRGxZajZKa0FPd2Rla0wxYjdRSWd4Y2JTRjR6NzVZT3ZnRlFxc3ZwbWRFSnZZRnRXQjJTN2ljdTE2V0pSZE5mMFVBIiwiZXhwIjoxNjk4MzgxODA1fQ.qk9E7o_n0lNrsffHa3jgEfLUKVOB8Houxo5wG09LWxk' }
