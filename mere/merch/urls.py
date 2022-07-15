from django.urls import path
from . import views
from .views import MerchListView, MerchDetailView, MerchUpdateView, MerchDeleteView, MerchCreateView

urlpatterns = [
    path('', MerchListView.as_view(), name='merch-home'),
    path('<int:pk>/', MerchDetailView.as_view(), name='merch-detail'),
    # path('user/<str:username>', UserPostListView.as_view(), name='user-posts'),
    path('<int:pk>/update', MerchUpdateView.as_view(), name='merch-update'),
    path('<int:pk>/delete', MerchDeleteView.as_view(), name='merch-delete'),
    path('new/', MerchCreateView.as_view(), name='merch-create'),
    path('about/', views.about, name='merch-about'),
]