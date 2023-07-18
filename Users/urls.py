from django.urls import path
from . import views

urlpatterns = [
    path('admin/',views.admin_view,name='admin_view'),
    path('CO/',views.co_view,name='CO_view'),
    path('Medical_staff/',views.medical_view,name='med_view'),
    path('Visitor/',views.visitor_view,name='visit_view'),
    path('Patient_Hist/',views.med_hist,name='med_hist'),
    path('COs_show/',views.COs_show,name='COs_show'),
    path('CO_update/<str:id>',views.CO_update,name='CO_update'),
    path('med_show/',views.med_show,name='med_show'),
    path('Patient_History/<str:id>',views.Patient_hist,name='Patient_hist'),
    path('Inmate_show/',views.inmate_show,name='inmate_show'),
    path('Delete_Inmate/<str:id>',views.Delete_inmate,name='Delete_inmate'),
    path('edit_Inmate/<str:id>',views.edit_inmate,name='edit_inmate'),
    path('visit_pending',views.visit_pending,name='visit_pending'),
    path('edit_visit/<str:id>',views.edit_visit,name='edit_visit'),
    path('visit_yes',views.visit_yes,name='visit_yes'),
    path('visit_no',views.visit_no,name='visit_no'),
]
