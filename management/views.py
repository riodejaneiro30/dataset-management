 
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .models import Dataset, DatasetBook

# Create your views here.
response = {}

@login_required
def datasetList(request):
    dataset_list = Dataset.objects.filter(active=True)
    page = request.GET.get('page', 1)

    paginator = Paginator(dataset_list, 5)
    try:
        datasets = paginator.page(page)
    except PageNotAnInteger:
        datasets = paginator.page(1)
    except EmptyPage:
        datasets = paginator.page(paginator.num_pages)

    response['datasets'] = datasets
    html = 'management/dataset_admin.html'

    return render(request, html, response)

@login_required
def deleteDataset(request, id):
    try :
        dataset = Dataset.objects.get(id=id)
        dataset.is_active = False
    except Dataset.DoesNotExist :
        HttpResponseRedirect('/dataset')
    dataset.save()

    return HttpResponseRedirect('/dataset')

@login_required
def createBooking(request, id):
    user = request.user
    print(user)

    try :
        dataset = Dataset.objects.get(id=id)
        datasetBook = DatasetBook.create(dataset=dataset, user=user, status=1)
        dataset.is_booked = True
    except Dataset.DoesNotExist :
        HttpResponseRedirect('/dataset')
    datasetBook.save()
    dataset.save()

    return HttpResponseRedirect('/dataset')

@login_required
def datasetBookList(request):
    dataset_book_list = DatasetBook.objects.all()
    page = request.GET.get('page', 1)

    paginator = Paginator(dataset_book_list, 5)
    try:
        datasetBooks = paginator.page(page)
    except PageNotAnInteger:
        datasetBooks = paginator.page(1)
    except EmptyPage:
        datasetBooks = paginator.page(paginator.num_pages)

    response['datasetBooks'] = datasetBooks
    html = 'management/dataset_book_user.html'

    return render(request, html, response)