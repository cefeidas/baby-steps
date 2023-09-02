from .forms import CSVImportForm
from .models import Book
from django.shortcuts import render, redirect
from django.urls import path
from django.contrib import admin
import csv
import sys
from datetime import datetime
from django.contrib import messages

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

            # Attempt to decode the file as UTF-8
            try:
                file_content = csv_file.read().decode('utf-8')
            except UnicodeDecodeError:
                messages.error(request, "The file is not in UTF-8 format")
                return redirect("..")

            reader = csv.reader(file_content.splitlines())
            next(reader)  # Skip the header row

            expected_columns = 10  # Expected number of columns

            for row in reader:
                if len(row) != expected_columns:
                    messages.error(
                        request, f"Row with incorrect number of columns: {row}")
                    continue  # Skip this row and continue with the next one

                try:
                    # Convert date to correct format
                    date_str = row[7]
                    date_obj = datetime.strptime(date_str, '%d-%m-%Y')
                    correct_format_date = date_obj.strftime(
                        '%Y-%m-%d')  # <-- Date conversion

                    book = Book(
                        title=row[0],
                        description=row[1],
                        genre=row[2],
                        num_pages=int(row[3]),
                        editorial=row[4],
                        isbn=row[5],
                        year_edition=int(row[6]),
                        date_edition=correct_format_date,  # <-- Use converted date
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
