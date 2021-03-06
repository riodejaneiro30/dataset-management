from django.urls import path
from .views import datasetList, deleteDataset, createBooking, cancelBooking, datasetBookList

app_name = 'management'

urlpatterns = [
    path('', datasetList, name='datasetList'),
    path('delete/{i.id}', deleteDataset, name='deleteDataset'),
    path('book/create/{i.id}', createBooking, name='createBooking'),
    path('book/cancel/{i.id}', deleteDataset, name='cancelBooking'),
    path('book', datasetBookList, name='datasetBookList')
]   