from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("pages", "0004_multilang_content"),
    ]

    operations = [
        migrations.AlterField(
            model_name="cvsection",
            name="type",
            field=models.CharField(
                choices=[
                    ("summary", "Podsumowanie"),
                    ("experience", "Doswiadczenie"),
                    ("education", "Wyksztalcenie"),
                    ("skills", "Umiejetnosci"),
                    ("techstack", "Stos technologiczny"),
                    ("projects", "Projekty"),
                    ("certificates", "Certyfikaty"),
                    ("languages", "Jezyki"),
                    ("other", "Inne"),
                ],
                max_length=50,
            ),
        ),
    ]

