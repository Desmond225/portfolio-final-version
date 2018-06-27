from django.db import models
from datetime import datetime

# create a blog model

class Blog(models.Model):
    title = models.CharField(max_length=200)
    p_date = models.DateTimeField('Date published')
    body = models.TextField()
    image = models.ImageField(upload_to='images/')

    def __str__(self):
        return self.title

    def summary(self):
        return self.body[:100]

    def pub_date_modified(self):
        return datetime.now().strftime('%d-%m-%Y %H:%M:%S')


#add blog app to settings

#create migration

#migrate

#add to the admin
