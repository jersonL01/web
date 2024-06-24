# Generated by Django 4.0.4 on 2024-06-20 22:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Carrito',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('codigo_producto', models.IntegerField()),
                ('nombre_producto', models.CharField(max_length=50)),
                ('precio_producto', models.IntegerField()),
                ('cantidad', models.IntegerField()),
                ('total', models.IntegerField()),
                ('imagen', models.ImageField(upload_to='', verbose_name='imagen')),
                ('usuario_producto', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='TipoObras',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tecnica', models.CharField(max_length=50)),
                ('created_at', models.DateField(auto_now_add=True)),
                ('update_at', models.DateField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='TipoUsuario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tipo', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('codigo_usuario', models.IntegerField(primary_key=True, serialize=False)),
                ('nombre_usuario', models.CharField(max_length=30)),
                ('correo', models.CharField(max_length=20)),
                ('telefono', models.CharField(max_length=12)),
                ('direccion', models.CharField(max_length=30)),
                ('created_at', models.DateField(auto_now_add=True)),
                ('update_at', models.DateField(auto_now=True)),
                ('tipo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.tipousuario')),
            ],
        ),
        migrations.CreateModel(
            name='Producto',
            fields=[
                ('codigo_producto', models.IntegerField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=50)),
                ('precio', models.IntegerField()),
                ('stock', models.IntegerField()),
                ('descripcion', models.CharField(max_length=100)),
                ('historia', models.CharField(max_length=100)),
                ('imagen', models.ImageField(blank=True, null=True, upload_to='')),
                ('created_at', models.DateField(auto_now_add=True)),
                ('update_at', models.DateField(auto_now=True)),
                ('tecnica', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.tipoobras')),
            ],
        ),
    ]
