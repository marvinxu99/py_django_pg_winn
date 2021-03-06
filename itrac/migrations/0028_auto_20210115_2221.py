# Generated by Django 3.1.4 on 2021-01-16 06:21

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import itrac.models.issue_attachment


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('itrac', '0027_issuetoissuelink_link_to_type'),
    ]

    operations = [
        migrations.CreateModel(
            name='IssueAttachment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(blank=True, max_length=255)),
                ('attachment', models.FileField(upload_to=itrac.models.issue_attachment.get_directory_path)),
                ('uploaded_at', models.DateTimeField(auto_now_add=True)),
                ('issue', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='attachments', to='itrac.issue')),
                ('uploaded_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='attachment_uploader', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'issue_attachment',
                'verbose_name_plural': 'issue_attachments',
                'db_table': 'itrac_issue_attachment',
                'ordering': ['description'],
            },
        ),
        migrations.AddIndex(
            model_name='issueattachment',
            index=models.Index(fields=['description'], name='itrac_issue_descrip_c05756_idx'),
        ),
    ]
