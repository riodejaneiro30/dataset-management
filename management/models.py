from django.db import models
from django.contrib.auth.models import User

# Create your models here.
STATUS = ((1, 'PENDING'),(2, 'REJECTED'),(3, 'APPROVE'))

class Dataset(models.Model):
    file_url = models.URLField()
    file_name = models.CharField(max_length=50)
    active = models.BooleanField(default=True)
    is_booked = models.BooleanField(default=False)
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.file_url}'
    
class DatasetBook(models.Model):
    dataset = models.ForeignKey(Dataset, on_delete=models.CASCADE, blank=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=False)
    status = models.IntegerField(choices=STATUS)
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.dataset.file_url} - {self.user.username}'