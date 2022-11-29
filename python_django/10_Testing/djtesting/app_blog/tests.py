from app_blog.models import BlogPost
from django.contrib.auth.models import User
from django.test import TestCase
from django.urls import reverse
from django.utils.timezone import now

NUMBER_POST_BLOG = 10


class BlogTest(TestCase):  # Тест постов, добавляет 10 штук
    @classmethod
    def setUpTestData(cls):
        test_user = User.objects.create_user(username='test', email='test@email.ru', password='test')
        for post_index in range(NUMBER_POST_BLOG):
            BlogPost.objects.create(
                name='test_post',
                text='test_post_text',
                dataCreate=now(),
                activity='True',
                author=test_user
            )

    def test_view_new_post_blog(self):
        url = reverse('new_post_blog')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'app_blog/new_post_blog.html')

    def test_view_infopost(self):
        response = self.client.get('/blog/infopost/10/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'app_blog/infopost.html')
        self.assertContains(response, 'test_post')

    def test_login_and_list_post(self):
        test_user = User.objects.get(username='test')
        response = self.client.post(reverse('login'), {'username': 'test', 'password': 'test'})
        url = reverse('list_post')
        response_list_post = self.client.get(url)
        self.assertEqual(response_list_post.status_code, 200)                               # Проверяем авторизацию
        self.assertTemplateUsed(response_list_post, 'app_blog/list_post.html')
        self.assertTrue(len(response_list_post.context['post_list']) == NUMBER_POST_BLOG)   # Сравниваем количество постов в профиле
