from django.contrib import admin
from .models import Districts,Branches,NetBankingCustomer

# Register your models here.
admin.site.register(Districts)
admin.site.register(Branches)
admin.site.register(NetBankingCustomer)

