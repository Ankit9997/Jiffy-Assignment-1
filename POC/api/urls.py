from django.conf.urls import url
from .views import POCAPIView,POCDetailAPIView

urlpatterns=[
    url(r'^$',POCAPIView.as_view()),
    url(r'^(?P<pk>\d+)/$',POCDetailAPIView.as_view())
]
