from django.contrib import admin
from .models import User, Sensor, Data, Alert
# Register your models here.


admin.site.register(User)
admin.site.register(Sensor)
admin.site.register(Data)
admin.site.register(Alert)