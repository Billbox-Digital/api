from django.db import models

class Country (models.Model):
    name = models.CharField(max_length=255, null=True)

class State (models.Model):
    # use for province also
    name = models.CharField(max_length=255, null=True)

class City (models.Model):
    # use for district also
    name = models.CharField(max_length=255, null=True)

class SocialDomain (models.Model):
    name = models.CharField(max_length=255, null=True)
    description = models.TextField(null=True, blank=True)

class Link (models.Model):
    username = models.CharField(max_length=255, null=True)
    social_domain = models.ForeignKey(SocialDomain, on_delete=models.PROTECT, null=True)
    full_url = models.SmallIntegerField(default=0)
    user = models.BigIntegerField(default=0)

class Contact (models.Model):
    # use for district also
    phone1 = models.BigIntegerField(default=0)
    phone2 = models.BigIntegerField(default=0)
    email1 = models.CharField(max_length=255, null=True)
    email2 = models.CharField(max_length=255, null=True)
    social_json = models.TextField()
    user = models.BigIntegerField(default=0)

class Address(models.Model):
    billboxcode = models.CharField(max_length=12, null=True)
    address1 = models.CharField(max_length=255, null=True)
    address2 = models.CharField(max_length=255, null=True)
    address3 = models.CharField(max_length=255, null=True)
    country = models.ForeignKey(Country, on_delete=models.PROTECT, null=True)
    state = models.ForeignKey(State, on_delete=models.PROTECT, null=True)
    city = models.ForeignKey(City, on_delete=models.PROTECT, null=True)
    zipcode = models.CharField(max_length=32, null=True)
    postalcode = models.CharField(max_length=32, null=True)
    lat = models.DecimalField(max_digits=8, decimal_places=6, null=True)
    lng = models.DecimalField(max_digits=9, decimal_places=6, null=True)
    phone = models.BigIntegerField(default=0)
    user = models.BigIntegerField(default=0)

class Website (models.Model):
    username = models.CharField(max_length=32, null=True)
    domain_name = models.CharField(max_length=255, null=True)
    title = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    contact = models.ForeignKey(Contact, on_delete=models.PROTECT, null=True)
    address = models.ForeignKey(Address, on_delete=models.PROTECT, null=True)
    user = models.BigIntegerField(default=0)

class WebSettings (models.Model):
    # Site Identity: Title, Description, Logo, LogoType, Cover, 
    # Color 2 colors
    # Theme Options
    # Backgroun Image
    # fonts 2
    # language 3
    # currency 2
    # category 
    # Other info under discussion...


    i = True

class WebHomepage(models.Model):
    #item to be drop in front end need in Json format
    i = True

class WebMenu (models.Model):
    target_id = models.BigIntegerField(default=0)
    # target_collection = models.CharField(
        # max_length=1, choices=WEBSITE_NAVIGATION, default=W1)
    label = models.CharField(max_length=255, null=True)
    # position = models.CharField(
        # max_length=1, choices=WEBSITE_NAVIGATION, default=W1)
    nav_order = models.BigIntegerField(default=0)
    website = models.ForeignKey(Website, on_delete=models.PROTECT, null=True)
    website1 = models.SmallIntegerField()

