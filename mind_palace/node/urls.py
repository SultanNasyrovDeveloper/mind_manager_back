from rest_framework import routers

from .api.body import NodeBodyViewSet
from .api.node import MindPalaceNodeViewSet
from .api.media import MindPalaceNodeMediaViewSet


router = routers.DefaultRouter()
router.register('media', MindPalaceNodeMediaViewSet)
router.register('bodies', NodeBodyViewSet)
router.register('nodes', MindPalaceNodeViewSet)


urlpatterns = router.urls