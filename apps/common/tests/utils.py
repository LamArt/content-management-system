from apps.services.models import ServiceFile


def create_test_file() -> ServiceFile:
    file = ServiceFile.objects.create(
        name="Мой сертификат.pdf", path="files/2023/02/16/example.pdf"
    )
    return file
