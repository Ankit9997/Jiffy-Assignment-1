from django import forms
from .models import Registration, City



class PersonForm(forms.ModelForm):
    # name = forms.CharField(disabled=True)
    class Meta:
        model = Registration
        fields = ['name', 'age','gender','country', 'city','zip','address']




    def __init__(self, *args, **kwargs):
        # super().__init__(*args, **kwargs)
        super(PersonForm, self).__init__(*args,**kwargs)
        self.fields['city'].queryset = City.objects.none()
        




        if 'country' in self.data:
            try:
                country_id = int(self.data.get('country'))
                self.fields['city'].queryset = City.objects.filter(country_id=country_id).order_by('name')
            except (ValueError, TypeError):
                pass  # invalid input from the client; ignore and fallback to empty City queryset
        elif self.instance.pk:
            self.fields['city'].queryset = self.instance.country.city_set.order_by('name')
