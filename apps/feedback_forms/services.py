from django.core.mail import send_mail
from django.template import Template, Context
from django.utils.html import strip_tags

from apps.feedback_forms.constants import FormConstants
from content_management_system.settings import EMAIL_HOST_USER


def send_confirmation_email(feedback_form_log):
    template = Template(feedback_form_log.feedback_form.confirmation_email_template)
    context = Context({"feedback_form_log": feedback_form_log})

    html_message = template.render(context)

    send_mail(
        subject=FormConstants.get_sender_mail_subject(feedback_form_log),
        message=strip_tags(html_message),
        from_email=EMAIL_HOST_USER,
        recipient_list=[feedback_form_log.email_address],
        html_message=html_message,
        fail_silently=False,
    )


def send_manager_email(feedback_form_log):
    template = Template(
        feedback_form_log.feedback_form.notification_manager_email_template
    )
    context = Context({"feedback_form_log": feedback_form_log})

    html_message = template.render(context)

    send_mail(
        subject=FormConstants.get_manager_mail_subject(feedback_form_log),
        message=strip_tags(html_message),
        from_email=EMAIL_HOST_USER,
        recipient_list=list(
            map(
                lambda x: x.email_address,
                feedback_form_log.feedback_form.emails.all(),
            )
        ),
        html_message=html_message,
        fail_silently=False,
    )
