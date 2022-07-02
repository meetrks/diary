from django.core.exceptions import FieldDoesNotExist


def is_field_exists(model, field):
    try:
        field = model._meta.get_field(field)
    except FieldDoesNotExist:
        field = None

    return bool(field)
