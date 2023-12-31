# Generated by Django 4.1.3 on 2023-11-17 11:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("main", "0007_delete_kthemeimages"),
    ]

    operations = [
        migrations.AlterField(
            model_name="csscolor",
            name="bg_color",
            field=models.CharField(
                default="#FFFFFF", max_length=7, verbose_name="배경 컬러"
            ),
        ),
        migrations.AlterField(
            model_name="csscolor",
            name="input_bg_color",
            field=models.CharField(
                default="#D3D3D3", max_length=7, verbose_name="입력창 컬러"
            ),
        ),
        migrations.AlterField(
            model_name="csscolor",
            name="main_text_color",
            field=models.CharField(
                default="#000000", max_length=7, verbose_name="메인 텍스트 컬러"
            ),
        ),
        migrations.AlterField(
            model_name="csscolor",
            name="point_text_color",
            field=models.CharField(
                default="#FFC0CB", max_length=7, verbose_name="강조 텍스트 컬러"
            ),
        ),
        migrations.AlterField(
            model_name="csscolor",
            name="receive_text_color",
            field=models.CharField(
                default="#808080", max_length=7, verbose_name="받은 말풍선 텍스트 컬러"
            ),
        ),
        migrations.AlterField(
            model_name="csscolor",
            name="send_text_color",
            field=models.CharField(
                default="#A9A9A9", max_length=7, verbose_name="보낸 말풍선 텍스트 컬러"
            ),
        ),
        migrations.AlterField(
            model_name="ktheme",
            name="name",
            field=models.CharField(max_length=50, verbose_name="테마 이름"),
        ),
    ]
