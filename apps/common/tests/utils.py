from apps.contacts.models import Contact


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
