from django import forms
from .models import Passenger, Payment
from .models import Station
from django.utils import timezone
from .models import Zone


class PassengerForm(forms.ModelForm):
    class Meta:
        model = Passenger
        fields = ['first_name', 'last_name', 'passenger_type']
        

from django import forms
from .models import Ticket, Station

class TicketSaleForm(forms.Form):
    use_registered_passenger = forms.BooleanField(
        required=False,
        label="Použiť registrovaného pasažiera"
    )
    first_name = forms.CharField(max_length=50, required=False)
    last_name = forms.CharField(max_length=50, required=False)

    start_station = forms.ModelChoiceField(queryset=Station.objects.all())
    end_station = forms.ModelChoiceField(queryset=Station.objects.all())
    valid_until = forms.DateTimeField(widget=forms.DateTimeInput(attrs={'type': 'date'}))
    
    
class StationForm(forms.ModelForm):
    class Meta:
        model = Station
        fields = ['station_name', 'city', 'address', 'zone']
        labels = {
            'station_name': 'Názov stanice',
            'city': 'Mesto',
            'address': 'Adresa',
            'zone': 'Zóna',
        }
        
from .models import Zone

class ZoneForm(forms.ModelForm):
    class Meta:
        model = Zone
        fields = ['zone_id', 'valid_from', 'valid_to']
        labels = {
            'zone_id': 'ID zóny',
            'valid_from': 'Platná od',
            'valid_to': 'Platná do (voliteľné)',
        }
        widgets = {
            'valid_from': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
            'valid_to': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
        }
        
