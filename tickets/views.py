from django.shortcuts import render, get_object_or_404, redirect
from .models import Passenger, PriceSettings, Ticket, Station, Payment
from .forms import PassengerForm, TicketSaleForm
from django.utils import timezone
from decimal import Decimal
from django.contrib import messages
from .models import Station
from .forms import StationForm
from django.db.models import Q
from .forms import ZoneForm

def station_list(request):
    stations = Station.objects.all()
    return render(request, 'tickets/station_list.html', {'stations': stations})

def create_station(request):
    if request.method == 'POST':
        form = StationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('station_list')
    else:
        form = StationForm()
    return render(request, 'tickets/create_station.html', {'form': form})

def edit_station(request, station_id):
    station = get_object_or_404(Station, pk=station_id)
    if request.method == 'POST':
        form = StationForm(request.POST, instance=station)
        if form.is_valid():
            form.save()
            return redirect('station_list')
    else:
        form = StationForm(instance=station)
    return render(request, 'tickets/edit_station.html', {'form': form, 'station': station})



def search_passenger(request):
    query = request.GET.get('q', '')
    results = []

    if query:
        results = Passenger.objects.filter(
            Q(first_name__icontains=query) | Q(last_name__icontains=query)
        )

    return render(request, 'tickets/search_passenger.html', {
        'query': query,
        'results': results
    })

def passenger_list(request):
    passengers = Passenger.objects.all()
    return render(request, 'tickets/passenger_list.html', {'passengers': passengers})

def passenger_detail(request, passenger_id):
    passenger = get_object_or_404(Passenger, pk=passenger_id)
    tickets = Ticket.objects.filter(passenger=passenger)
    return render(request, 'tickets/passenger_detail.html', {
        'passenger': passenger,
        'tickets': tickets
    })


def passenger_create(request):
    if request.method == 'POST':
        form = PassengerForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('passenger_list')
    else:
        form = PassengerForm()
    return render(request, 'tickets/passenger_form.html', {'form': form})


def ticket_sale_view(request):
    context = {}
    if request.method == 'POST':
        form_type = request.POST.get('form_type')
        form = TicketSaleForm(request.POST)

        if form.is_valid():
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            start = form.cleaned_data['start_station']
            end = form.cleaned_data['end_station']
            valid_until = form.cleaned_data['valid_until'].replace(hour=23, minute=59, second=59)

            price_setting = PriceSettings.objects.order_by('-valid_from').first()
            if not start.zone or not end.zone:
                context['error'] = "Stanice nemajú priradenú zónu."
                return render(request, 'tickets/ticket_sale_form.html', context)

            number_of_zones = abs(start.zone.zone_id - end.zone.zone_id)
            base_price = number_of_zones * price_setting.price_per_zone

            discount = None
            discount_percent = 0
            passenger = None

            if form_type == 'registered':
                passenger_id = request.POST.get('passenger_id')
                passenger = Passenger.objects.filter(pk=passenger_id).first()
                if not passenger:
                    context['error'] = "Registrovaný pasažier nebol nájdený."
                    return render(request, 'tickets/ticket_sale_form.html', context)
                discount = passenger.passenger_type.discount if passenger.passenger_type else None
                discount_percent = discount.percentage if discount else 0
            else:
                passenger_type = form.cleaned_data.get('passenger_type')
                discount = passenger_type.discount if passenger_type else None
                discount_percent = discount.percentage if discount else 0

            final_price = base_price * (1 - Decimal(discount_percent) / 100)

            ticket = Ticket.objects.create(
                passenger=passenger,
                first_name=first_name if not passenger else '',
                last_name=last_name if not passenger else '',
                start_station=start,
                end_station=end,
                number_of_zones=number_of_zones,
                valid_from=timezone.now(),
                valid_until=valid_until,
                created_at=timezone.now(),
                price_setting=price_setting,
                price=final_price,
                discount=discount
            )
            

            context.update({
                'success': f"Lístok #{ticket.id} bol vystavený. Cena: {final_price:.2f} EUR",
                'ticket': ticket,
                'base_price': base_price,
                'final_price': final_price,
                'form': TicketSaleForm()
            })
            
            context['registered_passengers'] = Passenger.objects.all()
            return render(request, 'tickets/ticket_sale_form.html', context)
            

    else:
        form = TicketSaleForm()

    context['form'] = form
    context['registered_passengers'] = Passenger.objects.all()
    return render(request, 'tickets/ticket_sale_form.html', context)

def ticket_list(request):
    tickets = Ticket.objects.select_related('passenger', 'start_station', 'end_station')
    return render(request, 'tickets/ticket_list.html', {'tickets': tickets})


def create_zone(request):
    if request.method == 'POST':
        form = ZoneForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('station_list') 
    else:
        form = ZoneForm()
    return render(request, 'tickets/create_zone.html', {'form': form})

def home(request):
    return render(request, 'tickets/home.html')