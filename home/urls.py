from home import views
from django.urls import path

urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
    path('filter-content/', views.FilteredContentListView.as_view(), name='home'),
]