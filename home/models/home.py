from django.db import models

class WhyChooseUs(models.Model):
   heading_name=models.CharField(max_length=500)
   icon_image=models.ImageField(upload_to='uploads/home/')
   description=models.TextField(default='description')

   def __str__(self):
        return str(self.heading_name)


class Slider(models.Model):
   slider_image=models.ImageField(upload_to='uploads/home/')
   

       