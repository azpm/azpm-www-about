from django.db import models

class JobListing(models.Model):
    title = models.CharField(max_length = "255")
    active = models.BooleanField(default = True)
    start = models.DateField()
    end = models.DateField(null = True, blank = True)
    review = models.DateField(null = True, blank = True)
    link = models.URLField(verify_exists = False)
    description = models.TextField()
    class Meta:
        verbose_name = 'Job Listing'
        verbose_name_plural = 'Job Listings'
        ordering = ['-start']