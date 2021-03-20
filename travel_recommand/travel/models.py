from django.db import models
from enum import Enum
# Create your models here....
# Comment
class User(models.Model):
    username = models.CharField(max_length=200,unique=True)
    password = models.CharField(max_length=15)
    email = models.EmailField(unique=True)
    contact = models.IntegerField()
    gender = models.CharField(max_length=1)
    dob = models.DateField()

    def __str__(self):
        return str(self.id)

 
class User_Account(models.Model):
    account_id=models.IntegerField(primary_key=True,auto_created=True)
    user_id=models.ForeignKey(User,default=1,on_delete=models.SET_DEFAULT)
    account_balance=models.FloatField()

    def __str__(self):
        return str(self.account_id)

class Destination(models.Model):
    dest_id=models.IntegerField(primary_key=True,auto_created=True)
    dest_name=models.CharField(max_length=200,unique=True)
    state=models.CharField(max_length=200)
    temprature=models.FloatField()
    humidity=models.FloatField()

    def __str__(self):
        return str(self.dest_id)     

class placeTypeChoice(Enum):   # A subclass of Enum
    beach = "beach"
    shopping = "shopping"
    historical = "historical"
    tracking = "tracking"
    religious = "religious"
    relaxing = "relaxing"

class Place(models.Model):
    place_id=models.IntegerField(primary_key=True,auto_created=True)
    dest_id=models.ForeignKey(Destination,default=1,on_delete=models.SET_DEFAULT)    
    name_place=models.CharField(max_length=100)
    desc_place=models.CharField(max_length=400)
    latitude=models.FloatField()
    longitude=models.FloatField()
    extra_charge=models.FloatField()
    time_durationForVisit=models.TimeField()
    rate_place=models.FloatField()
    type_of_Place=models.CharField(max_length=15, choices=[(tag, tag.value) for tag in placeTypeChoice] ) #enum, beach, shopping, historical, tracking, religious, relexing

    def __str__(self):
        return str(self.place_id)          

class Place_Review(models.Model):
    place_id=models.ForeignKey(Place,default=1,on_delete=models.SET_DEFAULT)
    user_id=models.ForeignKey(User,default=1,on_delete=models.SET_DEFAULT)    
    review_place=models.TextField(max_length=1000,null=True)
    rate_place=models.FloatField()

    class Meta:
        unique_together = (("user_id", "place_id"))

    def __str__(self):
        return str(self.place_id)+' '+str(self.user_id)

class Place_Image(models.Model):
    image_id=models.IntegerField()
    place_id=models.ForeignKey(Place,default=1,on_delete=models.SET_DEFAULT)
    image_of_place=models.ImageField(height_field=500,width_field=500)

    class Meta:
        unique_together = (("image_id", "place_id"))
    def __str__(self):
        return str(self.image_id)

class User_Input(models.Model):
    trip_id=models.IntegerField(primary_key=True,auto_created=True)
    user_id=models.ForeignKey(User,default=1,on_delete=models.SET_DEFAULT)    
    dest_id=models.ForeignKey(Destination,default=1,on_delete=models.SET_DEFAULT)    
    #source_id=models.ForeignKey(Destination,default=1,on_delete=models.SET_DEFAULT)    
    starting_date=models.DateField()
    ending_date=models.DateField()
    no_of_adult =models.IntegerField()              
    no_of_child =models.IntegerField()
    budget=models.CharField(max_length=10)                   # choice low, moderate, high
    visit_place_type= models.CharField(max_length=15, choices=[(tag, tag.value) for tag in placeTypeChoice] )        #enum
    trans_to_choose=models.CharField(max_length=10)           # own car, texi, bus

    def __str__(self):
        return str(self.trip_id)


class Itinerary(models.Model):
    trip_id=models.ForeignKey(User_Input,default=1,on_delete=models.SET_DEFAULT)
    place_id=models.ForeignKey(Place,default=1,on_delete=models.SET_DEFAULT)
    arrival_DnT=models.DateTimeField()
    departure_DnT=models.DateTimeField()

    class Meta:
        unique_together = (("place_id", "trip_id"))

    def __str__(self):
        return str(self.trip_id)

        
class Hotel(models.Model):
    hotel_id=models.IntegerField(primary_key=True,auto_created=True)
    hotel_name=models.CharField(max_length=200)
    dest_id=models.ForeignKey(Destination,default=1,on_delete=models.SET_DEFAULT)    
    type_of_room=models.CharField(max_length=20)
    latitude=models.FloatField()
    longitude=models.FloatField()
    stayCharge_dayPerRoom=models.FloatField()
    mealCharge_perPerson=models.FloatField()
    capacity=models.IntegerField()
    service=models.CharField(max_length=200)
    rate_hotel=models.FloatField()
    image_hotel=models.ImageField(height_field=500, width_field=500)
    type_of_hotel=models.CharField(max_length=200)                      # choice : luxury, first class,star of hotel, frontend side handling

    def __str__(self):
        return str(self.hotel_id)

class Hotel_Booking(models.Model):
    trip_id=models.ForeignKey(User_Input,default=1,on_delete=models.SET_DEFAULT)
    hotel_id=models.ForeignKey(Hotel,default=1,on_delete=models.SET_DEFAULT)
    date_of_booking_hotel=models.DateField()
    charge_hotel=models.FloatField()
    no_of_room=models.IntegerField()

    class Meta:
        unique_together = (("hotel_id", "trip_id"))

    def __str__(self):
        return str(self.trip_id)+' '+str(self.hotel_id)



# Genralization is required

class Transport(models.Model):
    trans_id=models.IntegerField(primary_key=True,auto_created=True)
    driver_name=models.CharField(max_length=100)
    place_hold_once_sd=models.ForeignKey(Destination,default=1,on_delete=models.SET_DEFAULT) 
    place_hold_once_sd=models.ForeignKey(Destination,default=1,on_delete=models.SET_DEFAULT) 
    trans_contact=models.IntegerField()
    capacity_trans=models.IntegerField()
    charge_per_person=models.FloatField()

    def __str__(self):
        return str(self.trans_id)

class Transport_Booking(models.Model):
    trans_id=models.ForeignKey(Transport,default=1,on_delete=models.SET_DEFAULT)
    trip_id=models.ForeignKey(User_Input,default=1,on_delete=models.SET_DEFAULT)
    date_ofBooking_trans=models.DateField()
    start_dateOfTrans=models.DateField()
    end_dateOfTrans=models.DateField()
    source=models.CharField(max_length=200)
    type_of_trans=models.CharField(max_length=10)
    no_of_person_onTrans=models.IntegerField()
    charge_of_trans=models.FloatField()

    class Meta:
        unique_together = (("trans_id", "trip_id"))

    def __str__(self):
        return str(self.trip_id)+' '+str(self.trans_id)

class Taxi_Booking(models.Model):
    trans_id=models.ForeignKey(Transport,default=1,on_delete=models.SET_DEFAULT)
    trip_id=models.ForeignKey(User_Input,default=1,on_delete=models.SET_DEFAULT)
    date_ofBooking_taxi=models.DateField()
    charge_ofTaxiRide=models.FloatField()

    class Meta:
        unique_together = (("trans_id", "trip_id"))

    def __str__(self):
        return str(self.trip_id)+' '+str(self.trans_id)
        
#Hello how are you
