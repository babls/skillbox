from app_blog.models import BlogPost
from django.contrib.auth.models import User
from django.test import TestCase
from django.urls import reverse
from django.utils.timezone import now
from .models import Profile

NUMBER_POST_BLOG = 10
USER_EMAIL = 'test@email.ru'
OLD_PASSWORD = 'test'


class UsersTest(TestCase):  # Тест постов, добавляет 10 штук
    @classmethod
    def setUpTestData(cls):
        test_user = User.objects.create_user(username='test', email=USER_EMAIL, password=OLD_PASSWORD)
        for post_index in range(NUMBER_POST_BLOG):
            BlogPost.objects.create(
                name='test_post',
                text='test_post_text',
                dataCreate=now(),
                activity='True',
                author=test_user
            )

    def test_post_blog(self):
        url = reverse('main')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'app_users/index.html')
        self.assertTrue(len(response.context['blog']) == NUMBER_POST_BLOG)  # сравнивает количество постов

    def test_profile(self):
        url = reverse('profile')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'app_users/profile.html')
        self.assertContains(response, 'Вы не авторизованы на нашем сайте')


class RestorePasswordTest(TestCase):

    def test_restore_password_url_and_template(self):
        url = reverse('restore_password')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'app_users/restore_password.html')

    def test_post_restore_password(self):
        response = self.client.post(reverse('restore_password'), {'email': USER_EMAIL})
        self.assertEqual(response.status_code, 302)
        from django.core.mail import outbox
        self.assertEqual(len(outbox), 1)
        self.assertIn(USER_EMAIL, outbox[0].to)

    def test_if_password_was_changed(self):
        user = User.objects.create(username='test', email=USER_EMAIL)
        user.set_password(OLD_PASSWORD)
        user.save()
        old_password_hash = user.password
        response = self.client.post(reverse('restore_password'), {'email': USER_EMAIL})
        self.assertEqual(response.status_code, 302)
        user.refresh_from_db()
        self.assertNotEqual(old_password_hash, user.password)


class EditProfileTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        test_user = User.objects.create_user(username='test', email='test@email.ru', password='test')
        test_profile = Profile.objects.create(user=test_user, city='Test', date_of_birth='2000-01-01',
                                              telephone_number='89991117733', about_myself='TEST_TEXT')

    def test_edit_profile_url_and_template(self):
        test_user = User.objects.get(username='test', email='test@email.ru')
        test_profile = Profile.objects.get(user=test_user)
        response = self.client.post(reverse('login'), {'username': 'test', 'password': 'test'})
        url_str = '/edit_profile/' + str(test_user.id) + '/'
        # url = reverse(url_str)
        response_profile = self.client.get(url_str)
        self.assertEqual(response_profile.status_code, 200)

    def test_edit_profile(self):
        test_user = User.objects.get(username='test', email='test@email.ru')
        old_name = test_user.username
        test_profile = Profile.objects.get(user=test_user)
        url_str = '/edit_profile/' + str(test_user.id) + '/'
        response = self.client.post(url_str, {
            'username': 'test_new',
            'surname': 'testov',
            'email': 'test_new@mail.ru',
            'city': 'Test_sity',
            'date_of_birth': '01.01.2001',
            'telephone_number': '89991117733',
            'about_myself': 'TEST_TEXT'
        })
        user = User.objects.get(username='test_new', email='test_new@mail.ru')
        new_name = user.username
        self.assertNotEqual(old_name, new_name)
