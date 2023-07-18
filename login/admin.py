from django.contrib import admin
from .models import Admin,Inmate,Charge,CO,Shift,Medical,Visitor,Cell,med_visit,Education

admin.site.register(Admin)
admin.site.register(Charge)
admin.site.register(Inmate)
admin.site.register(CO)
admin.site.register(Shift)
admin.site.register(Medical)
admin.site.register(Visitor)
admin.site.register(Cell)
admin.site.register(med_visit)
admin.site.register(Education)
