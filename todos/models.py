from django.db import models
from users.models import NewUser

class Group(models.Model):
  title = models.CharField(max_length=100)
  user = models.ForeignKey(NewUser, on_delete=models.CASCADE, null=True)
  created = models.DateTimeField(auto_now_add=True)


  def __str__(self):
    return self.title

class Task(models.Model):
  title = models.CharField(max_length=100, blank=False)
  group = models.ForeignKey(Group, on_delete=models.CASCADE, null=True)
  description = models.CharField(max_length=200)
  completed = models.BooleanField(default=False)
  created = models.DateTimeField(auto_now_add=True)

  def __str__(self):
    return self.title
  
  # class Meta:
  #   ordering = ['complete']
