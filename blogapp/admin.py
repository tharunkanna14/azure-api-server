from django.contrib import admin
from .models import Post,Secrets



class PostAdmin(admin.ModelAdmin):
	list_display = ('title','text','published_date')


admin.site.register(Post,PostAdmin)
admin.site.register(Secrets)


