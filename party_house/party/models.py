from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

class PartyInformation(models.Model):
    address_st = models.CharField(max_length=100, help_text="Enter the street name for the party")
    address_num = models.IntegerField(help_text="Enter the house address number, if none leave blank", blank=False)
    address_apt_num = models.CharField(max_length = 5, blank=True)
    address_zip = models.IntegerField(help_text="Enter the zip for the address", blank=False)
    address_city = models.CharField(max_length = 100, blank=False)
    description = models.CharField(max_length=750, help_text="Enter a description of the party (750 max characters!)", blank=False)
    date_of_party = models.DateField('Party Date', blank=False)
    active = models.BooleanField(help_text="Is the party active? True or False")
    creator = models.IntegerField(blank=False)
    def get_absolute_url(self):
        return reverse('party-information-detail', args=[str(self.id)])

    def __str__(self):
        return f'{self.address_zip}, {self.description}, {self.date_of_party}'

class Party(models.Model):
    party_information_id = models.OneToOneField('PartyInformation', on_delete=models.SET_NULL, null=True)
    party_thrower_id = models.ForeignKey(User, related_name='party_thrower_id', on_delete=models.SET_NULL, null=True)
    party_goer_id = models.ForeignKey(User, related_name = 'party_goer_id', on_delete=models.SET_NULL, null=True)
    applications = models.IntegerField(blank=True)
    status = models.IntegerField(blank=False, help_text="1 for pending, 2 for accepted, 3 for rejected")
    attended=models.BooleanField(blank=True)

    def get_absolute_url(self):
        return reverse('party-detail', args=[str(self.id)])

    def __str__(self):
        return f'{self.applications}, {self.active}'

class Attended(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    num_attended = models.IntegerField(blank=True, help_text="Number of parties that you've attended")
    num_thumbs = models.IntegerField(blank=True, help_text="Number of thumbs that you have")

    def get_absolute_url(self):
        return reverse('attended', args=[str(self.id)])

    def __str__(self):
        return f'{self.num_attended}, {self.num_thumbs}'

class Testimonial(models.Model):
    party_id = models.ForeignKey('Party', on_delete=models.SET_NULL, null=True)
    user_id = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    thumbs = models.BooleanField()
    description = models.CharField(max_length=750, help_text="How was this person?", blank=False)

    def get_absolute_url(self):
        return reverse('testimonial', args=[str(self.id)])

    def __str__(self):
        return f'{self.thumbs}, {self.description}'
