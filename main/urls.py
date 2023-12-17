from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('menu/', views.menu, name='menu'),
    path('add', views.addprod, name='add'),
    path('hatyn/<slug:post_url>', views.hatynka, name='hatynka'),
    path('hatyn/<slug:post_url>/buy', views.buy, name='contact'),
    path('logout', views.logout_user, name='logout'),
    path('hatyn/<slug:post_url>/update', views.update, name='update_hatyn'),
    path('hatyn/<slug:post_url>/delete', views.delete, name='delete_hatyn'),
    path('zams', views.zamovlenia, name='zam')
]