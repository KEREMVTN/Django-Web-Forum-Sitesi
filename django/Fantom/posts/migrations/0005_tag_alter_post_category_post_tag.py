# Generated by Django 4.2.4 on 2023-08-30 10:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0004_post_category_alter_category_slug_alter_post_slug'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('slug', models.SlugField(editable=False)),
            ],
        ),
        migrations.AlterField(
            model_name='post',
            name='category',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='posts', to='posts.category'),
        ),
        migrations.AddField(
            model_name='post',
            name='tag',
            field=models.ManyToManyField(blank=True, related_name='posts', to='posts.tag'),
        ),
    ]
