from apps.company_description.models import (
    Link,
    Contact,
    CompanyImage,
    StaffImage,
    CompanyDescription,
    PatientInfo,
    ConstituentDocument,
    InformedPatientConsent,
    MedicalProfessionalProvisions,
    Partner,
)


def create_test_link() -> Link:
    link = Link.objects.create(
        link_address="https://vk.com",
        link_for_messenger=False,
        link_for_social_network=True,
        logo="images/2023/02/16/example.jpg",
    )
    return link


def create_test_contact() -> Contact:
    contact = Contact.objects.create(
        address="620014, Россия, г. Екатеринбург, ул. 8 Марта, 12А, оф. 609, 6 этаж, направо",
        work_schedule="Пн-Пт: 09:00-21:00 \n Сб-Вс:10:00-18:00",
        phone_number_cell="+79221144688",
        phone_number_home="+7 (343) 356-72-68",
        email_address="admin@example.com",
        entance_diagram="images/2023/02/16/example.jpg",
        parking_place="images/2023/02/16/example.jpg",
        yandex_map="55.752571, 37.610811",
    )
    return contact


def create_test_company_image() -> CompanyImage:
    company_image = CompanyImage.objects.create(
        name="Фотография компании",
        path="images/2023/02/16/example.jpeg",
    )
    return company_image


def create_test_staff_image() -> StaffImage:
    staff_image = StaffImage.objects.create(
        name="Фотография персонала",
        path="images/2023/02/16/example.jpeg",
    )
    return staff_image


def create_test_company_description() -> CompanyDescription: # TEEEESTING!!!
    company_description = CompanyDescription.objects.create(
        client_approach_description="Качественно – это значит используются современные гибридные"
        " и на основе нано-технологий материалы, имеющие очень длительный срок эксплуатации, которые "
        "прекрасно полируются и соответствуют различным оттенкам на любой выбор и особенностям Ваших зубов. \n "
        "Красиво – это, прежде всего, гармонично Вам и Вашему представлению о красоте. Кому-то нужна "
        "эстетика, а кому-то и нет. Это дело вкуса, как восток и запад, горячее и холодное, "
        "горькое и сладкое, можно продолжать бесконечно сравнивать. Так и в красоте зуба - всё "
        "по-разному и у всех в своем роде – неповторимо. Ваша красота складывается из диалога, "
        "переговоров с доктором. \n"
        "Комфортно – это значит не только подстраиваемое под Вас расписание работы нашей клиники,  "
        "это и созданная у нас доверительная обстановка, и просторный кабинет, и оборудование, "
        "позволяющее проводить все операции безболезненно и физиологически удобно.",
        video="https://www.youtube.com/watch?v=b3ootXSAaqE",
        company_main_director_description="Качественно – это значит используются современные гибридные"
        " и на основе нано-технологий материалы, имеющие очень длительный срок эксплуатации, которые "
        "прекрасно полируются и соответствуют различным оттенкам на любой выбор и особенностям Ваших зубов. \n "
        "Красиво – это, прежде всего, гармонично Вам и Вашему представлению о красоте. Кому-то нужна "
        "эстетика, а кому-то и нет. Это дело вкуса, как восток и запад, горячее и холодное, "
        "горькое и сладкое, можно продолжать бесконечно сравнивать. Так и в красоте зуба - всё "
        "по-разному и у всех в своем роде – неповторимо. Ваша красота складывается из диалога, "
        "переговоров с доктором. \n"
        "Комфортно – это значит не только подстраиваемое под Вас расписание работы нашей клиники,  "
        "это и созданная у нас доверительная обстановка, и просторный кабинет, и оборудование, "
        "позволяющее проводить все операции безболезненно и физиологически удобно.",
        image="images/2023/02/16/example.jpeg",
        company_history="Качественно – это значит используются современные гибридные"
        " и на основе нано-технологий материалы, имеющие очень длительный срок эксплуатации, которые "
        "прекрасно полируются и соответствуют различным оттенкам на любой выбор и особенностям Ваших зубов. \n "
        "Красиво – это, прежде всего, гармонично Вам и Вашему представлению о красоте. Кому-то нужна "
        "эстетика, а кому-то и нет. Это дело вкуса, как восток и запад, горячее и холодное, "
        "горькое и сладкое, можно продолжать бесконечно сравнивать. Так и в красоте зуба - всё "
        "по-разному и у всех в своем роде – неповторимо. Ваша красота складывается из диалога, "
        "переговоров с доктором. \n"
        "Комфортно – это значит не только подстраиваемое под Вас расписание работы нашей клиники,  "
        "это и созданная у нас доверительная обстановка, и просторный кабинет, и оборудование, "
        "позволяющее проводить все операции безболезненно и физиологически удобно.",
    )
    return company_description


def create_test_patient_info() -> PatientInfo:
    patient_info = PatientInfo.objects.create(
        typical_contract="files/2023/02/16/example.pdf",
        personal_data_policy=100
        * "<h5>2. Основные понятия, используемые в&nbsp;Политике</h5>",
    )
    return patient_info


def create_test_constituent_document() -> ConstituentDocument:
    constituent_document = ConstituentDocument.objects.create(
        name="Мой сертификат.pdf", path="files/2023/02/16/example.pdf"
    )
    return constituent_document


def create_test_informed_patient_consent() -> InformedPatientConsent:
    informed_patient_consent = InformedPatientConsent.objects.create(
        name="Мой сертификат.pdf", path="files/2023/02/16/example.pdf"
    )
    return informed_patient_consent


def create_test_medical_professional_provisions() -> MedicalProfessionalProvisions:
    medical_professional_provisions = MedicalProfessionalProvisions.objects.create(
        name="Мой сертификат.pdf", path="files/2023/02/16/example.pdf"
    )
    return medical_professional_provisions


def create_test_partner() -> Partner:
    partner = Partner.objects.create(
        name="Попова Елена Владимировна",
        logo="images/2023/02/16/example.jpg",
        description="Качественно – это значит используются современные гибридные"
        " и на основе нано-технологий материалы, имеющие очень длительный срок эксплуатации, которые "
        "прекрасно полируются и соответствуют различным оттенкам на любой выбор и особенностям Ваших зубов. \n "
        "Красиво – это, прежде всего, гармонично Вам и Вашему представлению о красоте. Кому-то нужна "
        "эстетика, а кому-то и нет. Это дело вкуса, как восток и запад, горячее и холодное, "
        "горькое и сладкое, можно продолжать бесконечно сравнивать. Так и в красоте зуба - всё "
        "по-разному и у всех в своем роде – неповторимо. Ваша красота складывается из диалога, "
        "переговоров с доктором. \n"
        "Комфортно – это значит не только подстраиваемое под Вас расписание работы нашей клиники,  "
        "это и созданная у нас доверительная обстановка, и просторный кабинет, и оборудование, "
        "позволяющее проводить все операции безболезненно и физиологически удобно.",
        phone_number_cell="+79221144688",
        link_address="https://vk.com",
    )
    return partner
