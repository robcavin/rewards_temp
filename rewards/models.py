from django.db import models

# Create your models here.
class Prize(models.Model):

    class Meta:
        permissions = (
            ("view_prize", "Can see available tasks"),
            ("change_prize", "Can change the status of tasks"),
            ("delete_prize", "Can remove a task by setting its status as closed"),
        )    
    
    title = models.CharField(max_length=80)
    subtitle = models.TextField(blank=True)
    description = models.TextField(blank=True)
    
    def __unicode__(self):
        return self.title
