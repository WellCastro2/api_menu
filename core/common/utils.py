from django.utils.text import slugify
from django.core.exceptions import FieldError
 
def get_unique_slug(model_instance, slugable_field_name, slug_field_name):
    """
    Takes a model instance, sluggable field name (such as 'title') of that
    model as string, slug field name (such as 'slug') of the model as string;
    returns a unique slug as string.
    """
    slug = slugify(getattr(model_instance, slugable_field_name))
    unique_slug = slug
    ModelClass = model_instance.__class__
 
    if ModelClass._default_manager.filter(**{slug_field_name: unique_slug}).exists():
        raise FieldError(f'Unique SLUG, the slug {unique_slug} exists')
    else:
        return unique_slug

def calculate_plan_price(data):
    plan = data.get('plan')
    total = 0

    for item in data.get('item_qty').items():

        # get item price and qty in items json
        item_price = plan.items.get(item__slug=item[0])
        qty = item[1]
        unit_range = item_price.item.unit_range

        total += int(qty/unit_range) * item_price.value

    return total