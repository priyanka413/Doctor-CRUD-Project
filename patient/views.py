from django.shortcuts import render, HttpResponseRedirect
from .forms import PatientRegistration
from .models import User 
from django.views.generic.base import TemplateView, RedirectView
from django.views import View

# Create your views here.




#This CBV will add and show
class UserAddShowView(TemplateView):
	template_name = 'patient/addandshow.html'
	def get_context_data(self, *args, **kwargs):
		context = super().get_context_data(**kwargs)
		fm = PatientRegistration()
		pati = User.objects.all()
		context = {'pat':pati, 'form':fm}
		return context

	def post(self, request):
	  fm = PatientRegistration(request.POST)
	  if fm.is_valid():
	    nm = fm.cleaned_data['name']
	    em = fm.cleaned_data['email']
	    ad = fm.cleaned_data['address']
	    reg = User(name=nm, email=em, address=ad)
	    reg.save()
	    return HttpResponseRedirect('/')


#This CBV will delete
class UserDeleteView(RedirectView):
	url = '/'
	def get_redirect_url(self, *args, **kwargs):
		del_id = kwargs['id']
		User.objects.get(pk=del_id).delete()
		return super().get_redirect_url(*args, **kwargs)


#This CBV will update patients details
class UserUpdateView(View):
	def get(self, request, id):
	  pi = User.objects.get(pk=id)
	  fm = PatientRegistration(instance=pi)
	  return render(request, 'patient/updatepatient.html', {'form':fm})

	def post(self, request, id):
	  pi = User.objects.get(pk=id)
	  fm = PatientRegistration(request.POST, instance=pi)	
	  if fm.is_valid():
	   fm.save()
	  return HttpResponseRedirect('/')


