from .views import (
     SearchProductView,
)
from django.conf.urls import url


urlpatterns = [
    url(r'^$', SearchProductView.as_view(), name='list'),
]
