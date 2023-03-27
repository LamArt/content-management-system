import os

from django.conf import settings

import filetype


def sizify(value):
    """
    Simple kb/mb/gb size converter
    """
    # value = ing(value)
    if value < 512000:
        value = value / 1024.0
        ext = "kb"
    elif value < 4194304000:
        value = value / 1048576.0
        ext = "mb"
    else:
        value = value / 1073741824.0
        ext = "gb"
    return "%s %s" % (str(round(value, 2)), ext)


class FileSerializerMixin:
    def to_representation(self, instance):
        data = super().to_representation(instance)
        result = {field: data[field] for field in data}
        file_path = f"{settings.MEDIA_ROOT_NAME}/{instance.path}"
        if os.path.exists(file_path):
            result["extension"] = filetype.guess_extension(file_path)
            result["size"] = sizify(int(os.path.getsize(file_path)))
        return result
