from django.urls import path
from .views import CreateView, RedirectView, AllUrlView

urlpatterns = [
    path("", CreateView),
    path("allurl/", AllUrlView),
    path("short_url/<str:url>/", RedirectView)
]
