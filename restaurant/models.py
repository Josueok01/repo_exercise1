from django.db import models

class Menu(models.Model): 
    title = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2, db_index=True)
    inventory = models.IntegerField()

    def __str__(self):
        return f"{self.title} : {self.price}"

class Booking(models.Model): 
    name = models.CharField(max_length=255)
    no_of_guests = models.IntegerField()
    booking_date = models.DateTimeField()
