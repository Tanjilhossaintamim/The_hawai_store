from django.urls import path
from rest_framework_nested import routers
from store.views import ProductViewSet, CollectionViewSet, ReviewViewSet, CartViewSet, CartItemViewSet, OrderViewSet

router = routers.DefaultRouter()
router.register('products', ProductViewSet)
router.register('collections', CollectionViewSet)
router.register('cart', CartViewSet)
router.register('order', OrderViewSet, basename='order')

review_router = routers.NestedDefaultRouter(
    router, 'products', lookup='product')
review_router.register('review', ReviewViewSet, basename='review')

cart_router = routers.NestedDefaultRouter(router, 'cart', lookup='cart')
cart_router.register('items', CartItemViewSet, basename='cartitem')

urlpatterns = router.urls+review_router.urls+cart_router.urls
