from django.urls import path
from myapp import views
urlpatterns =[
    path('',views.index),
    path('about',views.about),
    path('form/',views.form, name='form'),
    path('edit/<int:person_id>/',views.edit, name='edit'),
    path('delete/<int:person_id>/',views.delete, name='delete'),
    path('api/add-department/', views.add_department_api, name='add_department_api')
]