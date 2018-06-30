from django.shortcuts import render
from .forms import AddResearchForm
from .models import Publication

# Create your views here.

def add(request):
    if request.method == 'POST':
        p_id = request.POST.get("p_id", "")
        if(p_id):
            rec=Publication.objects.get(id=p_id)
            add=AddResearchForm(request.POST,instance=rec)
            msg="The publication has been edited successfully"
        else:
            add=AddResearchForm(request.POST)
            msg = "The publication has been added successfully"
        if(add.is_valid()):
            add.save()
        return render(request, 'add.html', {'form':add,'id':p_id,'msg':msg})
    else:
        add = AddResearchForm()
        return render(request, 'add.html', {'form': add})


def index(request):
    return render(request, 'index.html', {'pubs':Publication.objects.order_by('year_of_publication')})


def edit(request,p_id=1):
    p = Publication.objects.get(pk=p_id)
    add = AddResearchForm(instance=p)
    return render(request, 'add.html', {'form':add,'id':p_id})

def delete(request,p_id=1):
    p = Publication.objects.get(pk=p_id)
    p.delete()
    return render(request, 'index.html', {'pubs': Publication.objects.order_by('year_of_publication'),'msg':"The publication has been deleted successfully"})