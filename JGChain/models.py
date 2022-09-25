from django.db import models

# Create your models here.
class Block(models.Model):
    id = models.AutoField(primary_key=True)
    current_hash = models.CharField(max_length=64, null=False, blank=False)
    previous_hash = models.CharField(max_length=64, null=False, blank=False)
    timestamp = models.DateTimeField(auto_now_add=True)
    data = models.TextField(blank=True, null=True)
    nonce = models.IntegerField(default=0)
    difficulty = models.IntegerField(default=0)


class JGChain(models.Model):
    id = models.AutoField(primary_key=True)
    blocks = models.ManyToManyField(Block)

