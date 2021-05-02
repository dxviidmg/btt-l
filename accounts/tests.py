from django.test import TestCase
from django.contrib.auth.models import User

data_user = {'username':'ejemplo', 'first_name': 'ejemplo'}
password_user = 'testuser'


class UserModelTest(TestCase):
    def test_create_user(self):
        user, user_created = User.objects.get_or_create(**data_user)
        user.set_password(password_user)

        self.assertEquals(user.username, 'ejemplo')

