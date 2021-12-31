from django.db import models
# from embedvideofield import 
# from embed_video.fields import EmbedVideoField
# from embed_video.fields import EmbedVideoField

class jacps(models.Model):
   name=models.CharField(max_length=1000)
   batan=models.CharField(max_length=1000,default="some_string")
   url=models.CharField(max_length=1000,default="some_string")

class jacms(models.Model):
   name=models.CharField(max_length=1000)
   batan=models.CharField(max_length=1000,default="some_string")
   url=models.CharField(max_length=1000,default="some_string")


class jaccs(models.Model):
   name=models.CharField(max_length=1000)
   batan=models.CharField(max_length=1000,default="some_string")
   url=models.CharField(max_length=1000,default="some_string")

class jamps(models.Model):
   name=models.CharField(max_length=1000)
   batan=models.CharField(max_length=1000,default="some_string")
   url=models.CharField(max_length=1000,default="some_string")
class jamcs(models.Model):
   name=models.CharField(max_length=1000)
   batan=models.CharField(max_length=1000,default="some_string")
   url=models.CharField(max_length=1000,default="some_string")
class jamms(models.Model):
   name=models.CharField(max_length=1000)
   batan=models.CharField(max_length=1000,default="some_string")
   url=models.CharField(max_length=1000,default="some_string")
class jatps(models.Model):
   name=models.CharField(max_length=1000)
   batan=models.CharField(max_length=1000,default="some_string")
   url=models.CharField(max_length=1000,default="some_string")
class jatcs(models.Model):
   name=models.CharField(max_length=1000)
   batan=models.CharField(max_length=1000,default="some_string")
   url=models.CharField(max_length=1000,default="some_string")
class jatms(models.Model):
   name=models.CharField(max_length=1000)
   batan=models.CharField(max_length=1000,default="some_string")
   url=models.CharField(max_length=1000,default="some_string")


class video(models.Model):
   name=models.CharField(max_length=1000)
   batan=models.CharField(max_length=1000,default="some_string")
   url=models.CharField(max_length=1000,default="some_string")
   # icon=EmbedVideoField()
   
   # def __str__(self):
      # return str(self.name)
#    icon=

   
# Create your models here.
