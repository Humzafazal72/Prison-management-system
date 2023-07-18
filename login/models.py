from django.db import models
from django.utils.dateparse import parse_date

class Education(models.Model):
    program_id=models.CharField(max_length=5,primary_key=True)
    name=models.CharField(max_length=40)
    def __str__(self):
        return f"{self.name}"

class Charge(models.Model):
    id=models.CharField(max_length=7,primary_key=True)
    name=models.CharField(max_length=64)
    def __str__(self) :
        return f"{self.name}"

class Shift(models.Model):
    shift_id=models.CharField(max_length=3,primary_key=True)
    starting_day=models.CharField(max_length=10,null=True)
    ending_day=models.CharField(max_length=10,null=True)
    starting_time=models.TimeField()
    ending_time=models.TimeField()
    def __str__(self) :
        return f"{self.starting_day}-{self.ending_day}: {self.starting_time} to {self.ending_time}"


class Cell(models.Model):
    cell_id=models.CharField(max_length=4,primary_key=True)
    block=models.CharField(max_length=1)
    def __str__(self):
        return f"{self.cell_id}"

class Inmate (models.Model):
    Inmate_id=models.CharField(max_length=6,primary_key=True)
    first_name=models.CharField(max_length=25)
    last_name=models.CharField(max_length=25)
    dob=models.DateField()
    arrival_date=models.DateField()
    release_date=models.DateField()
    Risk_level=models.SmallIntegerField()
    charges=models.ManyToManyField(Charge,blank=True,related_name='criminal')
    cell=models.ForeignKey(Cell,related_name='inhabitant',blank=False,on_delete=models.CASCADE,default=None)
    education=models.ForeignKey(Education,related_name='student',on_delete=models.CASCADE,blank=True,null=True)
    completed_courses=models.ManyToManyField(Education,related_name='completed',blank=True)

    def __str__(self) :
        return f"{self.Inmate_id}: {self.first_name} {self.last_name}"


class Admin(models.Model):
    admin_id=models.CharField(max_length=4,primary_key=True)
    first_name=models.CharField(max_length=25)
    last_name=models.CharField(max_length=25)
    dob=models.DateField()
    title=models.CharField(max_length=32)
    clearance_level=models.SmallIntegerField()
    contact_number=models.CharField(max_length=11)
    salary=models.BigIntegerField()
    password=models.CharField(max_length=8)
    def __str__(self) :
        return f"{self.admin_id}: {self.title}. {self.first_name} {self.last_name}"

class CO(models.Model):
    CO_id=models.CharField(max_length=4,primary_key=True)
    first_name=models.CharField(max_length=25)
    last_name=models.CharField(max_length=25)
    dob=models.DateField()
    shift=models.ForeignKey(Shift,related_name='CO',on_delete=models.CASCADE,blank=False)
    contact_number=models.CharField(max_length=11)
    salary=models.BigIntegerField()
    password=models.CharField(max_length=8)
    def __str__(self) :
        return f"{self.CO_id}: {self.first_name} {self.last_name}"

class Medical(models.Model):
    med_id=models.CharField(max_length=4,primary_key=True)
    first_name=models.CharField(max_length=25)
    last_name=models.CharField(max_length=25)
    dob=models.DateField()
    Speciality=models.CharField(max_length=32)
    shift=models.ForeignKey(Shift,related_name='medical',on_delete=models.CASCADE,blank=False)
    contact_number=models.CharField(max_length=11)
    salary=models.BigIntegerField()
    password=models.CharField(max_length=8)
    def __str__(self) :
        return f"{self.med_id}: Dr. {self.first_name} {self.last_name}"

class Visitor(models.Model):
    CNIC=models.CharField(max_length=13,primary_key=True)
    first_name=models.CharField(max_length=25)
    last_name=models.CharField(max_length=25)
    Inmate_visting=models.ForeignKey(Inmate,blank=False,on_delete=models.CASCADE)
    Visit_date=models.DateTimeField(null=True,blank=True)
    approval_status=models.BooleanField(null=True)
    relation_w_inmate=models.CharField(max_length=24)
    contact_number=models.CharField(max_length=11)
    password=models.CharField(max_length=24,null=True)
    def __str__(self):
        return f"{self.first_name} {self.last_name}"

class med_visit(models.Model):
    patient=models.ForeignKey(Inmate,on_delete=models.CASCADE,blank=False)
    doctor=models.ForeignKey(Medical,on_delete=models.CASCADE,blank=False)
    diagnosis=models.CharField(max_length=50)
    date=models.DateField(null=True)