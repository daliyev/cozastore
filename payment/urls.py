from django.urls import path
from . import views
from . import webhook

app_name = 'payment'

urlpatterns = [
    path('process/', views.payment_process, name='process'),
    path('completed/', views.payment_completed, name='completed'),
    path('canceled/', views.payment_canceled, name='canceled'),
    path('webhook/', webhook.stripe_webhook, name='stripe-webhook'),
]


# https://www.c-sharpcorner.com/article/how-to-schedule-automatic-shut-down-in-windows-10/