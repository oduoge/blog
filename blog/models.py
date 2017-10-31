from django.db import models

# Create your models here.

class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)


class user(models.Model):
    user_id = models.IntegerField()
    username = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    telephone = models.CharField(max_length=20)
    last_login_ip = models.CharField(max_length=23)
    last_login_date = models.DateTimeField('last login time')
    credit_score = models.IntegerField(default=0)

    def __str__(self):
        return self.username + ': ' + self.credit_score

    class Meta:
        app_label = 'db_blog'
        ordering = ['last_login_date']

    @staticmethod
    def tran(string=None):
        if string is not None:
            newuser = user()
            newuser.user_id = string[0]
            newuser.username = string[1]
            newuser.password = string[2]
            newuser.email = string[3]
            newuser.telephone = string[4]
            newuser.last_login_ip = string[5]
            newuser.last_login_date = string[6]
            newuser.credit_score = string[7]
            return newuser
        else:
            return None