from django.contrib import admin
from .models import Post
from .models import Champion
# Register your models here.

admin.site.register(Post)
admin.site.register(Champion)