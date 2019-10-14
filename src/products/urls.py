from .views import (
     ProductListView,
     # product_list_view,
     # ProductDetailView,
     ProductDetailSlugView,
     # product_detail_view,
     # ProductFeaturedDetailView,
     # ProductFeaturedListView
)


from django.conf.urls import url


urlpatterns = [
    url(r'^$', ProductListView.as_view()),
    url(r'^(?P<slug>[\w-]+)/$', ProductDetailSlugView.as_view()),
]


