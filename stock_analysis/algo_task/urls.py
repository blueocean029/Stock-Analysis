from django.conf.urls import url, include
from rest_framework import routers as merouters
from views import StockAnalysis

router = merouters.SimpleRouter(trailing_slash=True)
router.register('get_stock_analysis', StockAnalysis, 'stock_analysis')

urlpatterns = []
urlpatterns.extend(router.urls)

print urlpatterns

