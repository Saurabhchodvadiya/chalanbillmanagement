# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class chalantable(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    chalanno = models.TextField(db_column='chalanno', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    user_id = models.TextField(blank=True, null=True)  # This field type is a guess.
    products = models.TextField(db_column='products', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    prices = models.TextField(db_column='prices', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    qty = models.TextField(db_column='qty', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    rate = models.TextField(db_column='rate', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    amount = models.TextField(db_column='amount', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    date = models.DateField(db_column='date', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'chalantable'



class Usertable(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    name = models.TextField(db_column='name', blank=True, null=True)
    comapny_name = models.TextField(db_column='name', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    phone = models.TextField(blank=True, null=True)  # This field type is a guess.
    phone1 = models.TextField(db_column='phone1', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    

    class Meta:
        managed = False
        db_table = 'Usertable'

class Producttable(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    name = models.TextField(db_column='name', blank=True, null=True)
    price = models.TextField(blank=True, null=True)  # This field type is a guess.
    class Meta:
        managed = False
        db_table = 'Usertable'

