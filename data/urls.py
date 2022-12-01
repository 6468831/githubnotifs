from django.urls import path

from .views import *


urlpatterns = [
    path('', GitCommitView.as_view(), name='git-commit')
]