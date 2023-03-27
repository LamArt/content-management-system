from apps.feedback_forms.models import FeedbackFormLog


class FormConstants:
    @staticmethod
    def get_manager_mail_subject(feedback_form_log: FeedbackFormLog):
        return f"Заявка на консультирование от {feedback_form_log.phone_number}"

    @staticmethod
    def get_sender_mail_subject(feedback_form_log: FeedbackFormLog):
        return f'Заполненная вами форма "{feedback_form_log.feedback_form.name}" была отправлена'
