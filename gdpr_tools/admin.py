from django.contrib import admin

from .models import Category, Cookie, Consent


class CategoryAdmin(admin.ModelAdmin):
    pass

class CookieAdmin(admin.ModelAdmin):
    pass

class ConsentAdmin(admin.ModelAdmin):
    pass

admin.site.register(Category, CategoryAdmin)
admin.site.register(Cookie, CookieAdmin)
admin.site.register(Consent, ConsentAdmin)
