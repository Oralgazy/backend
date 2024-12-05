from django.db import models

# Create your models here.
class UserTelegram(models.Model):
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE, null=True)
    chat_id = models.CharField(max_length=100, unique=True)
    first_name = models.CharField(max_length=100, null=True, blank=True)
    last_name = models.CharField(max_length=100, null=True, blank=True)
    username = models.CharField(max_length=100)
    language_code = models.CharField(max_length=10)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    status = models.BooleanField(default=True)
    entered_data = models.CharField(max_length=100, null=True)

    def __str__(self) -> str:
        return self.username

class Item(models.Model):
    name = models.CharField(max_length= 100)
    price = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return f'{self.name} - {self.price}'

