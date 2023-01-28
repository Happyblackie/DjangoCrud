from django.urls import path
''' from .import views '''
from.views import TaskList #part D d
from.views import TaskDetail #part D e
from.views import TaskCreate #part f a
from.views import TaskUpdate #part g a
from.views import TaskDelete #part h a
from.views import RegisterPage #part L e

from.views import CustomLoginView#part i f
from django.contrib.auth.views import LogoutView# part i i

''' urlpatterns =[
    path('',views.taskList,name='tasks'),
] '''

urlpatterns =[
    path('login/', CustomLoginView.as_view(), name='login'),#part i f
    path('logout/', LogoutView.as_view(next_page='login'), name='logout'),#part i i
    path('register/', RegisterPage.as_view(),name='register'),#part L e

    path('',TaskList.as_view(),name='tasks'),
    path('task/<int:pk>/',TaskDetail.as_view(),name='task'), #part D e
    path('task-create/',TaskCreate.as_view(),name='task-create'),#part f a
    path('task-update/<int:pk>/',TaskUpdate.as_view(),name='task-update'),#part g a
    path('task-delete/<int:pk>/',TaskDelete.as_view(),name='task-delete'),#part h a
]