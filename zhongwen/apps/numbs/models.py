from django.db import models

class Numb(models.Model):
    num = models.IntegerField() # number in Integer value
    zw = models.CharField(max_length=10) # number in Chinese (中文)
    pinyin = models.CharField(max_length=10) # number in Pinyin
    
    def __str__(self) -> str:
        return f"Number: {self.num} | Hanzi: {self.zw} | Pinyin: {self.pinyin}"