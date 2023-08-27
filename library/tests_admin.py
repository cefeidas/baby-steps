from django.test import TestCase, Client
from django.core.files.uploadedfile import SimpleUploadedFile
from library.models import Book


class BookAdminTestCase(TestCase):

    def setUp(self):
        self.client = Client()

    def test_import_csv_post_request(self):
        csv_content = "title,description,genre,num_pages,editorial,isbn,year_edition,date_edition,writer,image_url\n" \
                      "Sample Title,Sample Description,Sample Genre,300,Sample Editorial,1234567890,2022,01-01-2022,Sample Writer,http://sample.com/image.jpg"

        csv_file = SimpleUploadedFile(
            'test.csv', csv_content.encode('utf-8'), content_type='text/csv')

        response = self.client.post(
            '/admin/library/book/import-csv/', {'csv_file': csv_file})
        self.assertEqual(response.status_code, 302)

        self.assertEqual(Book.objects.count(), 1)

        book = Book.objects.first()
        self.assertEqual(book.title, "Sample Title")
