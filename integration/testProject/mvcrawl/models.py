from django.db import models

from django.contrib import admin

 

# Create your models here.

class DjangoTest(models.Model) :

     userID = models.CharField(max_length=20, db_column='userID')

     contents = models.CharField(max_length=255, db_column='contents')

     accessTime = models.DateTimeField(db_column='accessTime')

 

     class Meta :

         db_table = 'DjangoTest'

        

     def __unicode__(self) :

            return "%s %s" %(self.id, self.userID)

  

 class DjangoTestAdmin(admin.ModelAdmin):

     list_display = ["id", "userID", "contents", accessTime"]

     search_fields = ["userID"]
