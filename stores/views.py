from django.shortcuts import render, redirect
from .models import Store
from .forms import StoreModelForm

# Create your views here.
def store_list(request):
    context = {
        "stores": Store.objects.all()
    }
    return render(request, 'store_list.html', context)

def create(request):
	form = StoreModelForm()
	if request.method == "POST":
		form = StoreModelForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect('store-list')
	context = {
	"form": form,
	}
	return render(request, 'create.html', context)

def store_detail(request,store_slug):
    context = {
        "store": Klass.objects.get(slug=store_slug)
    }
    return render(request, 'detail.html', context)
