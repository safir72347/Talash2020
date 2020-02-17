from django.db import models

# Create your models here.
class TEAM_Register(models.Model):
    user_id = models.AutoField(primary_key=True)
    team_name = models.CharField(max_length=100)
    stu1_name = models.CharField(max_length=100)
    stu2_name = models.CharField(max_length=100)
    user_name = models.CharField(max_length=100)
    pass_word = models.CharField(max_length=100)
    conf_pass = models.CharField(max_length=100)

class TEAM_Login(models.Model):
    user_id = models.AutoField(primary_key=True)
    user_name = models.CharField(max_length=100)
    pass_word = models.CharField(max_length=100)

class clues(models.Model):
    clue_id = models.AutoField(primary_key=True)
    clue_seq = models.CharField(max_length=10)
    clue_pattern = models.CharField(max_length=10)
    clue_desc = models.CharField(max_length=100)
    clue_ans = models.CharField(max_length=10)

