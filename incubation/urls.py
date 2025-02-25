from django.contrib import admin
from django.urls import path
from django.http import HttpResponse
# Simple home page view
def home(request):
    return HttpResponse("<h1>Welcome to the Incubation Booking System</h1>")
urlpatterns = [
    path('', home),
    path('admin/', admin.site.urls),
]
