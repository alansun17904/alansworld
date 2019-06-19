from django.db import models

# Create your models here.
class Question(models.Model):
    question_text = models.CharField(max_length=500, unique=True)
    answer_text = models.CharField(max_length=20000, null=True)
    published_date = models.DateTimeField()

    def get_tags(self):
        return self.tag_set.all()

    def __str__(self):
        return self.question_text

class Tag(models.Model):
    name = models.CharField(max_length=100, unique=True)
    questions = models.ManyToManyField(Question)

    def __str__(self):
        return self.name
