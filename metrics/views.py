from django.shortcuts import render, render_to_response
from django.core import serializers
from metrics.models import Metrics
from django.http import JsonResponse, HttpResponse
from django.core import serializers
from datetime import datetime, timedelta
import json

def metricsSerializer(queryset):
    output = []
    for metric in list(queryset):
        output.append({
            "temperature": metric.temperature,
            "humidity": metric.humidity,
            "pressure": metric.pressure,
            "timestamp": metric.timestamp.strftime('%Y-%m-%dT%H:%M:%S')
        })

    return json.dumps(output)

def Index(request):
    objects = Metrics.objects.all()
    last = list(objects)[-1]
    latest = {
        "temperature": round((float(last.temperature) * 1.8) + 32, 2),
        "humidity": round(float(last.humidity), 2),
        "pressure": round(float(last.pressure), 2)
    }

    metrics = { "data": objects, "latest": latest, "json": metricsSerializer(objects) }
    return render_to_response('metrics/index.html', metrics)

def API(request):
    if request.GET.get('from'):
        metrics = Metrics.objects.filter(timestamp__lte=duration)
    else:
        metrics = Metrics.objects.all()

    metrics_serial = metricsSerializer(metrics)
    return HttpResponse(metrics_serial)

def Register(request):
    from sense_hat import SenseHat
    sense = SenseHat()
    context = {
        "humidity": sense.get_humidity(),
        "temperature": sense.get_temperature(),
        "pressure": sense.get_pressure()
    }

    metric = Metrics(**context)
    metric.save()

    return JsonResponse(context)

def Clean(request):
    hours = request.GET.get('duration') or 1
    duration = datetime.now()-timedelta(hours=hours)
    metrics = Metrics.objects.filter(timestamp__lte=duration).delete()

    return HttpResponse("True")
