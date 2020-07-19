from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static


app_name = 'blog'

urlpatterns = [
    path('', views.home, name='home'),
    path('post/create/', views.create, name='create'),
    path('edit/<int:pk>/', views.edit, name='edit'),
    path('tags/<slug:tag>/', views.home, name='posts_by_tag'),
    path('delete/<int:pk>/', views.delete, name='delete'),
    path('post/<slug:slug>/', views.detail, name='detail'),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


