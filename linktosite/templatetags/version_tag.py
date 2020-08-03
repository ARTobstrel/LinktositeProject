from django import template
from linktosite.models import Version


register = template.Library()


@register.simple_tag()
def get_version():
    return Version.objects.last()