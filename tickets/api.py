from ninja import NinjaAPI
from .models import Passenger, Ticket
from django.shortcuts import get_object_or_404
from django.contrib import admin
from .models import Passenger, PassengerType, Discount, Station, Zone, Ticket, Payment, PriceSettings

admin.site.register(Passenger)
admin.site.register(PassengerType)
admin.site.register(Discount)
admin.site.register(Station)
admin.site.register(Zone)
admin.site.register(Ticket)
admin.site.register(Payment)
admin.site.register(PriceSettings)

api = NinjaAPI()

@api.get("/passengers")
def list_passengers(request):
    return [{"id": p.id, "name": f"{p.first_name} {p.last_name}"} for p in Passenger.objects.all()]

@api.get("/tickets")
def list_tickets(request):
    return [
        {
            "id": t.id,
            "passenger": f"{t.passenger.first_name} {t.passenger.last_name}",
            "from": t.start_station.station_name,
            "to": t.end_station.station_name,
            "zones": t.number_of_zones,
            "price": float(t.price),
        }
        for t in Ticket.objects.select_related("passenger", "start_station", "end_station")
    ]