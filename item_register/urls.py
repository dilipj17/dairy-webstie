from django.urls import path
from . import views

app_name = 'item_register'
urlpatterns = [
    path('add_customer/',views.addCustomer.as_view(),name='add_customer'),
    path('view_customer/',views.CustomerListView.as_view(),name='view_customer'),
    path('delete/<int:id>',views.CustomerDeleteView.as_view(),name='delete_customer'),
    path('update/<int:pk>',views.CustomerUpdateView.as_view(),name='update_customer'),
]
