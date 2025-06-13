from django.db import models

class Discount(models.Model):
    discount_type = models.CharField(max_length=100)
    percentage = models.DecimalField(max_digits=5, decimal_places=0)
    duration = models.PositiveIntegerField()

    def __str__(self):
        return f"{self.discount_type} ({self.percentage}%)"

class PassengerType(models.Model):
    type_name = models.CharField(max_length=100)
    description = models.TextField()
    is_valid = models.BooleanField(default=True)
    discount = models.ForeignKey(Discount, on_delete=models.PROTECT, null=False, blank=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.type_name

class Passenger(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    passenger_type = models.ForeignKey(PassengerType, on_delete=models.PROTECT, null=False, blank=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

class Zone(models.Model):
    zone_id = models.DecimalField(max_digits=2, decimal_places=0)
    valid_from = models.DateField()
    valid_to = models.DateField(null=True, blank=True)

    def __str__(self):
        return f" {self.zone_id}"

class Station(models.Model):
    station_name = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    address = models.CharField(max_length=255)
    zone = models.ForeignKey(Zone, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.station_name

class PriceSettings(models.Model):
    price_per_zone = models.DecimalField(max_digits=6, decimal_places=2)
    valid_from = models.DateField()
    valid_to = models.DateField(null=True, blank=True)

    def __str__(self):
        return f"{self.price_per_zone} €"

class Ticket(models.Model):
    passenger = models.ForeignKey(Passenger, on_delete=models.CASCADE, null=True, blank=True)
    first_name = models.CharField(max_length=50, blank=True)
    last_name = models.CharField(max_length=50, blank=True)
    start_station = models.ForeignKey(Station, related_name='tickets_starting', on_delete=models.CASCADE)
    end_station = models.ForeignKey(Station, related_name='tickets_ending', on_delete=models.CASCADE)
    discount = models.ForeignKey(Discount, on_delete=models.SET_NULL, null=True, blank=True)
    number_of_zones = models.PositiveIntegerField()
    valid_from = models.DateTimeField()
    valid_until = models.DateTimeField()
    created_at = models.DateTimeField(auto_now_add=True)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    price_setting = models.ForeignKey(PriceSettings, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return f"Ticket #{self.id} for {self.passenger}"

class Payment(models.Model):
    passenger = models.ForeignKey(Passenger, on_delete=models.CASCADE, null=True, blank=True)
    ticket = models.OneToOneField(Ticket, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=6, decimal_places=2)
    payment_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Payment for ticket #{self.ticket.id}"