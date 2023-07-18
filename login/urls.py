from django.urls import path
from . import views
urlpatterns = [
    path('admin_login/',views.admin_login,name='admin_login'),
    path('CO_login/',views.CO_login,name='CO_login'),
    path('med_login/',views.med_login,name='med_login'),
    path('visit_login/',views.visit_login,name="visit_login"),
    path('Register/',views.visit_registor,name="visit_reg"),
    path('logout_a/',views.admin_logout,name='admin_logout'),
    path('logout_c/',views.CO_logout,name='CO_logout'),
    path('logout_m/',views.med_logout,name='med_logout'),
    path('logout_v/',views.visit_logout,name='visit_logout')
]

