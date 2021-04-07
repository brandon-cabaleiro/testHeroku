from os import path
from django import forms
from django.contrib.admin.widgets import FilteredSelectMultiple
from django.core.exceptions import ValidationError

from .models import Tag, Media, Person

from pprint import pprint

# https://gist.github.com/qylove516/d6b246980dd78e1427adc7c712571beb

class TagForm(forms.ModelForm):
    personnel = forms.ModelMultipleChoiceField(
        queryset = Person.objects.all(),
        required = False,
        widget = FilteredSelectMultiple(
            verbose_name = 'related personnel',
            is_stacked = False
        )
    )

    media = forms.ModelMultipleChoiceField(
        queryset = Media.objects.all(),
        required = False,
        widget = FilteredSelectMultiple(
            verbose_name = 'related media',
            is_stacked = False
        )
    )

    class Meta:
        model = Tag
        exclude = []

    def __init__(self, *args, **kwargs):
        super(TagForm, self).__init__(*args, **kwargs)

        if self.instance and self.instance.pk:
            self.fields['personnel'].initial = self.instance.personnel.all()
            self.fields['media'].initial = self.instance.media.all()

    def save(self, commit=True):
        tag = super(TagForm, self).save(commit=False)

        if commit:
            tag.save()

        if tag.pk:
            tag.personnel.set(self.cleaned_data['personnel'])
            tag.media.set(self.cleaned_data['media'])
            self.save_m2m()

        return tag

    def clean_name(self):
        return self.cleaned_data['name'].lower()

class MediaForm(forms.ModelForm):
    personnel = forms.ModelMultipleChoiceField(
        queryset = Person.objects.all(),
        required = False,
        widget = FilteredSelectMultiple(
            verbose_name = 'related personnel',
            is_stacked = False
        )
    )

    class Meta:
        model = Media
        exclude = []

    def __init__(self, *args, **kwargs):
        super(MediaForm, self).__init__(*args, **kwargs)

        if self.instance and self.instance.pk:
            if 'related_media' in self.fields:
                self.fields['related_media'].queryset = Media.objects.exclude(pk=self.instance.pk)
            self.fields['personnel'].initial = self.instance.personnel.all()

    def save(self, commit=True):
        if self.cleaned_data['digital_location']:
            l = path.splitext(self.cleaned_data['digital_location'])
            self.cleaned_data['file_extension'] = l[1] if len(l) == 2 else None
            self.fields = self.cleaned_data['file_extension']

        media = super(MediaForm, self).save(commit=False)

        if commit:
            media.save()

        if media.pk:
            media.personnel.set(self.cleaned_data['personnel'])
            self.save_m2m()

        return media

    def clean(self):
        cleaned_data = super().clean()

        if cleaned_data['is_physical']:
            if not cleaned_data['physical_location']:
                raise ValidationError(
                    'Physical location must be given if media is physical'
                )
        else:
            if not cleaned_data['digital_location']:
                raise ValidationError(
                    'Digital location must be given if media is not physical'
                )
