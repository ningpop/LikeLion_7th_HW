from django.shortcuts import render
import time

# Create your views here.

def nowclock(request):
    now = time.localtime()

    date = {0:"월", 1:"화", 2:"수", 3:"목", 4:"금", 5:"토", 6:"일"}

    return render(request, "now_clock.html", {
        "year" : now.tm_year,
        "month" : now.tm_mon,
        "day" : now.tm_mday,
        "hour" : now.tm_hour,
        "min" : now.tm_min,
        "sec" : now.tm_sec,
        "date" : date[now.tm_wday],
    })