from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('nutritionAPI', '0015_alter_savedmeal_foods'),
    ]

    operations = [
        migrations.AddField(
            model_name='savedmeal',
            name='serving_multipliers',
            field=models.JSONField(default=dict),
        ),
    ]
