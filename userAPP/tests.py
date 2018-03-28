from django.test import TestCase

# Create your tests here.
from .models import User
import os


class UserModelTests(TestCase):

    def test_user_image_upload(self):
        user1 = User.objects.create_user(username="aaa",
                                        password="woshishadan",
                                        first_name="kekeda",)
        img = user1.image.url
        self.assertIs(os.path.exists(img), True)