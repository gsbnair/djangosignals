# jobs_board_notifications/models.py.

from django.db.models.signals import pre_delete
from django.dispatch import receiver

from jobs_board_main.signals import new_subscriber
from jobs_board_main.models import Job, Subscriber, Subscription


@receiver(new_subscriber, sender=Subscription)
def handle_new_subscription(sender, **kwargs):
    subscriber = kwargs["subscriber"]
    job = kwargs["job"]

    message = """User {} has just subscribed to the Job {}.
    """.format(
        subscriber.email, job.title
    )

    print("job subscribed", message)


@receiver(pre_delete, sender=Job)
def handle_deleted_job_posting(**kwargs):
    job = kwargs["instance"]

    # Find the subscribers list
    subscriptions = Subscription.objects.filter(job=job)

    for subscription in subscriptions:
        subscriber = Subscriber.objects.get(id=subscription.user.id)
        message = """Dear {}, the job posting {} by {} has been taken down.
        """.format(
            subscriber.email, job.title, job.company
        )

        print(message)
