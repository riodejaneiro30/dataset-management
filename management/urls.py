from django.urls import path
from .views import datasetList, deleteDataset, createBooking, datasetBookList

app_name = 'management'

urlpatterns = [
    path('', datasetList, name='datasetList'),
    path('delete/<id>', deleteDataset, name='deleteDataset'),
    path('book/create/<id>', createBooking, name='createBooking'),
    path('book', datasetBookList, name='datasetBookList')
]   