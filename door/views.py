from django.shortcuts import render
from django.http import HttpResponse
from .models import DoorStatus, OpenData
from django.views.decorators.csrf import csrf_exempt
from django.utils import timezone
from website import settings
import json

# Create your views here.

@csrf_exempt
def door_post(request):
    if request.method == 'POST':
        unico = request.body.decode('utf-8')
        data = json.loads(unico)
        if 'key' in data:
            if data['key'] == settings.DOOR_KEY:
                if 'status' in data:
                    status = data['status']

                    if DoorStatus.objects.filter(name='hackerspace').count():
                        door_status_object = DoorStatus.objects.get(name='hackerspace')
                    else:
                        door_status_object = DoorStatus(name='hackerspace')
                    door_status_object.status = status
                    door_status_object.save()

                    if status == True:
                        if 'timeStart' in data and 'dateStart' in data:
                            time = data['timeStart']
                            date = data['dateStart']
                            y = date[0:4]
                            M = date[5:7]
                            d = date[8:10]
                            h = time[0:2]
                            m = time[3:5]
                            s = time[6:8]
                            door_status_object.opened.replace(hour=h, minute=m, second=s)
                            door_status_object.opened.replace(day=d, month=M, year=y)
                            door_status_object.save()
                    elif status == False:
                        if 'timeStart' in data and 'dateStart' in data and 'timeEnd' in data and 'dateEnd' in data and 'timeTotal' in data:
                            timeStart = data['timeStart']
                            dateStart = data['dateStart']
                            timeEnd = data['timeEnd']
                            dateEnd = data['dateEnd']
                            total = data['timeTotal']
                            y_s = dateStart[0:4]
                            M_s = dateStart[5:7]
                            d_s = dateStart[8:10]
                            h_s = timeStart[0:2]
                            m_s = timeStart[3:5]
                            s_s = timeStart[6:8]
                            y_e = dateEnd[0:4]
                            M_e = dateEnd[5:7]
                            d_e = dateEnd[8:10]
                            h_e = timeEnd[0:2]
                            m_e = timeEnd[3:5]
                            s_e = timeEnd[6:8]
                            openData = OpenData()
                            openData.opened.replace(hour=h_s, minute=m_s, second=s_s)
                            openData.opened.replace(day=d_s, month=M_s, year=y_s)
                            openData.closed.replace(hour=h_e, minute=m_e, second=s_e)
                            openData.closed.replace(day=d_e, month=M_e, year=y_e)
                            openData.total = total
                            openData.save()
    return HttpResponse(" ")

@csrf_exempt
def get_status(request):
    if DoorStatus.objects.filter(name='hackerspace').count():
        status = DoorStatus.objects.get(name='hackerspace').status
    else:
        status = True
    return HttpResponse(status)


def door_data(request):
    opendata_list = OpenData.objects.all()
    if DoorStatus.objects.filter(name='hackerspace').count():
        status = DoorStatus.objects.get(name='hackerspace')
    else:
        status = DoorStatus(name='hackerspace')
    context = {
        'opendata_list': opendata_list,
        'status': status,
    }

    return render(request, 'door_data.html', context)
