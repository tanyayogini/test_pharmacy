from rest_framework import routers

from products.views import ProductClientViewSet

router = routers.SimpleRouter()
router.register('client', ProductClientViewSet)

urlpatterns = router.urls
