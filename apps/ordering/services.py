def reorder_objects(model):
    """
    call this method from model delete and admin delete_queryset
    """
    qs = model.objects.order_by("ordering").all()
    for i in range(len(qs)):
        qs[i].ordering = i
        qs[i].save(update_fields=["ordering"])
