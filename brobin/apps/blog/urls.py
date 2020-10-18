from django.urls import path

from .views import (
    PostListView,
    PostArchiveListView,
    PostCategoryListView,
    PostDetailView,
    SidebarAPIView
)

urlpatterns = [
    path('blog/sidebar', SidebarAPIView.as_view()),
    path('blog/archive/<int:year>', PostArchiveListView.as_view()),
    path('blog/<int:year>/<int:month>/<str:slug>', PostDetailView.as_view()),
    path('blog/<str:slug>', PostCategoryListView.as_view()),
    path('blog', PostListView.as_view())
]