from django.test import TestCase
from .forms import BookForm

# Create your tests here.

class TestBookForm(TestCase):
    def test_item_name_is_required(self):
        form=BookForm({'name': ''})
        self.assertFalse(form.is_valid())
        self.assertIn('name', form.errors.keys())
        self.assertEqual(form.errors['name'][0], 'This field is required')
