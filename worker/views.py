from django.shortcuts import render
from django.http import HttpResponse


def waiting_room(request,file_id):
    context = {
        'file_id': file_id
    }
    return render(request, 'worker/waiting_room.html',context)