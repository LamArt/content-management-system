seo_fields = (
    "slug",
    "meta_title",
    "meta_keywords",
    "meta_description",
)

fieldsets = (
    (
        "SEO",
        {"fields": seo_fields},
    ),
)


def PageSEOAdminMixin(prepopulated_slug_field=None):
    class SEOTagAdminMixinClass:
        def __getattribute__(self, name):
            if name == "fieldsets":
                return object.__getattribute__(self, name) + fieldsets
            else:
                return object.__getattribute__(self, name)

        prepopulated_fields = {}

    if prepopulated_slug_field:
        SEOTagAdminMixinClass.prepopulated_fields["slug"] = (prepopulated_slug_field,)

    return SEOTagAdminMixinClass


class PageSEOSerializerMixin:
    def to_representation(self, instance):
        data = super().to_representation(instance)
        result = {field: data[field] for field in data if field not in seo_fields}
        result["seo"] = {field: data[field] for field in seo_fields}
        return result


class PageSEOViewMixin:
    lookup_field = "slug"
