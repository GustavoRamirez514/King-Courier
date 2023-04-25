from django.db import migrations, models
from django.conf import settings
from django.db.backends.signals import connection_created
from django.dispatch import receiver
from django.test.runner import DiscoverRunner


class CustomTestRunner(DiscoverRunner):
    def setup_test_environment(self, *args, **kwargs):
        connection = settings.DATABASES['test']
        connection_name = connection['NAME']
        connection['NAME'] = ':memory:'
        super().setup_test_environment(*args, **kwargs)
        connection['NAME'] = connection_name


@receiver(connection_created)
def setup_test_db(connection, **kwargs):
    if connection.alias == 'test':
        connection.connection.executescript('PRAGMA foreign_keys=ON;')


class Migration(migrations.Migration):
    dependencies = []

    operations = [
        migrations.CreateModel(
            name='MyModel',
            fields=[
                ('id', models.AutoField(auto_created=True,
                 primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
            ],
        ),
        migrations.RunSQL('PRAGMA foreign_keys=ON;', reverse_sql=''),
    ]