from django.urls import path
from . import views

app_name='item_register'
urlpatterns = [
    path('add/',views.AddItem.as_view(),name='add'),
    path('view/',views.ViewItem.as_view(),name='view'),
    path('update/<int:pk>',views.UpdateItem.as_view(),name='update'),
    path('delete/<int:pk>',views.DeleteItem.as_view(),name='delete'),
    path('add_bill/',views.AddBill.as_view(),name='add_bill'),
    path('newbill/',views.NewBill,name='new_bill'),
    path('tempitem/',views.TempItemCreateView.as_view(),name='addtempitem'),
    path('tempitemupdate/<int:pk>',views.TempItemEditView.as_view(),name='edittempitem'),
    path('tempitemdelete/<int:pk>',views.TempItemDeleteView.as_view(),name='deletetempitem'),
]
