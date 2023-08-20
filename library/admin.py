import sys
print("Python Paths:", sys.path)

import csv
from django.contrib import admin
from django.urls import path
from django.shortcuts import render
from .models import Book
from .forms import CSVImportForm

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
            reader = csv.reader(csv_file.read().decode('utf-8').splitlines())
            for row in reader:
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
            self.message_user(request, "CSV file has been imported")
            return redirect("..")
        form = CSVImportForm()
        payload = {"form": form}
        return render(request, "admin/csv_form.html", payload)

admin.site.register(Book, BookAdmin)

