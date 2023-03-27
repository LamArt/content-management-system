from apps.feedback_forms.models import FeedbackForm, FeedbackFormLog, FormEmail, Field


def create_test_feedback_form() -> FeedbackForm:
    feedback_form = FeedbackForm.objects.create(
        name="Контакты",
        notification_success_template="Форма успешно отправлена",
        notification_failure_template="При отправке формы возникла ошибка",
        notification_manager_email_template="<p>Шаблон</p>",
        confirmation_email=False,
        confirmation_email_template='<p style="text-align: left;"><span style="font-size: 14pt;">Добрый ден'
        "ь!<br />Отправленная вами форма была проверена!<br /><br />Спасибо за отзыв!<br"
        " />Команда SMEG.</span></p>",
    )
    return feedback_form


def create_test_field() -> Field:
    field = Field.objects.create(
        name="Имя",
        marker_template="Введите имя",
        required_field=True,
        type="String",
    )
    return field


def create_test_form_email() -> FormEmail:
    form_email = FormEmail.objects.create(email_address="example@admin.com")
    return form_email


def create_test_feedback_form_log(feedback_form: FeedbackForm) -> FeedbackFormLog:
    feedback_form_log = FeedbackFormLog.objects.create(
        datetime="2023-02-24T10:49:38.171Z",
        ip_address="127.0.0.1",
        url="https://smeg48.ru/",
        url_source="https://smeg48.ru/",
        name="Ксения",
        phone_number="+79222933944",
        email_address="admin@example.com",
        message="Перезвоните пожалуйста, нужна консультация",
        convenient_time="11:45",
        service_name="Лечение",
        page_name="Услуги",
        feedback_form=feedback_form,
    )
    return feedback_form_log
