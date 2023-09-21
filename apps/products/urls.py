from django.urls import path

from . import views

app_name = 'products'

urlpatterns = [
    path('', views.ProductListAPIView.as_view()),
    path('<str:category>/<slug:slug>/', views.ProductDetailAPIView.as_view()),
    path('create/', views.ProductCreateAPIView.as_view()),
]
