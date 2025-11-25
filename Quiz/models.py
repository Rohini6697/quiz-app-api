from django.db import models

# Create your models here.
class Quizes(models.Model):
    questions = models.CharField(max_length = 100,null = False,blank = False)
    option1 = models.CharField(max_length=50,null = False,blank = False)
    option2 = models.CharField(max_length=50,null = False,blank = False)
    option3 = models.CharField(max_length=50,null = False,blank = False)
    option4 = models.CharField(max_length=50,null = False,blank = False)
    answer = models.CharField(max_length=50,null = False,blank = False)
    
    def __str__(self):
        return f"{self.questions}"