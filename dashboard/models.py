from django.db import models

# Create your models here.
# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Otherproducts(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    mrfppartno = models.TextField(db_column='MrfpPartNo', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    datasheet = models.TextField(blank=True, null=True)  # This field type is a guess.
    ref = models.TextField(db_column='REF', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    mounting = models.TextField(db_column='Mounting', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    value = models.TextField(db_column='VALUE', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    ht = models.TextField(db_column='HT', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    dia = models.TextField(db_column='Dia', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    spring_dia = models.TextField(db_column='Spring_Dia', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    material = models.TextField(db_column='Material', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    pitch = models.TextField(db_column='Pitch', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    three_d_drawing = models.TextField(db_column='Three_d_drawing', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    size_of_component = models.TextField(db_column='Size_of_component', blank=True, null=True)  # Field name made lowercase. This field type is a guess.

    class Meta:
        managed = False
        db_table = 'OtherProducts'


class Surfaceproducts(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    mrfppartno = models.TextField(db_column='MrfpPartNo', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    datasheet = models.TextField(blank=True, null=True)  # This field type is a guess.
    ref = models.TextField(db_column='REF', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    mounting = models.TextField(db_column='Mounting', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    value = models.TextField(db_column='VALUE', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    ht = models.TextField(db_column='HT', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    dia = models.TextField(db_column='Dia', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    spring_dia = models.TextField(db_column='Spring_Dia', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    material = models.TextField(db_column='Material', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    pitch = models.TextField(db_column='Pitch', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    three_d_drawing = models.TextField(db_column='Three_d_drawing', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    size_of_component = models.TextField(db_column='Size_of_component', blank=True, null=True)  # Field name made lowercase. This field type is a guess.

    class Meta:
        managed = False
        db_table = 'SurfaceProducts'


class Throughproducts(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    mrfppartno = models.TextField(db_column='MrfpPartNo', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    datasheet = models.TextField(blank=True, null=True)  # This field type is a guess.
    ref = models.TextField(db_column='REF', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    mounting = models.TextField(db_column='Mounting', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    value = models.TextField(db_column='VALUE', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    ht = models.TextField(db_column='HT', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    dia = models.TextField(db_column='Dia', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    spring_dia = models.TextField(db_column='Spring_Dia', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    material = models.TextField(db_column='Material', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    pitch = models.TextField(db_column='Pitch', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    three_d_drawing = models.TextField(db_column='Three_d_drawing', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    size_of_component = models.TextField(db_column='Size_of_component', blank=True, null=True)  # Field name made lowercase. This field type is a guess.

    class Meta:
        managed = False
        db_table = 'ThroughProducts'



# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class ChalanTable(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)
    chalanno = models.CharField(max_length=50, blank=True, null=True)
    user_id = models.IntegerField(blank=True, null=True)
    products = models.TextField(blank=True, null=True)
    prices = models.TextField(blank=True, null=True)
    qty = models.TextField(blank=True, null=True)
    rate = models.TextField(blank=True, null=True)
    amount = models.TextField(blank=True, null=True)
    date = models.DateField(blank=True, null=True)
    url = models.URLField(blank=True, null=True)
    # url1 = models.URLField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'chalantable'




class User(models.Model):
    id = models.AutoField(primary_key=True, db_column='ID')
    name = models.TextField(blank=True, null=True, db_column='name')
    company_name = models.TextField(blank=True, null=True, db_column='company_name')
    phone_number = models.CharField(max_length=20, blank=True, null=True)
    phone1 = models.CharField(max_length=20, blank=True, null=True, db_column='phone1')

    class Meta:
        managed = True
        db_table = 'User'

class Product(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.TextField(blank=True, null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'Producttable'

