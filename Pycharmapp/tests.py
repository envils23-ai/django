from django.test import TestCase
from django.urls import reverse


class UrlsStatusCodeTests(TestCase):
    def test_home_page_returns_200(self):
        """Главная страница ('') возвращает 200."""
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)

    def test_home_page_correct_location(self):
        """Главная страница ('') возвращает 200."""
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)

    def test_about_page_returns_200(self):
        """Страница 'about/' возвращает 200."""
        response = self.client.get(reverse('about'))
        self.assertEqual(response.status_code, 200)

    def test_about_page_correct_location(self):
        """Страница 'about/' возвращает 200."""
        response = self.client.get('/about/')
        self.assertEqual(response.status_code, 200)



    def test_home_page_contains_h1(self):
        """На главной странице есть заголовок <h1>Home1</h1>."""
        response = self.client.get(reverse('home'))
        self.assertContains(response, '<h1>Home2</h1>')

    def test_home_page_contains_about_link(self):
        """На главной странице есть ссылка на страницу About."""
        response = self.client.get(reverse('home'))
        about_url = reverse('about')
        self.assertContains(response, f'<a href="{about_url}">About</a>', html=True)