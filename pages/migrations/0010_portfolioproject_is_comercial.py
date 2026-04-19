from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("pages", "0009_offeritem_and_offer_texts"),
    ]

    operations = [
        migrations.AddField(
            model_name="portfolioproject",
            name="is_comercial",
            field=models.BooleanField(blank=True, default=None, null=True),
        ),
    ]
