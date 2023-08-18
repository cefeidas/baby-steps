# Generated by Django 3.2.20 on 2023-08-15 17:32

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0002_auto_20230810_1918'),
    ]

    operations = [
        migrations.RenameField(
            model_name='book',
            old_name='author',
            new_name='editorial',
        ),
        migrations.RenameField(
            model_name='book',
            old_name='ISBN',
            new_name='isbn',
        ),
        migrations.RemoveField(
            model_name='book',
            name='available_for_download',
        ),
        migrations.RemoveField(
            model_name='book',
            name='available_for_loan',
        ),
        migrations.RemoveField(
            model_name='book',
            name='code',
        ),
        migrations.RemoveField(
            model_name='book',
            name='location',
        ),
        migrations.AddField(
            model_name='book',
            name='date_edition',
            field=models.DateField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='book',
            name='description',
            field=models.TextField(default='Insert description here'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='book',
            name='image_url',
            field=models.URLField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='book',
            name='num_pages',
            field=models.PositiveIntegerField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='book',
            name='writer',
            field=models.CharField(default='Insert name of the writer here', max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='book',
            name='year_edition',
            field=models.PositiveIntegerField(default=2000),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='book',
            name='genre',
            field=models.CharField(choices=[('folk_tales', 'Folk tales'), ('fantasy_magic', 'Fantasy and magic'), ('african_history', 'History of African countries'), ('children_10_12', "Children's literature for 10 to 12 year olds"), ('french_literature', 'French literature'), ('spanish_literature', 'Spanish literature'), ('science_fiction_new', 'Science fiction'), ('humorous_fiction', 'Humorous fiction'), ('horror_fiction', 'Horror fiction'), ('travel_literature', 'Travel literature'), ('foreign_lit_18th', 'Foreign literature up to the 18th century'), ('fantastic_fiction', 'Fantastic fiction'), ('horror_pocketbooks', 'Horror pocketbooks')], max_length=50),
        ),
    ]
