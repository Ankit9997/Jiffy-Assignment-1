from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^list/$', views.PersonListView.as_view(), name='person_changelist'),
    url(r'^$', views.PersonCreateView.as_view(), name='person_add'),
    url(r'^(?P<pk>\d+)/$', views.PostDetailView.as_view(), name='person_detail'),
    url(r'^update/(?P<pk>\d+)/$', views.PersonUpdateView.as_view(), name='person_change'),
    url(r'^delete/(?P<pk>\d+)/$', views.PersonDeleteView.as_view(), name='person_delete'),
    url(r'^search/$', views.SearchResultsView.as_view(), name='search_results'),
    url(r'^home/$', views.HomePageView.as_view(), name='home'),
    url(r'^ajax/load-cities/$', views.load_cities, name='ajax_load_cities'),
    ]
