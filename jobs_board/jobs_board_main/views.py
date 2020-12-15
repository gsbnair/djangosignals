# jobs_board_main/views.py

from django.shortcuts import render
from .models import Job, Subscriber, Subscription

from .signals import new_subscriber


def get_jobs(request):
    # get all jobs from the DB
    jobs = Job.objects.all()
    return render(request, "jobs.html", {"jobs": jobs})


def get_job(request, id):
    job = Job.objects.get(pk=id)
    return render(request, "job.html", {"job": job})


def subscribe(request, id):
    job = Job.objects.get(pk=id)
    try:
        sub = Subscriber.objects.get(email=request.POST["email"])
    except:
        sub = Subscriber(email=request.POST["email"])
        sub.save()

    # subscription = Subscription(email=request.POST["email"], user=sub, job=job)
    subscription = Subscription.objects.filter(user=sub, job=job)
    if subscription.exists():
        msg = "You have already subscribed to "
    else:
        subscription = Subscription(user=sub, job=job)
        subscription.save()
        msg = "thank you for subscribing to"

    new_subscriber.send(sender=Subscription, job=job, subscriber=sub)

    payload = {"job": job, "email": request.POST["email"], "msg": msg}
    return render(request, "subscribed.html", {"payload": payload})
