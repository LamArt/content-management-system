from pytils.translit import slugify

from apps.employees.models import Employee
from apps.portfolios.models import Portfolio
from apps.services.models import Service, ServiceCategory


def create_test_portfolio() -> Portfolio:
    portfolio = Portfolio.objects.create(
        task_description="Объясняя клиенту различные методы протезирования (виниры, коронки) иллюстрируйте рассказ "
        "фотографиями своих бывших пациентов. Желательно, чтобы снимки были сделаны «до» и «после» "
        "проведения реставрации. Постарайтесь сделать описание более эмоциональным и подробным, "
        "тогда будет понятно, что Вы действительно помогли всем этим людям обрести уверенность в "
        "себе посредством возможности широко улыбаться миру.",
        problem_solve="Лечение и профилактика аномалий прикуса характеризуется большой длительностью и сложностью, "
        "поэтому рекомендуется сделать не две, как в предыдущем случае, а три фотографии: \n до лечения "
        "(неправильный прикус);\n в процессе (установленные брекет-системы);\n после лечения ("
        "полученный результат).\n Таким образом, Вы поможете пациенту увидеть все этапы "
        "ортодонтического лечения и оценить эстетичность"
        "проводимых процедур. Добавляя в портфолио фотографию «в процессе лечения» можно избавиться от "
        "долгих объяснений на пальцах о внешнем виде предлагаемой конструкции. Используя фото вы легко "
        "сможете продемонстрировать варианты установки (лингвальные или вестибулярные) и то, "
        "как реально выглядят разные типы брекетных систем в процессе носки.",
        patient_result="Приняв решение составить собственное портфолио нужно помнить, что в альбоме представлены "
        "услуги, которые Вы оказываете пациентам, поэтому снимки в нем должны быть четкими и "
        "качественными, а сам он выглядел солидно и респектабельно. Мутные фотографии сложных "
        "клинических случаев не добавят Вам доверия пациента, поэтому не стоит их показывать, "
        "хотя они и в самом деле способны подтвердить Вашу высокую квалификацию. \n Для того, "
        "чтобы получить качественные снимки Вам придется помучить пациента, выбирая наилучший ракурс (не"
        "забудьте получить письменное разрешение на их использование!). Но где же разместить удачные "
        "фотографии? Рекомендуем воспользоваться альбомом с толстыми листами, что-то типа «свадебной "
        "книги». Подобрать подходящий вариант довольно просто: или в магазинах, занимающихся продажей "
        "фото принадлежностей, или сделав заказ в специализированном интернет-магазине, причем покупку "
        "доставят прямо в клинику.\n Готовый альбом с фотографиями работ, расположенных для лучшего "
        "поиска по категориям, лучше всего оставить в холе Вашей стоматологической клиники. Там, "
        "в непринужденной обстановке, пациенты смогут не торопясь посмотреть какое лечение они "
        "получат, обратившись непосредственно к Вам. Правильно составленный альбом поможет создать "
        "репутацию преуспевающего стоматолога.",
        image_avatar="images/2023/02/16/example.jpg",
        video="https://www.youtube.com/watch?v=b3ootXSAaqE",
        completion_date_result="Все работы выполнили за 6 месяцев!",
        slug=slugify("1"),
    )
    return portfolio


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


def create_test_service(service_category: ServiceCategory, index: int) -> Service:
    service = Service.objects.create(
        name=f"Лечение №{index}",
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
        slug=slugify(f"Лечение №{index}"),
    )
    return service


def create_test_doctor(index) -> Employee:
    doctor = Employee.objects.create(
        full_name=f"Попова Елена Владимировна №{index}",
        image_photo="images/2023/02/16/example.jpg",
        image_patient_photo="images/2023/02/16/example.jpg",
        video="https://www.youtube.com/watch?v=b3ootXSAaqE",
        specialization="Главный врач, врач ортопед, гнатолог, терапевт",
        skills="Ортопед, гнатолог, терапевт",
        start_year=2000,
        slug=f"Попова Елена Владимировна №{index}",
    )
    return doctor
