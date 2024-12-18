from django.db import models

class QuizQuestions(models.Model):
    question_id = models.AutoField(primary_key=True)
    QuesText = models.CharField(max_length=255) 
    OptionA = models.CharField(max_length=100)   
    OptionB = models.CharField(max_length=100)   
    OptionC = models.CharField(max_length=100)   
    OptionD = models.CharField(max_length=100)  
    OptionAns = models.IntegerField()  
    class Meta:
        db_table = 'quiz_question'



