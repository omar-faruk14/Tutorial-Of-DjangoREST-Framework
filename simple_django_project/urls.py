
from django.contrib import admin
from django.urls import path,include
from home import views
from home.views import HelloWorld

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.display,name='First'),
    #path('api/', views.Apidisplay,name='api'),
    path('hello/', HelloWorld.as_view(), name='hello_world'),
    path('api_test/', views.homedata, name='hello'),
]