from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$',views.index),
    url(r'^create$',views.create_qr),
    url(r'^code_process$',views.code_process),
    url(r'^qr_created/(?P<qr_id>\d+)$',views.qr_created),
    url(r'^login$',views.login),
    url(r'^login_process$',views.login_process),
    url(r'^register$',views.register),
    url(r'^register_process$',views.register_process),
    url(r'^master$',views.master)
    
]