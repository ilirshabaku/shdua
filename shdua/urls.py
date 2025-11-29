from django.conf import settings   
from django.conf.urls.static import static
from django.urls import path
from .views_ushar import ushtar_create, pdf_me_kosdakt, pdf_pa_kosdakt, ushar_list, ushtar_update, ushtar_delete, ushtar_retrieve
from .views_titullari import  titullari_dashboard, titullari_list, titullari_create, titullari_update, titullari_delete
from .views_firmat import firmat_dashboard, firmat_list, firmat_create, firmat_update, firmat_delete

urlpatterns = [
    path('', ushar_list, name='ushtar_list'),
    path('ushtar_create/', ushtar_create, name='ushtar_create'),
    path('ushtar_<int:pk>/retrieve/', ushtar_retrieve, name='ushtar_retrieve'),
    path('ushtar/<int:pk>/update/', ushtar_update, name='ushtar_update'),
    path('ushtar/<int:pk>/delete/', ushtar_delete, name='ushtar_delete'),


    path('titullari_dashboard/', titullari_dashboard, name='titullari_dashboard'),
    path('titullari_list/', titullari_list, name='titullari_list'),
    path('titullari_create/', titullari_create, name='titullari_create'),
    path('titullari/<int:pk>/update/', titullari_update, name='titullari_update'),
    path('titullari/<int:pk>/delete/', titullari_delete, name='titullari_delete'),

    path('firmat_dashboard/', firmat_dashboard, name='firmat_dashboard'),
    path('firmat_list/', firmat_list, name='firmat_list'),
    path('firmat_create/', firmat_create, name='firmat_create'),
    path('firmat/<int:pk>/update/', firmat_update, name='firmat_update'),
    path('firmat/<int:pk>/delete/', firmat_delete, name='firmat_delete'),

    path('<int:pk>/pdf_me_kosdakt', pdf_me_kosdakt, name='pdf_me_kosdakt'),
    path('<int:pk>/pdf_pa_kosdakt', pdf_pa_kosdakt, name='pdf_pa_kosdakt'),
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
