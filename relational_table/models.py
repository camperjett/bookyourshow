from django.db import models

class movie_detail(models.Model):
    mid          = models.PositiveIntegerField()
    mname        = models.CharField(max_length=20)
    mgenre       = models.CharField(max_length=20)
    mrating      = models.DecimalField(max_digits=2, decimal_places=1)
    budget       = models.CharField(max_length=20)
    director     = models.CharField(max_length=20)
    producer     = models.CharField(max_length=20)
    cast         = models.CharField(max_length=100)
    release_date = models.DateField()
    language     = models.CharField(max_length=20)

class theatre(models.Model):
    tid       = models.PositiveIntegerField()
    tname     = models.CharField(max_length=20)
    halls     = models.SmallIntegerField()
    taddress  = models.CharField(max_length=30)
    tphone    = models.BigIntegerField()
    trating   = models.DecimalField(max_digits=2, decimal_places=1)
    opens_at  = models.TimeField(auto_now=False, auto_now_add=False)
    closes_at = models.TimeField(auto_now=False, auto_now_add=False)

class show_detail(models.Model):
    show_id      = models.PositiveIntegerField()
    running_time = models.DurationField()
    start_time   = models.DateTimeField()
    hall_no      = models.SmallIntegerField()
    mid          = models.ForeignKey(movie_detail, on_delete=models.CASCADE)
    tid          = models.ForeignKey(theatre, on_delete=models.CASCADE)

class seat_matrix(models.Model):
    seat_id      = models.PositiveIntegerField()
    seat_row     = models.SmallIntegerField()
    seat_type    = models.SmallIntegerField()
    seat_no      = models.CharField(max_length=5)
    seat_section = models.CharField(max_length=1)
    hall_no      = models.SmallIntegerField()
    is_booked    = models.BooleanField(default=False)
    tid          = models.ForeignKey(theatre, on_delete=models.CASCADE)

class ticket_offer(models.Model):
    offer_id  = models.PositiveBigIntegerField()
    currency  = models.CharField(max_length=5)
    amount    = models.DecimalField(max_digits=10, decimal_places=2)
    seat_type = models.SmallIntegerField()
    rate      = models.SmallIntegerField()
    show_id   = models.ForeignKey(show_detail, on_delete=models.CASCADE)

class manager(models.Model):
    mgid      = models.PositiveIntegerField()
    mpassword = models.CharField(max_length=10)
    tid       = models.ForeignKey(theatre, on_delete=models.CASCADE)

class customer(models.Model):
    customer_id = models.PositiveIntegerField(null=False)
    first_name  = models.CharField(max_length=10)
    last_name   = models.CharField(max_length=10)
    gender      = models.CharField(max_length=1)
    age         = models.PositiveSmallIntegerField()
    address     = models.CharField(max_length=30)
    contact     = models.PositiveBigIntegerField()
    password    = models.CharField(max_length=20)

class booked_seat(models.Model):
    ticket_id    = models.PositiveIntegerField()
    booking_time = models.DateTimeField()
    show_id      = models.ForeignKey(show_detail, on_delete=models.CASCADE)
    seat_id      = models.ForeignKey(seat_matrix, on_delete=models.CASCADE)
    customer_id  = models.ForeignKey(customer, on_delete=models.CASCADE)
    offer_id     = models.ForeignKey(ticket_offer, on_delete=models.CASCADE)
    mgid         = models.ForeignKey(manager, on_delete=models.CASCADE)

class booking(models.Model):
    transaction_id     = models.PositiveBigIntegerField()
    transaction_status = models.CharField(max_length=10)
    booking_date       = models.DateField(auto_now=False, auto_now_add=False)
    ticket_id          = models.ForeignKey(booked_seat, on_delete=models.CASCADE)
    customer_id        = models.ForeignKey(customer, on_delete=models.CASCADE)
