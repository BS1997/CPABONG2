from django import template

register = template.Library()

# @register.filter
# def multiply(value, arg):
#     try:
#         return float(value) * float(arg)
#     except (ValueError, TypeError):
#         return ''

@register.filter
def percentage(value):
    try:
        return f"{float(value) * 100:.0f}%"
    except (ValueError, TypeError):
        return ''