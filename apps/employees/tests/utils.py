from apps.employees.models import JuniorMedicalStaff, Administrator, Director


def create_test_junior_medical_staff() -> JuniorMedicalStaff:
    junior_medical_staff = JuniorMedicalStaff.objects.create(
        full_name="Ксения",
        image_photo="images/2023/02/16/example.jpg",
    )
    return junior_medical_staff


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
