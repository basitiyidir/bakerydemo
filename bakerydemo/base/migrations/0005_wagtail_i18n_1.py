# Generated by Django 2.1.7 on 2019-03-27 11:09

from django.db import migrations, models
import django.db.models.deletion
import wagtail_i18n.models


class Migration(migrations.Migration):

    dependencies = [
        ('wagtail_i18n', '0008_region_ordering'),
        ('base', '0004_auto_20180522_1856'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='formfield',
            options={},
        ),
        migrations.AddField(
            model_name='footertext',
            name='locale',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='+', to='wagtail_i18n.Locale'),
        ),
        migrations.AddField(
            model_name='footertext',
            name='translation_key',
            field=models.UUIDField(editable=False, null=True),
        ),
        migrations.AddField(
            model_name='formfield',
            name='locale',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='+', to='wagtail_i18n.Locale'),
        ),
        migrations.AddField(
            model_name='formfield',
            name='translation_key',
            field=models.UUIDField(editable=False, null=True),
        ),
        migrations.AddField(
            model_name='formpage',
            name='locale',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='+', to='wagtail_i18n.Locale'),
        ),
        migrations.AddField(
            model_name='formpage',
            name='translation_key',
            field=models.UUIDField(editable=False, null=True),
        ),
        migrations.AddField(
            model_name='gallerypage',
            name='locale',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='+', to='wagtail_i18n.Locale'),
        ),
        migrations.AddField(
            model_name='gallerypage',
            name='translation_key',
            field=models.UUIDField(editable=False, null=True),
        ),
        migrations.AddField(
            model_name='homepage',
            name='locale',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='+', to='wagtail_i18n.Locale'),
        ),
        migrations.AddField(
            model_name='homepage',
            name='translation_key',
            field=models.UUIDField(editable=False, null=True),
        ),
        migrations.AddField(
            model_name='people',
            name='locale',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='+', to='wagtail_i18n.Locale'),
        ),
        migrations.AddField(
            model_name='people',
            name='translation_key',
            field=models.UUIDField(editable=False, null=True),
        ),
        migrations.AddField(
            model_name='standardpage',
            name='locale',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='+', to='wagtail_i18n.Locale'),
        ),
        migrations.AddField(
            model_name='standardpage',
            name='translation_key',
            field=models.UUIDField(editable=False, null=True),
        ),
    ]
