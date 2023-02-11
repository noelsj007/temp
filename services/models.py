from django.db import models



class Services(models.Model):
    ACTIVE = 'active'
    DELETEED = 'deleted'

    STATUS_CHOICES = (
        (ACTIVE, 'active'),
        (DELETEED,  'deleted')
    )
    title = models.CharField(max_length=50)
    description = models.TextField(max_length=200)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default=ACTIVE)
    image = models.ImageField(upload_to='media/uploads/service_image/', blank=True)
    video = models.FileField(upload_to='media/uploads/service_video/', blank=True)
    price = models.IntegerField()
    service_provider = models.ForeignKey('ServiceProvider', related_name='service_provider', on_delete=models.CASCADE)
    
    def __str__(self):
        return self.title
        
class ServiceProvider(models.Model):
    service_provider_id = models.IntegerField(null=True)
    service_provider_name = models.CharField(max_length=50)
    sp_image = models.ImageField(upload_to='media/uploads/service_provider_image/', blank=True)
    contact = models.TextField(max_length=200)
    star = models.IntegerField(null=True)

    def __str__(self):
        return self.service_provider_name
