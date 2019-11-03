from django.urls import path
from . import views

app_name = 'reports'
urlpatterns = [
    path('',views.LedgerQueryView.as_view(),name='report'),
    path('ledger/',views.ledgerView,name='list'),
]
