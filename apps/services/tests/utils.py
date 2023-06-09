from pytils.translit import slugify

from apps.services.models import (
    ServiceFile,
    ServicePatientNeedsCategory,
    ServiceCategory,
    Service,
)
from apps.employees.models import Employee


def create_test_service_category() -> ServiceCategory:
    service_category = ServiceCategory.objects.create(
        name="Лечение",
        logo="images/2023/02/16/example.jpg",
        short_description="Сегодня лечится всё — простые маленькие кариозные полости и самые сложные "
        "гнойно-воспалительные процессы. В нашей клинике при четкой диагностике, сборе анамнеза, "
        "обследования и выставления окончательно диагноза лечение у всех разное, "
        "так как индивидуальное.",
        long_description="Качественно – это значит используются современные гибридные и на основе нано-технологий "
        "материалы, имеющие очень длительный срок эксплуатации, которые прекрасно полируются и "
        "соответствуют различным оттенкам на любой выбор и особенностям Ваших зубов. \n "
        "Красиво – это, прежде всего, гармонично Вам и Вашему представлению о красоте. Кому-то нужна "
        "эстетика, а кому-то и нет. Это дело вкуса, как восток и запад, горячее и холодное, "
        "горькое и сладкое, можно продолжать бесконечно сравнивать. Так и в красоте зуба - всё "
        "по-разному и у всех в своем роде – неповторимо. Ваша красота складывается из диалога, "
        "переговоров с доктором. \n"
        "Комфортно – это значит не только подстраиваемое под Вас расписание работы нашей клиники,  "
        "это и созданная у нас доверительная обстановка, и просторный кабинет, и оборудование, "
        "позволяющее проводить все операции безболезненно и физиологически удобно.",
    )
    return service_category


def create_test_service(service_category: ServiceCategory) -> Service:
    service = Service.objects.create(
        name="Лечение",
        code="А16.07.020.001, \n А22.07.002",
        title="Лечение зубов",
        image="images/2023/02/16/example.jpg",
        price=500,
        published=True,
        price_published=True,
        short_description="Сегодня лечится всё — простые маленькие кариозные полости и самые сложные "
        "гнойно-воспалительные процессы. В нашей клинике при четкой диагностике, сборе анамнеза, "
        "обследования и выставления окончательно диагноза лечение у всех разное, "
        "так как индивидуальное.",
        long_description="Качественно – это значит используются современные гибридные и на основе нано-технологий "
        "материалы, имеющие очень длительный срок эксплуатации, которые прекрасно полируются и "
        "соответствуют различным оттенкам на любой выбор и особенностям Ваших зубов. \n "
        "Красиво – это, прежде всего, гармонично Вам и Вашему представлению о красоте. Кому-то нужна "
        "эстетика, а кому-то и нет. Это дело вкуса, как восток и запад, горячее и холодное, "
        "горькое и сладкое, можно продолжать бесконечно сравнивать. Так и в красоте зуба - всё "
        "по-разному и у всех в своем роде – неповторимо. Ваша красота складывается из диалога, "
        "переговоров с доктором. \n"
        "Комфортно – это значит не только подстраиваемое под Вас расписание работы нашей клиники,  "
        "это и созданная у нас доверительная обстановка, и просторный кабинет, и оборудование, "
        "позволяющее проводить все операции безболезненно и физиологически удобно.",
        video="https://www.youtube.com/watch?v=b3ootXSAaqE",
        service_category=service_category,
        slug=slugify("Лечение"),
    )
    return service


def create_test_service_patient_needs_category() -> ServicePatientNeedsCategory:
    service_patient_needs_category = ServicePatientNeedsCategory.objects.create(
        name="Боль в зубах",
        logo="images/2023/02/16/example.jpg",
        short_description="Сегодня лечится всё — простые маленькие кариозные полости и самые сложные "
        "гнойно-воспалительные процессы. В нашей клинике при четкой диагностике, сборе анамнеза, "
        "обследования и выставления окончательно диагноза лечение у всех разное, "
        "так как индивидуальное.",
        long_description="Качественно – это значит используются современные гибридные и на основе нано-технологий "
        "материалы, имеющие очень длительный срок эксплуатации, которые прекрасно полируются и "
        "соответствуют различным оттенкам на любой выбор и особенностям Ваших зубов. \n "
        "Красиво – это, прежде всего, гармонично Вам и Вашему представлению о красоте. Кому-то нужна "
        "эстетика, а кому-то и нет. Это дело вкуса, как восток и запад, горячее и холодное, "
        "горькое и сладкое, можно продолжать бесконечно сравнивать. Так и в красоте зуба - всё "
        "по-разному и у всех в своем роде – неповторимо. Ваша красота складывается из диалога, "
        "переговоров с доктором. \n"
        "Комфортно – это значит не только подстраиваемое под Вас расписание работы нашей клиники,  "
        "это и созданная у нас доверительная обстановка, и просторный кабинет, и оборудование, "
        "позволяющее проводить все операции безболезненно и физиологически удобно.",
    )
    return service_patient_needs_category


def create_test_service_file() -> ServiceFile:
    service_file = ServiceFile.objects.create(
        name="Мой сертификат.pdf", path="files/2023/02/16/example.pdf"
    )
    return service_file


def create_test_employee(index: int = 1) -> Employee:
    doctor = Employee.objects.create(
        full_name=f"Попова Елена Владимировна №{index}",
        image_photo="images/2023/02/16/example.jpg",
        image_client_photo="images/2023/02/16/example.jpg",
        video="https://www.youtube.com/watch?v=b3ootXSAaqE",
        specialization="Главный врач, врач ортопед, гнатолог, терапевт",
        skills="Ортопед, гнатолог, терапевт",
        start_year=2000,
        slug=slugify(f"Попова Елена Владимировна №{index}"),
    )
    return doctor
