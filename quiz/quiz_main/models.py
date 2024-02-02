from django.db import models

# Create your models here.
class Leaderboard_scores(models.Model):
    username = models.CharField(max_length=255, null=True)
    user_score = models.IntegerField(null=True)

    def __str__(self) -> str:
        return f'{self.username}, score: {self.user_score}'