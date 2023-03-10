from django.db import models

# Create your models here.




class Bookings(models.Model):
    movie_name=models.CharField(max_length=50)
    Show_time=models.TimeField()
    # Date=models.DateField()
    price=models.IntegerField()
    selected_seats=models.CharField(max_length=100)
    u_name=models.CharField(max_length=30)
    
    def __str__(self):
        return str(self.u_name)


class Movies(models.Model):
    name = models.CharField(max_length=50)
    image=models.CharField(max_length=255)
    date = models.DateField()
    duration = models.CharField(max_length=50)
    type = models.CharField(max_length=50)
    language = models.CharField(max_length=50)
    rating = models.CharField(max_length=50)
    trailer = models.CharField(max_length=100)
    price = models.IntegerField(default=0)

    def __str__(self):
        return str(self.name)


class shows(models.Model):
    From_time=models.TimeField(auto_now=False, auto_now_add=False,unique=True)
    To_time=models.TimeField(auto_now=False, auto_now_add=False)
    M_id=models.ForeignKey(Movies,on_delete=models.CASCADE)
    def __str__(self):
        return (str(self.From_time)+"-"+str(self.To_time))

class Seats(models.Model):
    From_time=models.ForeignKey(shows, to_field="From_time", db_column="From_time",on_delete=models.CASCADE)
    Status1=models.CharField(max_length=10,default="Unbooked")
    Status2=models.CharField(max_length=10,default="Unbooked")
    Status3=models.CharField(max_length=10,default="Unbooked")
    Status4=models.CharField(max_length=10,default="Unbooked")
    Status5=models.CharField(max_length=10,default="Unbooked")
    Status6=models.CharField(max_length=10,default="Unbooked")
    S_no1=models.IntegerField()
    S_no2=models.IntegerField()
    S_no3=models.IntegerField()
    S_no4=models.IntegerField()
    S_no5=models.IntegerField()
    S_no6=models.IntegerField()
    def __str__(self):
        return(str(self.From_time)+","+str(self.S_no1))
