from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path("", include("home.urls")),
    path("dahmenvidz/", admin.site.urls),
]

admin.site.site_header = "Vidz"
admin.site.site_title = "Vidz Admin Portal"
admin.site.index_title = "Vidz Admin"