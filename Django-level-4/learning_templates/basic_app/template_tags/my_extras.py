from django import template 

register = template.Library()


# You can register you filter using decorators as well
@register.filter(name = 'cut')
def cut(value,arg):
    """
        This cuts out all values of 
        "args" from the string 

    """
    return value.replace(arg,"")


# You can register you filters like this also
# register.filter('cut', cut)

