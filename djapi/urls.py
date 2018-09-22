from django.urls import path

from . import views

app_name = 'djapi'
urlpatterns = [
    path('', views.QueryView.as_view(), name='index'),
    path('<int:query_id>/', views.results, name='results')
]
