from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('welcome_page.urls', namespace='welcome_page')),
    path('pages/', include('other_pages.urls', namespace='other_pages')),
]
