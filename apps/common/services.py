def reorder_models(model_type):
    """
    call this method from model delete and admin delete_queryset
    """
    qs = model_type.objects.order_by("ordering").all()
    for i in range(len(qs)):
        qs[i].ordering = i
        qs[i].save(update_fields=["ordering"])
