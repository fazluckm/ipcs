from django.urls import path
from .import views

urlpatterns = [
    path('',views.index,name='main'),
    path('student/',views.student,name='student'),
    path('teacher/',views.teacher,name='teacher'),
    path('details/',views.details,name='details'),
    path('contact/',views.contact,name='contact'),
    path('form/',views.user_form_view,name='user_form'),
    path('success/',views.sucess_view,name='success'),
    path('contact_details/',views.contact_details),
    path('contact2/',views.contact2,name='contact2'),
    path('employform/',views.employee_form_view,name='employform'),
    path('employlist/',views.employlist,name='employlist')







]
