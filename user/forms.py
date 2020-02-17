from django import forms
#from .models import Profile
from django.contrib.auth.models import User
from user.models import Profile, Address
from farm.models import Farm, WaterResource, Plots, Soil, Ploting, Reports

class NameForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name']
        widgets = {
            "first_name": forms.TextInput(attrs={'placeholder': 'First Name', 'class': 'form-control', 'required': 'required', 'autofocus':'""'}),
            "last_name": forms.TextInput(attrs={'placeholder': 'Last Name', 'class': 'form-control', 'required': 'required'}),
            }
            
class MobileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['mobile']
        widgets = {
            "mobile": forms.TextInput(attrs={'placeholder': 'Mobile', 'class': 'form-control', 'required': 'required'}),
            }


class AddressForm(forms.ModelForm):
    class Meta:
        model = Address
        fields = ['line_1', 'town', 'landmark', 'city','district', 'state','pin']
        widgets = {
            "line_1": forms.TextInput(attrs={'placeholder': 'Address Line', 'class': 'form-control', 'required': 'required', 'autofocus':'""'}),
            "town": forms.TextInput(attrs={'placeholder': 'Town /Village', 'class': 'form-control', 'required': 'required'}),
            "landmark": forms.TextInput(attrs={'placeholder': 'Landmark', 'class': 'form-control', 'required': 'required'}),
            "city": forms.TextInput(attrs={'placeholder': 'City', 'class': 'form-control', 'required': 'required'}),
            "district": forms.TextInput(attrs={'placeholder': 'District', 'class': 'form-control', 'required': 'required'}),
            "state": forms.Select(attrs={'placeholder': 'Select State', 'class': 'form-control', 'required': 'required'}),
            "pin": forms.TextInput(attrs={'placeholder': 'Area Pincode', 'class': 'form-control', 'required': 'required'}),
            }

class AddFarmForm(forms.ModelForm):
    
    class Meta:
        model = Farm
        fields = ['location', 'soil','water_resource','area']
        widgets = {
            "soil": forms.Select(attrs={'placeholder': 'Select Soil', 'class': 'form-control', 'required': 'required', 'autofocus':'""'}),
            "location": forms.Select(attrs={'placeholder': 'Select Address', 'class': 'form-control', 'required': 'required'}),
            "water_resource": forms.Select(attrs={'placeholder': 'select Water Resource', 'class': 'form-control', 'required': 'required'}),
            "area": forms.TextInput(attrs={'placeholder': 'Area in Acres', 'class': 'form-control', 'required': 'required'}),
            }

    def __init__(self, user, *args, **kwargs):
        super(AddFarmForm, self).__init__(*args, **kwargs)
        self.fields['water_resource'].queryset = WaterResource.objects.filter(
            owner=user)
        self.fields['location'].queryset = Address.objects.filter(
            user=user)


class AddWaterResourceForm(forms.ModelForm):
    class Meta:
        model = WaterResource
        fields = ['volume', 'depth', 'diameter','income_rate', 'available_water','type']
        widgets = {
            "volume": forms.TextInput(attrs={'placeholder': 'Volume in Litres', 'class': 'form-control', 'required': 'required'}),
            "depth": forms.TextInput(attrs={'placeholder': 'Depth', 'class': 'form-control', 'required': 'required'}),
            "diameter": forms.TextInput(attrs={'placeholder': 'Diameter', 'class': 'form-control', 'required': 'required'}),
            "income_rate": forms.TextInput(attrs={'placeholder': 'Income Rate', 'class': 'form-control', 'required': 'required'}),
            "available_water": forms.TextInput(attrs={'placeholder': 'Available Water', 'class': 'form-control', 'required': 'required'}),
            "type": forms.Select(attrs={'placeholder': 'Select Type', 'class': 'form-control', 'required': 'required'}),
            }


class AddPlotsForm(forms.ModelForm):

    class Meta:
        model = Plots
        fields = ['farm', 'area']
        widgets = {
            "farm": forms.Select(attrs={'placeholder': 'farm', 'class': 'form-control', 'required': 'required', 'autofocus':'""'}),
            "area": forms.Select(attrs={'placeholder': 'area', 'class': 'form-control', 'required': 'required'})
        }

    def __init__(self, user, *args, **kwargs):
        super(AddPlotsForm, self).__init__(*args, **kwargs)
        self.fields['farm'].queryset = Farm.objects.filter(owner=user)


class AddPlotingForm(forms.ModelForm):

    class Meta:
        model = Ploting
        fields = ['plot', 'crop']
        widgets = {
            "plot": forms.Select(attrs={'placeholder': 'Select Plot', 'class': 'form-control', 'required': 'required', 'autofocus':'""'}),
            "crop": forms.Select(attrs={'placeholder': 'Select Crop', 'class': 'form-control', 'required': 'required'})
        }


class AddReportsImageForm(forms.ModelForm):

    class Meta:
        model = Reports
        fields = ['ploting', 'file']
        widgets = {
            "ploting": forms.Select(attrs={'placeholder': 'Select Plot', 'class': 'form-control', 'required': 'required', 'autofocus':'""'}),
        }

    '''def __init__(self, user, *args, **kwargs):
        super(AddReportsImageForm, self).__init__(*args, **kwargs)
        self.fields['ploting'].queryset = Ploting.objects.filter(user=user)'''
            