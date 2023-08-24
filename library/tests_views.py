from django.test import TestCase
from django.test import TestCase
from django.urls import reverse
from library.models import Book


class LibraryHomeViewTest(TestCase):
    def test_library_home_view_status_code(self):
        url = reverse('library_home')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_library_home_view_template(self):
        url = reverse('library_home')
        response = self.client.get(url)
        self.assertTemplateUsed(response, 'library/library_home.html')


class CatalogViewTest(TestCase):
    def setUp(self):
        self.book1 = Book.objects.create(
            title='Book1',
            description='Description1',
            genre='fantasy_magic',
            num_pages=300,
            editorial='Editorial1',
            isbn='1234567890123',
            year_edition=2021,
            date_edition='2021-01-01',
            writer='Writer1'
        )
        self.book2 = Book.objects.create(
            title='Book2',
            description='Description2',
            genre='horror_fiction',
            num_pages=400,
            editorial='Editorial2',
            isbn='1234567890124',
            year_edition=2022,
            date_edition='2022-01-01',
            writer='Writer2'
        )

    def test_catalog_view_status_code(self):
        url = reverse('catalog')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_catalog_view_template(self):
        url = reverse('catalog')
        response = self.client.get(url)
        self.assertTemplateUsed(response, 'library/catalog.html')

    def test_catalog_search_by_title(self):
        url = reverse('catalog')
        response = self.client.get(url, {'query': 'Book1', 'field': 'title'})
        self.assertIn(self.book1, response.context['books'])
        self.assertNotIn(self.book2, response.context['books'])


class EventsViewTest(TestCase):
    def test_events_view_status_code(self):
        url = reverse('events')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_events_view_template(self):
        url = reverse('events')
        response = self.client.get(url)
        self.assertTemplateUsed(response, 'library/events.html')
class ContactViewTest(TestCase):
    def test_contact_view_status_code(self):
        url = reverse('contact')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_contact_view_template(self):
        url = reverse('contact')
        response = self.client.get(url)
        self.assertTemplateUsed(response, 'library/contact.html')

class AboutViewTest(TestCase):
    def test_about_view_status_code(self):
        url = reverse('about')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_about_view_template(self):
        url = reverse('about')
        response = self.client.get(url)
        self.assertTemplateUsed(response, 'library/about.html')
