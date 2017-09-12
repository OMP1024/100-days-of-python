from django.db import models
from django.utils import timezone
import datetime

# Create your models here.
class Question(models.Model):
    # 每个字段都是一个 Field 的实例，可以在第一个参数指定一个人类可读的名字，属性的名字就是机器可读的映射到数据库中的字段
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

    # 添加自定义的方法
    def was_published_recently(self):
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.pub_date <= now

    was_published_recently.admin_order_field = 'pub_date'
    was_published_recently.boolean = True
    was_published_recently.short_description = 'Published recently?'

    # 添加 __str__方法，方便交互命令时查看更加方便
    def __str__(self):
        return self.question_text

class Choice(models.Model):
    question = models.ForeignKey(Question)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text
