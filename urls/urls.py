from django.urls import path
from .views import CreateUrlApiView, ForwardUrlApiView, UrlAdminApiView

urlpatterns = [
    path('', CreateUrlApiView.as_view()),
    path('manage/<str:secret_key>', UrlAdminApiView.as_view()),
    path('<str:key>', ForwardUrlApiView.as_view()),
]
