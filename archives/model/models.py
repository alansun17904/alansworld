from django.db import models


class PsychologyStudy(models.Model):
    BIOLOGICAL = 'BIO'
    COGNITIVE = 'COG'
    SOCIAL = 'SC'
    STUDY_CATEGORIES = [
        (BIOLOGICAL, 'Biological'),
        (COGNITIVE, 'Cognitive'),
        (SOCIAL, 'Social Cultural'),
    ]

    category = models.CharField(
        max_length=3,
        choices=STUDY_CATEGORIES,
        default=BIOLOGICAL
    )
    experimenters = models.CharField(max_length=200)
    year = models.IntegerField()
    aim = models.TextField()
    method = models.CharField(max_length=500)
    participants = models.TextField()
    procedure = models.TextField()
    results = models.TextField()
    conclusion = models.TextField()
    evaluation = models.TextField()

    def __str__(self):
        return f'{self.experimenters} ({str(self.year)})'


class PsychologyQuestion(models.Model):
    category = models.CharField(
        max_length=3, 
        choices=PsychologyStudy.STUDY_CATEGORIES,
        default=PsychologyStudy.BIOLOGICAL
    )
    question = models.CharField(max_length=300)
    valid_studies = models.ManyToManyField(PsychologyStudy)