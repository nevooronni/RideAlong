from django.contrib import admin
from .models import Driver,DriverProfile,DriverReview,Rider,RiderProfile,RiderReview

admin.site.register(Driver)
admin.site.register(DriverProfile)
admin.site.register(DriverReview)
admin.site.register(Rider)
admin.site.register(RiderProfile)
admin.site.register(RiderReview)
