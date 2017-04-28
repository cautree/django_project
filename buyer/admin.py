from django.contrib import admin



from .models import Customer




class BuyerAdmin(admin.ModelAdmin):
	list_display =['name','email']

admin.site.register(Customer, BuyerAdmin)
