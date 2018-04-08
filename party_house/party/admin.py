from django.contrib import admin
from .models import Party, PartyInformation, Testimonial

class PartyAdmin(admin.ModelAdmin):
    pass

class PartyInformationAdmin(admin.ModelAdmin):
    pass

class TestimonialAdmin(admin.ModelAdmin):
    pass

admin.site.register(Party)
admin.site.register(PartyInformation)
admin.site.register(Testimonial)
