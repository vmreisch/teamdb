from django.urls import path
from .views import AthleteList, AthleteDetail

urlpatterns = [
    path('athletes/', AthleteList.as_view(), name='athlete-list'),
    path('athletes/<int:pk>/', AthleteDetail.as_view(), name='athlete-detail')
]