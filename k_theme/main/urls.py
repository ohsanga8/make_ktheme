from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("", views.main, name="main"),
    # path("create/", views.create_theme, name="create_theme"),
    path("detail/<str:id>/", views.ktheme_detail, name="ktheme_detail"),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
