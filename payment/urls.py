from django.urls import path
from . import views

app_name = 'payment'
urlpatterns = [
    path('pay/',views.AddTransection.as_view(),name='pay'),
    path('view/',views.ViewTransection.as_view(),name='view'),
    path('delete/<int:pk>',views.DeleteTransection.as_view(),name='delete'),
    path('api/balance',views.giveBalance,name='apibalance'),
]
