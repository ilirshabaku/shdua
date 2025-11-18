from django.conf import settings   
from django.conf.urls.static import static
from django.urls import path
from .views_ushar import ushtar_create, vertetimi_pdf, ushar_list, ushtar_update, ushtar_delete, ushtar_retrieve
from .views_titullari import  titullari_dashboard, titullari_list, titullari_create, titullari_update, titullari_delete

urlpatterns = [
    path('', ushar_list, name='ushtar_list'),
    path('ushtar_create/', ushtar_create, name='ushtar_create'),
    path('ushtar_<str:pk>/retrieve/', ushtar_retrieve, name='ushtar_retrieve'),
    path('ushtar/<str:pk>/update/', ushtar_update, name='ushtar_update'),
    path('ushtar/<str:pk>/delete/', ushtar_delete, name='ushtar_delete'),

    path('titullari_dashboard/', titullari_dashboard, name='titullari_dashboard'),
    path('titullari_list/', titullari_list, name='titullari_list'),
    path('titullari_create/', titullari_create, name='titullari_create'),
    path('titullari/<int:pk>/update/', titullari_update, name='titullari_update'),
    path('titullari/<int:pk>/delete/', titullari_delete, name='titullari_delete'),

    path('<str:pk>/pdf', vertetimi_pdf, name='pdf'),
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
