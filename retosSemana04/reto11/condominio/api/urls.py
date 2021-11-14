from django.urls import path

from . import views

urlpatterns = [
  path('',views.index),
  path('propietarios',views.propietarios),
  path('edificios',views.edificios),
  path('departamentos',views.departamentos),
  path('propietarios/<int:propietario_id>',views.propietario),

]