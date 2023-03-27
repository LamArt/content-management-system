from pytils.translit import slugify

from apps.seo.models import PageSEO


def create_test_page_seo():
    page_seo = PageSEO.objects.create(
        id="index",
        name="Главная",
        meta_title="Главная",
        meta_keywords="Лечение зубов Екатеринбург",
        meta_description="Стоматологическая Мастерская Елены Гончаровой - "
        "уникальная по красоте мини-клиника для решения стоматологических проблем.",
        slug=slugify("Главная"),
    )
    return page_seo
