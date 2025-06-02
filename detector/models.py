from django.db import models

class NewsArticle(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    source_url = models.URLField()
    is_verified = models.BooleanField(default=False)
    credibility_score = models.FloatField(default=0.0)  # Add this field
    verification_result = models.CharField(max_length=100, blank=True)
    submitted_at = models.DateTimeField(auto_now_add=True)
    keywords = models.TextField(blank=True)
    source_reliability = models.CharField(max_length=50, blank=True)

    def __str__(self):
        return self.title