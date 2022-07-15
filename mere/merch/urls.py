from django.urls import path
from . import views
from .views import MerchPostListView, MerchPostDetailView, MerchPostCreateView, MerchPostUpdateView, MerchPostDeleteView

urlpatterns = [
    path('', MerchPostListView.as_view(), name='merch-home'),
    path('post/<int:pk>', MerchPostDetailView.as_view(), name='merch-detail'),
    # path('user/<str:username>', UserPostListView.as_view(), name='user-posts'),
    path('post/<int:pk>/update', MerchPostUpdateView.as_view(), name='merch-update'),
    path('post/<int:pk>/delete', MerchPostDeleteView.as_view(), name='merch-delete'),
    path('post/new', MerchPostCreateView.as_view(), name='merch-create'),
    path('about/', views.about, name='merch-about'),
]