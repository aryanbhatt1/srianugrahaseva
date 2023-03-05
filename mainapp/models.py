from django.db import models

# Create your models here.

requirement_choices = [
    ('', 'Select Type'),
    ('type1', 'Type 1 - Planetary transit'),
    ('type2', 'Type 2 - House warming'),
    ('type3', 'Type 3 - Telugu Sampradaya'),
    ('type4', 'Type 4 - Homam'),
    ('type5', 'Type 5 - Sirartha'),
    ('type6', 'Type 6 - As per Telugu tradition')
]

services_choices = [
    ('', 'Select Services'),
    ('Vastu Puja','Vastu Puja'),
    ('Milk fever', 'Milk fever'),
    ('Ganapati Puja', 'Ganapati Puja'),
    ('Punyahavasanam', 'Punyahavasanam'),
    ('Ganapati Homam', 'Ganapati Homam'),
    ('Navagraha homam', 'Navagraha homam'),
    ('Lakshmi Homam', 'Lakshmi Homam'),
    ('All Dwara Pooja', 'All Dwara Pooja'),
    ('Agni Puja', 'Agni Puja'),
    ('Lakshmi Ganapati Homam', 'Lakshmi Ganapati Homam'),
    ('Satyanarayana Puja Lakshmi', 'Satyanarayana Puja Lakshmi'),
    ('Saffron consecration', 'Saffron consecration'),
    ('Satyanarayana Puja', 'Satyanarayana Puja'),
    ('Navagraha Puja', 'Navagraha Puja'),
    ('Loka Balakar Puja', 'Loka Balakar Puja'),
    ('Hall worship', 'Hall worship'),
    ('Lakshmi Kunguma Archana', 'Lakshmi Kunguma Archana'),
    ('Mrutyunjaya Homam', 'Mrutyunjaya Homam'),
    ('Sudarshana Homam', 'Sudarshana Homam'),
    ('Navagraha homam', 'Navagraha homam'),
    ('Lakshmi Homam', 'Lakshmi Homam'),
    ('Ayushya Homam', 'Ayushya Homam'),
    ('Chandi Homam', 'Chandi Homam'),
    ('Vastu Homam', 'Vastu Homam'),
    ('Dhanvantri Homam', 'Dhanvantri Homam'),
    ('Ashtalakshmi Homam', 'Ashtalakshmi Homam'),
    ('Durga Homam', 'Durga Homam'),
    ('Parvana Vidhana Sirartha', 'Parvana Vidhana Sirartha'),
    ('Hiranya Sirartham', 'Hiranya Sirartham'),
    ('No Moon Day', 'No Moon Day'),
    ('Tatnam (Sirartham)', 'Tatnam (Sirartham)'),
    ('Bindapradhanam Darpanam', 'Bindapradhanam Darpanam')
]

mode_choices = [
    ('0', 'Select Mode'),
    ('1', 'Offline'),
    ('2', 'Online')
]

class OrgDetails(models.Model):
    location = models.CharField('Location', max_length=40, null=True)
    email = models.EmailField('Email', null=True)
    facebook_url = models.CharField('Facebook', max_length=40, null=True)
    instagram_url = models.CharField('Instagram', max_length=40, null=True)
    youtube_url = models.CharField('Youtube', max_length=40, null=True)
    phone = models.CharField('Phone Number', max_length=14, null=True)


class slogan(models.Model):
    title = models.CharField('Title', max_length=30, null=True)
    media = models.FileField('Media', upload_to='audio', null=True)
    category = models.CharField('Category', max_length=30, null=True)
    duration = models.DecimalField('Duration', max_digits=6, decimal_places=2, null=True)
    caption = models.FileField('Caption', upload_to='vtt', null=True)

    def __str__(self):
        return self.title

class register(models.Model):
    first_name = models.CharField('First Name', max_length=40, null=True)
    last_name = models.CharField('Last Name', max_length=40, null=True)
    email = models.EmailField('Email', null=True)
    phonenumber = models.CharField('Phone Number', max_length=14, null=True)
    address = models.TextField('Address', null=True)
    postalCode = models.IntegerField('Postal Code', null=True)
    requirement = models.CharField('Requirement', max_length=50, choices=requirement_choices, null=True)
    services = models.CharField('Services', max_length=50, choices=services_choices, null=True)
    mode = models.CharField('Mode', max_length=50, choices=mode_choices, null=True)
    date = models.DateField('Date', null=True)
    others = models.TextField('Others', null=True)
