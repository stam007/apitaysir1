from django.contrib import admin
from .models import Details,SendRequest,ReciveRequest,History


# Register your models here.

admin.site.register(Details)
admin.site.register(SendRequest)
admin.site.register(ReciveRequest)
admin.site.register(History)



