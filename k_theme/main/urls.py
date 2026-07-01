from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

from . import views

urlpatterns = [
    path("", views.main, name="main"),
    path("detail/<str:theme_pk>/", views.ktheme_detail, name="ktheme_detail"),
    path("detail/<str:theme_pk>/name/", views.ktheme_update_name, name="ktheme_update_name"),
    path("detail/<str:theme_pk>/image/", views.ktheme_upload_image, name="ktheme_upload_image"),
    path("detail/<str:theme_pk>/color/", views.ktheme_update_color, name="ktheme_update_color"),
    path("detail/<str:theme_pk>/bubble/", views.ktheme_update_bubble, name="ktheme_update_bubble"),
    path("detail/<str:theme_pk>/zip/", views.ktheme_create_zip, name="ktheme_create_zip"),
    path("detail/<str:theme_pk>/delete/", views.ktheme_delete, name="ktheme_delete"),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)