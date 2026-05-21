import psutil
from django.http import JsonResponse
from django.shortcuts import render


def dashboard(request):

    return render(request, 'index.html')


def system_stats(request):

    cpu_usage = psutil.cpu_percent()

    memory_usage = psutil.virtual_memory().percent

    disk_usage = psutil.disk_usage('/').percent

    network = psutil.net_io_counters()

    battery = psutil.sensors_battery()

    processes = len(psutil.pids())

    
    if battery:

        battery_percent = battery.percent

    else:

        battery_percent = "No Battery"


    data = {

        "CPU Usage": cpu_usage,

        "Memory Usage": memory_usage,

        "Disk Usage": disk_usage,

        "Bytes Sent": network.bytes_sent,

        "Bytes Received": network.bytes_recv,

        "Battery": battery_percent,

        "Running Processes": processes

    }

    return JsonResponse(data)
