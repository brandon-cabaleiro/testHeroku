from django.db import models

class Tag(models.Model):
    name = models.CharField(max_length=100, unique=True)
    #related_person = models.ManyToManyField(Person, blank=True, related_name='personnel')
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    updated_at = models.DateTimeField(auto_now=True, editable=False)

    def __str__(self):
        return self.name

class PhysicalLocation(models.Model):
    description = models.CharField(max_length=500)
    picture = models.FileField(upload_to='uploads/locations/', null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    updated_at = models.DateTimeField(auto_now=True, editable=False)

    def __str__(self):
        return self.description

class Media(models.Model):
    class Meta:
        verbose_name_plural = 'media'
    name = models.CharField(max_length=200)
    description = models.TextField(max_length=2000, null=True, blank=True)
    date_published = models.DateField(null=True, blank=True)
    is_physical = models.BooleanField(default=False)
    physical_location = models.ForeignKey(PhysicalLocation, on_delete=models.SET_NULL, null=True, blank=True)
    digital_location = models.CharField(max_length=500, null=True, blank=True)
    file_extension = models.CharField(max_length=16, null=True, blank=True)
    tags = models.ManyToManyField(Tag, blank=True, related_name='media')
    related_media = models.ManyToManyField('self', blank=True)
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    updated_at = models.DateTimeField(auto_now=True, editable=False)

    def __str__(self):
        return self.name + ' (' + str(self.date_published) + ')'

class Person(models.Model):
    class Meta:
        verbose_name_plural = 'personnel'
    name = models.CharField(max_length=100)
    tags = models.ManyToManyField(Tag, blank=True, related_name='personnel')
    media = models.ManyToManyField(Media, blank=True, related_name='personnel')
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    updated_at = models.DateTimeField(auto_now=True, editable=False)

    def __str__(self):
        return self.name

class RecordingSession(models.Model):
    name = models.CharField(max_length=500)
    location = models.ForeignKey(PhysicalLocation, on_delete=models.SET_NULL, null=True, blank=True)
    date = models.DateTimeField()
    media = models.ManyToManyField(Media, blank=True)
    personnel = models.ManyToManyField(Person, blank=True)
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    updated_at = models.DateTimeField(auto_now=True, editable=False)

    def __str__(self):
        return self.name + ', ' + str(self.location) + '(' + str(self.date) + ')'
