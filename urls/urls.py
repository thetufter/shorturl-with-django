from django.urls import path
from .views import RootUrlApiView, ForwardUrlApiView, UrlAdminApiView

urlpatterns = [
    path('', RootUrlApiView.as_view()),
    path('manage/<str:secret_key>', UrlAdminApiView.as_view()),
    path('<str:key>', ForwardUrlApiView.as_view()),
]
