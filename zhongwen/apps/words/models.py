from django.db import models

# Create your models here.
class Word(models.Model):
    en = models.CharField(max_length=20) # word in English
    es = models.CharField(max_length=20) # word in Spanish
    zw = models.CharField(max_length=20) # word in Chinese (中文)
    pinyin = models.CharField(max_length=20) # word in Pinyin
    # pronun = models.CharField(max_length=100, null=True) # url to s3 audio file

    def __str__(self) -> str:
        return f"English: {self.en} | Spanish: {self.es} | Chinese: {self.zw}"