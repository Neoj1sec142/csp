from django.urls import path
from . import views
from .views import PortfolioListView, PortfolioDetailView, PortfolioUpdateView, PortfolioDeleteView, PortfolioCreateView

urlpatterns = [
    path('', PortfolioListView.as_view(), name='portfolio-home'),
    path('<int:pk>/', PortfolioDetailView.as_view(), name='portfolio-detail'),
    # path('user/<str:username>', UserPostListView.as_view(), name='user-posts'),
    path('<int:pk>/update', PortfolioUpdateView.as_view(), name='portfolio-update'),
    path('<int:pk>/delete', PortfolioDeleteView.as_view(), name='portfolio-delete'),
    path('new/', PortfolioCreateView.as_view(), name='portfolio-create'),
    path('about/', views.about, name='portfolio-about'),
]