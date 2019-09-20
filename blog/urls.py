from django.urls import path
from . import views

urlpatterns = [
    path('', views.initiation, name='home'),
    path('login', views.login_view, name='createuser'),
    path('remove_event/<int:pk>', views.remove_event, name='remove_event'),
    path('create_event', views.create_event, name='create_event'),
    path('createuser', views.create_user, name='createuser'),
    path('logout', views.logout_view, name='logout'),
    path('initiation', views.initiation, name='initiation'),
    path('evenements', views.evenements, name='evenements'),
    path('cotisation', views.cotisation, name='cotisation'),
    path('donateur', views.donateur, name='donateur'),
    path('contact', views.contact, name='contact'),
    path('torcy', views.torcy, name='torcy'),
]

