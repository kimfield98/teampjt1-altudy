from django.urls import path
from . import views


app_name = 'studies'
urlpatterns = [
    path('', views.index, name='index'),
    path('<int:study_pk>/', views.detail, name='detail'),
    path('create/', views.create, name='create'),
    path('<int:study_pk>/delete/', views.delete, name='delete'),
    path('<int:study_pk>/update/', views.update, name='update'),
    path('<int:study_pk>/join/', views.join, name='join'),
    path('<int:study_pk>/withdraw/', views.withdraw, name='withdraw'),
    path('<int:study_pk>/accept/<username>/', views.accept, name='accept'),
    path('<int:study_pk>/reject/<username>/', views.reject, name='reject'),
    path('<int:study_pk>/expel/<username>/', views.expel, name='expel'),
    
    # 알람 페이지 -임시-
    path('alarm/', views.alarm, name='alarm'),

    # mainboard
    path('<int:study_pk>/mainboard/', views.mainboard, name='mainboard'),
]