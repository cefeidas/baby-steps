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

    def clean_csv_file(self):
        file = self.cleaned_data.get('csv_file')
        if file:
            if not file.name.endswith('.csv'):
                raise forms.ValidationError("File must be a CSV file.")
        return file

class UserSearchForm(forms.Form):
    USER_SEARCH_FIELDS = (
        ('username', 'User Name'),
        ('reviews', 'Reviews'),
        ('ratings', 'Ratings'),
    )

    query = forms.CharField(label='Search:', required=True)
    field = forms.ChoiceField(choices=USER_SEARCH_FIELDS)
