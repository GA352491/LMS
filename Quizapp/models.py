from django.db import models
import uuid


class BaseModel(models.Model):
    uid = models.UUIDField(default=uuid.uuid4(), primary_key=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


# Create your models here.
class Categories(BaseModel):
    title = models.CharField(max_length=100)

    def __str__(self):
        return self.title


class Questions(BaseModel):
    category = models.ForeignKey(Categories, related_name='category_questions', on_delete=models.CASCADE)
    question = models.CharField(max_length=200)

    def __str__(self):
        return self.question


class Answers(BaseModel):
    question = models.ForeignKey(Questions, related_name='question_ans', on_delete=models.CASCADE)
    answer = models.CharField(max_length=100)
    is_correct = models.BooleanField(default=False)
