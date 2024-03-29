from django.urls import path
from . import views

app_name = 'customer'
urlpatterns = [
    path('add/',views.addCustomer.as_view(),name='add'),
    path('view/',views.CustomerListView.as_view(),name='view'),
    path('delete/<int:pk>',views.CustomerDeleteView.as_view(),name='delete'),
    path('update/<int:pk>',views.CustomerUpdateView.as_view(),name='update'),
]
