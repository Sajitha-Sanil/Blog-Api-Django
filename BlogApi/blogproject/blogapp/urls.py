from django.urls import path
from rest_framework_simplejwt.views import TokenRefreshView
from . import views

urlpatterns = [

    path('login/', views.UserLoginView.as_view(), name='login'),
    path('refresh-token/', TokenRefreshView.as_view(), name='token_refresh'),
    path('blog/create/', views.BlogPostListCreateView.as_view(), name='blog-create'),
    path('blog/', views.BlogPostListView.as_view(), name='blog-list'),
    path('blog/<slug:slug>/', views.BlogPostDetailView.as_view(), name='blogdetail'),

    path('blog_edit/<slug:slug>/', views.BlogPostRetrieveUpdateDeleteView.as_view(), name='blog-retrieve-update-delete'),
    path('blog/hashtag/<str:hashtag>/', views.BlogPostSearchByHashtagView.as_view(), name='blog-search-by-hashtag'),

]