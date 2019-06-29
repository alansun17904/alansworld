from django.db import models

# Create your models here.
class Tag(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name


class Question(models.Model):
    question_text = models.TextField(unique=True)
    answer_text = models.TextField(blank=True, default="Still searching for an answer...")
    published_date = models.DateTimeField()
    tags = models.ManyToManyField(Tag)

    def get_tags(self):
        return self.tags.all()

    def __str__(self):
        return self.question_text

