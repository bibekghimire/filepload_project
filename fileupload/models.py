
# Create your models here.
from django.db import models
import os
from django.utils import timezone
from django.core.exceptions import ObjectDoesNotExist

def upload_to(instance, filename):
    # Generate a path to store files with timestamp
    timestamp = timezone.now().strftime('%Y-%m-%d_%H-%M-%S')
    return os.path.join('uploaded_files', f'{timestamp}_{filename}')

class UploadedFile(models.Model):
    file = models.FileField(upload_to=upload_to)
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.file.name
    def delete(self, *args, **kwargs):
        # Before deleting, remove the file from storage
        try:
            if self.file:
                # Delete the file from the file system (storage)
                self.file.delete(save=False)
        except ObjectDoesNotExist:
            pass
        # Now, delete the model instance from the database
        super().delete(*args, **kwargs)