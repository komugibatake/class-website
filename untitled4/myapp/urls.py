from django.conf.urls import url, include
from .views import HomeView, AboutView, PeopleView
from rest_framework import routers
from myapp.api import views as api_views



router = routers.DefaultRouter()
router.register(r'people', api_views.PersonViewSet)


urlpatterns = [
    url(r'^home', HomeView.as_view(), name = 'home'),
    url(r'^about', AboutView.as_view(), name = 'about'),
    url(r'^people', PeopleView.as_view(), name = 'people'),
    url(r'^', include(router.urls))

]
