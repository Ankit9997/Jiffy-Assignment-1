# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.http import HttpResponse
from django.shortcuts import render
from .models import Registration,City
from django.views.generic import ListView, CreateView, UpdateView,DetailView,DeleteView,TemplateView
from django.urls import reverse
from django.db.models import Q
from .forms import PersonForm
from django.core.paginator import Paginator
from django.core.urlresolvers import reverse_lazy


# Create your views here.

# def home(request):
#     context = {
#         'peoples': Registration.objects.all()
#     }
#     return render(request, 'blog/home.html', context)



class PersonListView(ListView):
    context = {
        'peoples': Registration.objects.all()
    }
    model = Registration
    template_name = 'POC/home.html'  # <app>/<model>_<viewtype>.html
    context_object_name = 'peoples'
    ordering = ['-date_posted']
    paginate_by = 3
    queryset = Registration.objects.all()


class PersonCreateView(CreateView):
    model = Registration
    form_class = PersonForm
    template_name = 'POC/registration_form.html'
    # fields = ['name', 'age', 'country', 'city','zip','address']


class PostDetailView(DetailView):
    model = Registration
    template_name = 'POC/registration_detail.html'

class PersonUpdateView(UpdateView):

    model = Registration
    form_class = PersonForm
    # fields = ('name', 'age', 'country', 'city','zip','address')
    #success_url = reverse('person_changelist')




class PersonDeleteView(DeleteView):
    model = Registration
    # success_url = '/'
    success_url = reverse_lazy('person_changelist')

    def get(self, *args, **kwargs):
        return self.post(*args, **kwargs)




class HomePageView(TemplateView):
    template_name = 'POC/home1.html'


class SearchResultsView(ListView):
    model = Registration
    template_name = 'POC/search_results.html'

    def get_queryset(self):
        query = self.request.GET.get('p')
        querycountry = self.request.GET.get('q')
        # print(querycountry)
        querycity=self.request.GET.get('r')

        if query not in '':
            object_list = Registration.objects.filter(Q(name__icontains=query))
            print(object_list)
            if object_list == '':
                return HttpResponse('<h1>Page Not Found</h1>')
            else:
                return object_list
        if querycountry not in '':
            object_list = Registration.objects.filter(Q(country__name=querycountry))
            print(object_list)
            if object_list is None:
                print(object_list)
                return render(request, 'POC/Error.html')
            else:
                return object_list
        if querycity not in '':

            object_list = Registration.objects.filter(Q(city__name=querycity))
            if object_list == '':
                return HttpResponse('<h1>Page Not Found</h1>')
            else:
                return object_list








def load_cities(request):
    country_id = request.GET.get('country')
    print(country_id)
    cities = City.objects.filter(country_id=country_id)
    return render(request, 'POC/city_dropdown_list_options.html', {'cities': cities})
