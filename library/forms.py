from django import forms


class SearchForm(forms.Form):
    SEARCH_FIELDS = (
        ('title', 'Title'),
        ('writer', 'Writer'),
        ('genre', 'Genre'),
        ('editorial', 'Editorial'),
        ('isbn', 'ISBN'),
    )

    query = forms.CharField(label='Search:', required=True)
    field = forms.ChoiceField(choices=SEARCH_FIELDS)


class CSVImportForm(forms.Form):
    csv_file = forms.FileField()