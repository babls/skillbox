from app_store.models import Shop, Product, History_shopping
from django.contrib.auth.models import User
from django.test import TestCase
from django.urls import reverse

NUMBER_SHOP = 10
USER_EMAIL = 'test@email.ru'
PASSWORD = '123wW132'


class UsersAnonimusTest(TestCase):  # Тест постов, добавляет 10 штук

    def test_profile(self):
        url = reverse('profile')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'app_users/profile.html')
        self.assertContains(response, 'Вы не авторизованы на нашем сайте!')


class ProfileUserTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        test_user = User.objects.create_user(username='test', email='test@email.ru', password='test')

    def test_register_user(self):
        response = self.client.post(reverse('login'), {'username': 'test', 'password': 'test'})

        response_profile = self.client.get('/profile/')
        self.assertEqual(response_profile.status_code, 200)
        self.assertContains(response_profile, 'Логин пользователя: test')


class RegisterUserTest(TestCase):

    def test_register_user(self):
        url = reverse('register')
        response = self.client.get(url)
        response_post = self.client.post(url, {
            'username': 'test_username',
            'first_name': 'test_name',
            'last_name': 'test_surname',
            'email': 'test@mail.ru',
            'city': 'Test_sity',
            'telephone_number': '89991117733',
            'about_myself': 'TEST_TEXT',
            'password1': PASSWORD,
            'password2': PASSWORD
        })
        self.assertTemplateUsed(response, 'app_users/register.html')
        response_profile = self.client.get('/profile/')
        self.assertEqual(response_profile.status_code, 200)
        self.assertContains(response_profile, 'Логин пользователя: test_username')


class HistoryShoppingTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        test_user = User.objects.create_user(username='test', email='test@email.ru', password='test')

    def test_history_shopping_user(self):
        url = reverse('history_shopping')

        user = User.objects.get(username='test')
        self.client.post(reverse('login'), {'username': 'test', 'password': 'test'})

        for i in range(1, 11):                      # Добавляем 10 Магазинов
            shop = Shop.objects.create(name=f'Магазин {i}')
            for j in range(1, 4):                   # Добавляем каждому 3 товара
                product = Product.objects.create(
                    name=f'Продукт {j}',
                    price=j,
                    category='Test',
                )

                product.shop.add(shop)

                History_shopping.objects.create(    # Записываем покупку в историю
                    date_of_shopping='2022-05-27',
                    shop=shop,
                    product=product,
                    count=1,
                    total=j,
                    user=user
                )

        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'app_users/history_shopping.html')
        self.assertContains(response, 'Продукт 3')
        self.assertContains(response, 'Магазин 10')
        self.assertTrue(len(response.context['history']) == 10*3) # Проверяем сколько создалось покупок
