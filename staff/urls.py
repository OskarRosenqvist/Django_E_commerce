from django.urls import path
from .views import StaffView

app_name = 'staff'
urlpatterns = (
    path('', StaffView.as_view(), name='staff-view'),
)