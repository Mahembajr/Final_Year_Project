
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ClubViewSet, EventViewSet, JobViewSet, AssistanceOptionViewSet, user_profile

# Create a router and register our viewsets with it.
router = DefaultRouter()
router.register(r'clubs', ClubViewSet, basename='club')
router.register(r'events', EventViewSet, basename='event')
router.register(r'jobs', JobViewSet, basename='job')
router.register(r'assistance', AssistanceOptionViewSet, basename='assistance')

# The API URLs are now determined automatically by the router.
urlpatterns = [
    path('api/', include(router.urls)),
    path('api/profile/', user_profile, name='user_profile'),
]
