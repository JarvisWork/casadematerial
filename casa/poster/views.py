from django.shortcuts import render
def posters(request):
	return render(request,'posters/poster_form.html',
		{'form':None})
# Create your views here.
