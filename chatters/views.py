#for look ups
from django.db.models import Q

#Chatters view
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy
from django.views import generic

from .models import Chatter
from . import forms, mixins

class ChatterCreateView(LoginRequiredMixin, mixins.FormUserNeededMixin, generic.CreateView):
    #queryset = Chatter.objects.all()
    form_class = forms.ChatterModelForm
    template_name = "chatters/create_view.html"
    #success_url = "/chatter/create/"
    login_url = '/admin/'
    
    
class ChatterUpdateView(LoginRequiredMixin, mixins.UserOwnerMixin, generic.UpdateView):
    queryset = Chatter.objects.all()
    form_class = forms.ChatterModelForm
    #success_url = "/chatter/"
    template_name = "chatters/update_view.html"
    login_url = '/admin/'
    
class ChatterDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = Chatter
    template_name = 'chatters/delete_confirm.html'
    success_url = reverse_lazy('chatter:list')
    
    
    
class ChatterDetailView(generic.DetailView):
    # template_name = chatters/detail_view.html
    queryset = Chatter.objects.all()
    
    def get_object(self):
        #print(self.kwargs)
        pk = self.kwargs.get("pk") # primary key
        return Chatter.objects.get(id=pk)
        #return get_object_or_404(Chatter, id=pk)

class ChatterListView(generic.ListView):
    # template_name = chatters/list_view.html
    queryset = Chatter.objects.all()
    
    def get_queryset(self, *args, **kwargs):
        qs = Chatter.objects.all() #grab everything
        
        query = self.request.GET.get("q", None)
        if query is not None:
            qs = qs.filter(
                    Q(content__icontains=query) |
                    Q(user__username__icontains=query)
                )

        return qs
        
    #inherited function
    def get_context_data(self, *args, **kwargs): 
        # automatically creates context.
        # you can super this, and add your own.
        context = super(ChatterListView, self).get_context_data(*args, **kwargs)
        context['create_form'] = forms.ChatterModelForm
        context['create_url'] = reverse_lazy("chatter:create")
        return context
    
    
    
    
# Leaving the below as reference. Currently not used.
# Create your views here.
def chatter_detail_view(request,id=1):
    obj = Chatter.objects.get(id=id)
    context={
        "object": obj
    }
    return render(request, "chatters/detail_view.html", context)
    
def chatter_list_view(request):
    queryset = Chatter.objects.all()
    context={
        "object_list": queryset
    }
    return render(request, "chatters/list_view.html", context)
    
    