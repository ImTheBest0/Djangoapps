from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views

app_name = 'taskapp'
urlpatterns = [
    # route is a string contains a URL pattern
    # view refers to the view function
    # name the URL
    path(route='', view=views.index, name='index'),
    path("login/",views.login,name='login'),
    path("logout/",views.logout,name='logout'),
    path("assign/",views.assign.as_view(),name="assign"),
    path("taskdetail/<int:task_id>",views.taskdetail,name="taskdetail"),
    path("taskdetailw/<int:task_id>",views.taskdetailw,name="taskdetailw"),
    path("delete/<int:task_id>",views.delete,name="delete"),
    path("confirm/<int:task_id>",views.confirm,name="confirm")
   
    
 ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
