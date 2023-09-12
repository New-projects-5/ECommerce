from django.urls import path

from apps.index.views import Index

app_name = 'index'

urlpatterns = [
    path('', Index.as_view(), name='index_page'),
]
