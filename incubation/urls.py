from django.contrib import admin
from django.urls import path
from django.http import HttpResponse
# Simple home page view
def home(request):
    return HttpResponse("<h1>Welcome to the University of Johannesburg Technology Transfer officer (UJTTO) Entrepreneurship Support and Facilities Incubation Booking System</h1>")
urlpatterns = [
    path('', home),
    path('admin/', admin.site.urls),
    path('auth/', include('authapp.urls')),
]
