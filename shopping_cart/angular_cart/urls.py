from django.conf.urls import include, url

from views import IndexView, CategoriesView, ProductsView, PlaceOrderView 


urlpatterns = [
    url(r'^$', IndexView.as_view(), name='index'),
    url(r'^categorise/$', CategoriesView.as_view(), name='get_categories'),
    url(r'^products/(?P<category_id>\d+)$', ProductsView.as_view(), name='get_products'),
    url(r'^place-order/$', PlaceOrderView.as_view(), name='place_order_view'),
]
