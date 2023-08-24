from .forms import CSVImportForm
from .models import Book
from django.shortcuts import render
from django.urls import path
from django.contrib import admin
import csv
import sys
from django.shortcuts import redirect

print("Python Paths:", sys.path)


class BookAdmin(admin.ModelAdmin):
    change_list_template = 'admin/book_changelist.html'

    def get_urls(self):
        urls = super().get_urls()
        my_urls = [
            path('import-csv/', self.import_csv),
        ]
        return my_urls + urls

    def import_csv(self, request):
        if request.method == "POST":
            csv_file = request.FILES["csv_file"]

            # Check if the file is in UTF-8 format
            encoding = chardet.detect(csv_file.read())['encoding']
            if encoding.lower() != 'utf-8':
                messages.error(request, "The file is not in UTF-8 format")
                return redirect("..")
            csv_file.seek(0)  # Reset file pointer

            reader = csv.reader(csv_file.read().decode('utf-8').splitlines())
            next(reader)  # Skip the header row

            expected_columns = 10  # Expected number of columns

            for row in reader:
                if len(row) != expected_columns:
                    messages.error(
                        request, f"Row with incorrect number of columns: {row}")
                    continue  # Skip this row and continue with the next one

                try:
                    book = Book(
                        title=row[0],
                        description=row[1],
                        genre=row[2],
                        num_pages=int(row[3]),
                        editorial=row[4],
                        isbn=row[5],
                        year_edition=int(row[6]),
                        date_edition=row[7],
                        writer=row[8],
                        image_url=row[9],
                    )
                    book.save()
                except ValueError as e:
                    messages.error(
                        request, f"Error processing the row {row}: {e}")
                    continue  # Skip this row and continue with the next one

            messages.success(request, "CSV file has been imported")
            return redirect("..")
        form = CSVImportForm()
        payload = {"form": form}
        return render(request, "admin/csv_form.html", payload)


admin.site.register(Book, BookAdmin)
