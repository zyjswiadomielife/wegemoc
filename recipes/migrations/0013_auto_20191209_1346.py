# Generated by Django 2.2.5 on 2019-12-09 13:46

from django.db import migrations, models
import django.db.models.deletion
import mptt.fields


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0012_recipecategory_author'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recipecategory',
            name='body',
            field=models.TextField(blank=True, help_text='To pole nie jest obowiązkowe. Jeśli jednak chcesz, napisz co będzie można znaleźć w tej kategorii.', verbose_name='Opis kategorii'),
        ),
        migrations.AlterField(
            model_name='recipecategory',
            name='image',
            field=models.ImageField(blank=True, default='defaultbgcategory.jpg', help_text='Dodając zdjęcie jesteś w stanie wyróżnić kategorię, jeśli jednak tego nie zrobisz nic się nie stanie. :)', null=True, upload_to='Tło', verbose_name='Tło kategorii'),
        ),
        migrations.AlterField(
            model_name='recipecategory',
            name='parent',
            field=mptt.fields.TreeForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='children', to='recipes.RecipeCategory', verbose_name='Kategoria'),
        ),
    ]
