from django import forms
from django.db.utils import OperationalError, ProgrammingError
from project.models import Upload, Project
from django.contrib.auth.models import User
from committees.models import Committee
from django.forms.widgets import ClearableFileInput


class SplitDateTimeFieldCustom(forms.SplitDateTimeField):
    """
        Dette er en custom SplitDateTimeField som respekterer norske datoformat
    """
    widget = forms.SplitDateTimeWidget(
            date_attrs=({
                'class': 'no-autoinit datepicker',
                }),
            date_format='%Y-%m-%d',
            time_format='%H:%M',
            )


    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs, input_date_formats=['%Y-%m-%d',], input_time_formats=['%H:%M',])


class UserFullnameChoiceField(forms.ModelChoiceField):
    """
        Denne klassen overrider ModelChoiceField for å vise vanlige
        fulle navn istedenfor brukernavn
    """
    def label_from_instance(self, obj):
        return obj.get_full_name()


class MaterialFileWidget(ClearableFileInput):
    template_name = "files/_file_widget.html"


# class UploadForm(forms.ModelForm):
#     file = forms.FileField(label="Legg ved fil", required=False, widget=MaterialFileWidget)

#     class Meta:
#         model = Upload
#         fields = ['title', 'file']


def get_committees():
    try:
        return list(Committee.objects.values_list('name', flat=True))
    except OperationalError:
        return []
    except ProgrammingError:
        return []


class ProjectForm(forms.ModelForm):

    ingress_content = forms.CharField(
        widget=forms.Textarea(attrs={'class': 'materialize-textarea'}),
        label='Ingress', help_text="En kort introduksjon til teksten"
    )

    class Meta:
        model = Project
        # fields = ['name', 'body', 'ingress_content', 'thumbnail']
        fields = ['name', 'ingress_content', 'body', 'thumbnail', 'draft']
        
        # fields = ['title', 'ingress_content', 'main_content', 'thumbnail', 'internal', 'draft']


# uploadformset = inlineformset_factory(Project, Upload,
#         form=UploadForm, extra=3)


