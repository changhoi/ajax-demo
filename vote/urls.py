from django.urls import path

from . import views

urlpatterns = [
    path('form/', views.FormView.as_view(), name='form'),
    path('ajax/', views.AjaxView.as_view(), name='ajax')
]