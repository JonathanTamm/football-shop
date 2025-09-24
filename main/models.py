import uuid
from django.db import models


from django.contrib.auth.models import User

class News(models.Model):
    CATEGORY_CHOICES = [
        ('jersey', 'Jersey'),
        ('sepatu', 'Sepatu'),
        ('bola', 'Bola'),
        ('aksesoris', 'Aksesoris'),
        ('peralatan', 'Peralatan'),
        ('koleksi', 'Koleksi'),
    ]
    
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=255)
    price = models.IntegerField(default=0)
    description = models.TextField()
    thumbnail = models.URLField(blank=True, null=True)
    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES)
    is_featured = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    news_views = models.IntegerField(default=0)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    
    def __str__(self):
        return self.name
    
    @property
    def is_news_hot(self):
        return self.news_views > 20
        
    def increment_views(self):
        self.news_views += 1
        self.save()
        
        f