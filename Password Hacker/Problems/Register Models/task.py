from django.contrib import admin


class RatingAdmin(admin.ModelAdmin):
    pass

admin.site.register(Rating, RatingAdmin)
