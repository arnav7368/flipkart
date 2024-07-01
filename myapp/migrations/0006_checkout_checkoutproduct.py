# Generated by Django 4.2.4 on 2024-06-27 09:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("myapp", "0005_wishlist"),
    ]

    operations = [
        migrations.CreateModel(
            name="Checkout",
            fields=[
                ("id", models.AutoField(primary_key=True, serialize=False)),
                (
                    "orderstatus",
                    models.IntegerField(
                        choices=[
                            (0, "Order is Placed"),
                            (1, "Order is Packed"),
                            (2, "Ready to Dispatch"),
                            (3, "Dispatched"),
                            (4, "Out For Delivery"),
                            (5, "Delivered"),
                        ],
                        default=0,
                    ),
                ),
                (
                    "paymentstatus",
                    models.IntegerField(
                        choices=[(0, "Pending"), (1, "Done")], default=0
                    ),
                ),
                (
                    "paymentmode",
                    models.IntegerField(
                        choices=[(0, "COD"), (1, "NetBanking")], default=0
                    ),
                ),
                ("subtotal", models.IntegerField()),
                ("shipping", models.IntegerField()),
                ("total", models.IntegerField()),
                (
                    "rppid",
                    models.CharField(blank=True, default="", max_length=20, null=True),
                ),
                ("date", models.DateTimeField(auto_now=True)),
                (
                    "buyer",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="myapp.buyer"
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="CheckoutProduct",
            fields=[
                ("id", models.AutoField(primary_key=True, serialize=False)),
                ("qty", models.IntegerField()),
                ("total", models.IntegerField()),
                (
                    "checkout",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="myapp.checkout"
                    ),
                ),
                (
                    "product",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="myapp.product"
                    ),
                ),
            ],
        ),
    ]