import datetime

from django.forms import ModelForm, ValidationError
from django.shortcuts import get_object_or_404

from reservations.models import Queue, Reservation


class QueueForm(ModelForm):

    class Meta:
        model = Queue
        fields = '__all__'

    def clean(self):
        start_time = self.cleaned_data.get('start_time', None)
        end_time = self.cleaned_data.get('end_time', None)

        if start_time > end_time:
            raise ValidationError("Your queue must start before it can end")


class ReservationForm(ModelForm):

    class Meta:
        model = Reservation
        fields = ('date', 'start_time', 'end_time', )

    def __init__(self, *args, **kwargs):
        self.queue_id = kwargs.pop('pk')
        super(ReservationForm, self).__init__(*args, **kwargs)

    def clean(self):
        start_time = self.cleaned_data.get('start_time', None)
        end_time = self.cleaned_data.get('end_time', None)
        date = self.cleaned_data.get('date', None)
        pk = self.cleaned_data.get('pk', None)
        queue = get_object_or_404(Queue, pk=pk)

        if (
            start_time < end_time or
            start_time < queue.start_time or
            end_time > queue.end_time
        ):
            raise ValidationError("Valgt tid er ugyldig")

        if date >= datetime.date.today():
            raise ValidationError("You cannot make reservations back in time")
