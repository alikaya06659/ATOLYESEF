import unittest
from app import create_app, db
from app.models import User
from flask import url_for

class AuthTestCase(unittest.TestCase):
    def setUp(self):
        self.app = create_app('config.TestConfig')
        self.app_context = self.app.app_context()
        self.app_context.push()
        db.create_all()
        self.client = self.app.test_client()

    def tearDown(self):
        db.session.remove()
        db.drop_all()
        self.app_context.pop()

    def test_register_and_login(self):
        # Register a new user
        response = self.client.post(url_for('auth.register'), data={
            'username': 'testuser',
            'email': 'test@example.com',
            'password': 'Password123',
            'password_confirm': 'Password123',
            'submit': True
        }, follow_redirects=True)
        self.assertIn(b'Kayıt başarılı', response.data)
        # Login with the new user
        response = self.client.post(url_for('auth.login'), data={
            'email': 'test@example.com',
            'password': 'Password123',
            'remember_me': False,
            'submit': True
        }, follow_redirects=True)
        self.assertIn(b'Giriş başarılı', response.data)

if __name__ == '__main__':
    unittest.main()
