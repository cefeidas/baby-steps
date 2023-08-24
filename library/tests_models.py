from django.test import TestCase
from library.forms import SearchForm, CSVImportForm
from django.core.files.uploadedfile import SimpleUploadedFile
from library.models import Book


class SearchFormTest(TestCase):
    def test_empty_fields(self):
        form = SearchForm(data={})
        self.assertFalse(form.is_valid())

    def test_valid_options(self):
        valid_data = {'query': 'Test', 'field': 'title'}
        form = SearchForm(data=valid_data)
        self.assertTrue(form.is_valid())

    def test_invalid_field_option(self):
        invalid_data = {'query': 'Test', 'field': 'invalid_option'}
        form = SearchForm(data=invalid_data)
        self.assertFalse(form.is_valid())

class CSVImportFormTest(TestCase):
    def test_valid_csv_file(self):
        csv_file = SimpleUploadedFile("file.csv", b"file_content")
        form = CSVImportForm(files={'csv_file': csv_file})
        self.assertTrue(form.is_valid())

    def test_invalid_file(self):
        txt_file = SimpleUploadedFile("file.txt", b"file_content")
        form = CSVImportForm(files={'csv_file': txt_file})
        self.assertFalse(form.is_valid())