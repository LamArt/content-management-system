from apps.employees.models import JuniorStaff, Administrator, Director


def create_test_junior_staff() -> JuniorStaff:
    junior_staff = JuniorStaff.objects.create(
        full_name="Ксения",
        image_photo="images/2023/02/16/example.jpg",
    )
    return junior_staff


def create_test_administrator() -> Administrator:
    administrator = Administrator.objects.create(
        full_name="Ксения",
        image_photo="images/2023/02/16/example.jpg",
    )
    return administrator


def create_test_director() -> Director:
    director = Director.objects.create(
        full_name="Ксения",
        image_photo="images/2023/02/16/example.jpg",
    )
    return director
