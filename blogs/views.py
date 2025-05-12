from django.shortcuts import render, redirect
from .models import Overall, Explain, Explain2, Individaul
from .forms import OverallForm, ExplainForm
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.http import Http404




# Create your views here.
def index(request):
    return render(request, 'blogs/index.html')

@login_required
def overall(request):
    overall = Overall.objects.filter(owner=request.user).order_by('date_added')
    context = {'overall': overall}
    return render(request, 'blogs/overall.html', context)
    

@login_required
def overal(request, overal_id):
    overal = Overall.objects.get(id=overal_id)
    if overal.owner != request.user:
        raise Http404
    
    explains = overal.explain_set.order_by('-date_added')
    context = {'overal': overal, 'explains': explains}
    return render(request, 'blogs/overal.html', context)


@login_required
def new_overall(request):
    
    if request.method != 'POST':
        form = OverallForm()
    else:
        form = OverallForm(data=request.POST)
        if form.is_valid():
            new_overall = form.save(commit=False)
            new_overall.owner = request.user
            new_overall.save()
            return redirect('blogs:overall')
        
    context = {'form': form}
    return render(request,'blogs/new_overall.html', context)


@login_required
def new_explain(request, overal_id):
    overal = Overall.objects.get(id=overal_id)
    if overal.owner != request.user:
        raise Http404
    
    if request.method != 'POST':
        form = ExplainForm()
    else:
        form = ExplainForm(data=request.POST)
        if form.is_valid():
            new_explain = form.save(commit=False)
            new_explain.owner = request.user
            new_explain.overal = overal
            new_explain.overl_id = overal_id
            new_explain.esm = overal
            new_explain.save()
            return redirect('blogs:overal', overal_id=overal_id)
        
    context = {'overal': overal,'form': form }
    return render(request, 'blogs/new_explain.html', context)


@login_required
def edit_overall(request, overall_id):
    overall = Explain.objects.get(id=overall_id)
    overal = overall.esm
    if overal.owner != request.user:
        raise Http404

    if request.method != 'POST':
        form = ExplainForm(instance=overall)
    else:
        form = ExplainForm(instance=overall, data=request.POST)
    if form.is_valid():
        form.save()
        return redirect('blogs:overal', overal_id=overal.id)
    
    context = {'overall': overall, 'form': form, 'overal': overal}
    return render(request, 'blogs/edit_overall.html', context)


