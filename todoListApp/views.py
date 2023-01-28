from django.shortcuts import render,redirect

''' from django.http import HttpResponse '''

#part D c
from django.views.generic.list import ListView   #[part D c]
from .models import Task
#end of part D c

from django.views.generic.detail import DetailView #part D e
from django.views.generic.edit import CreateView #part f a
from django.urls import reverse_lazy #part f a redirects user to another page ater form is submitted

from django.views.generic.edit import UpdateView #part g a
from django.views.generic.edit import DeleteView #part h a

from django.contrib.auth.views import LoginView # part i d 
#route protection
from django.contrib.auth.mixins import LoginRequiredMixin #party j b

#registration       part L c
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.views.generic.edit import FormView







# Create your views here.
''' 
def taskList(request):
    return HttpResponse('To do list') '''


#part i e
class CustomLoginView(LoginView):
    template_name = 'todoListApp/login.html'
    fields = '__all__'
    redirect_authenticated_user = True

    def get_success_url(self):
        return reverse_lazy('tasks')
#end part i e

#part L d
class RegisterPage(FormView):
    template_name = 'todoListApp/register.html'
    form_class = UserCreationForm
    redirect_authenticated_user = True
    success_url =reverse_lazy('tasks')

    #part L f
    #user logged in automatiacally after registration
    def form_valid(self, form):
        user = form.save()
        if user is not None:
            login(self.request, user)
        return super(RegisterPage, self).form_valid(form)
    
    #part l g
    #avoiding registration page access via url after login
    def get(self, *args, **kwargs):
        if self.request.user.is_authenticated:
            return redirect('tasks')
        return super().get( *args, **kwargs)
    




#part D c        here part j b
class TaskList(LoginRequiredMixin, ListView):           
    model = Task
#end of part D c

#part D d
    context_object_name = 'tasks'
#end of part D d

    #''' part k a '''
     #making sure user sees their own data not someone elses data  
    def get_context_data(self, **kwargs):

        context = super().get_context_data(**kwargs)
        #context['color']='red' 
        context['tasks'] = context['tasks'].filter(user=self.request.user)  #''' part k b '''
        context['count'] = context['tasks'].filter(complete=False).count()  #''' part k b '''

        #part m b
        #filter search input data by title
        search_input = self.request.GET.get('search-area') or ''
        if search_input:
            context['tasks'] = context['tasks'].filter(
                title__icontains=search_input       #serch randomly
                #title__startswith=search_input      search by first words part m e
            )
        #part m c ...perisisting data in the input field
        context['search_input'] =search_input

        return context





#part D e         here part j e
class TaskDetail(LoginRequiredMixin,DetailView):
    model = Task
    context_object_name = 'task'
    template_name = 'todoListApp/task.html'
#end of part D e



''' part f a          here part j e '''
class TaskCreate(LoginRequiredMixin,CreateView):
    model = Task
    #fields = '__all__'

    #part k c
    #making sure user x sees only his details not another's
    fields = ['title','description','complete']
    #end of part k c

    success_url =reverse_lazy('tasks')

    #part k c
    #making sure user x sees only his details not another's
    def  form_valid(self,form):
        form.instance.user = self.request.user
        return super(TaskCreate, self).form_valid(form)





''' #part g a           here part j e '''
class TaskUpdate(LoginRequiredMixin,UpdateView):
    model = Task
    #fields = '__all__'

    #part k c
    #making sure user x sees only his details not another's
    fields = ['title','description','complete']
    #end of part k c

    success_url =reverse_lazy('tasks')






''' #part h a          here part j e '''
class TaskDelete(LoginRequiredMixin,DeleteView):
    model = Task
    context_object_name = 'task'
    success_url =reverse_lazy('tasks')
  