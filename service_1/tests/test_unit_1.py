from flask_testing import TestCase
from flask import url_for
from requests_mock import mock
from service_1.app import app


class TestBase(TestCase):

    def create_app(self):
        return app

class TestResponse(TestBase):

    def test_index(self):

        with mock() as m:
            m.get('http://34.105.171.115:80/get/weapon', text='Sword')
            m.get('http://34.105.171.115:80/get/damage', json=15)
            m.post('http://34.105.171.115:80/post/status', json={
                "name": "Sharp",
                "level": "Adept",
                "effect": "Fire"
            })

            response = self.client.get(url_for('index'))


        self.assert200(response)
        self.assertIn("You generated a Sword with a damage multiplier of 15 and the status effect of Fire.\n \
        It is called the Adept Sharp Sword of Fire", response.data.decode())