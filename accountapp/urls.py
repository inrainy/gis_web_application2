from django.urls import path

from accountapp.views import hi_world, AccountCreateView

app_name = 'accountapp'

urlpatterns = [
    path('hi_world/', hi_world, name='hi_world'),
    
    path('create/', AccountCreateView.as_view(), name='create')
]