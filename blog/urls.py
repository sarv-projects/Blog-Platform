from django.urls import path,include
from . import views
from .views import PostListAPIView
from blog.views import PostViewSet
from rest_framework.routers import DefaultRouter
router=DefaultRouter()
router.register(r'posts',PostViewSet,basename='post')

urlpatterns = [
    path('',views.post_list,name='post_list'),
    path('post/<int:pk>/',views.post_detail,name="post_detail"),
    path('api/posts/',PostListAPIView.as_view(),name="post-list-api"),
    path('api/',include(router.urls)),
]

#path('') maps the root of our blog app (e.g., http://localhost:8000/) to the post_list view.
#name='post_list' gives this URL a name, which is useful for referencing it later in templates.
#We've moved the API URLs to a dedicated api/ path to keep them separate from our standard Django URLs. This is a common architectural pattern.
#also,check in the website/api/posts
