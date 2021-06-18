from django.urls import path
from . import views

urlpatterns = [
    path('/', views.challenges),
    path('/<month>', views.monthly_challenge)

]
