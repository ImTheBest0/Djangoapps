from django.urls import path

from . import views

urlpatterns = [
   path("",views.index,name="index"),
   path("<int:id>/",views.show,name="show"),
   path("delete/<int:id>/",views.delete,name="delete"),
   path("create/",views.create,name="create"),
   path("validate/<int:id>",views.validate,name="validate")
]