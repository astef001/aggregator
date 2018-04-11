from django import template
register = template.Library()


@register.filter 
def index(List, i):
    return List[int(i)]

@register.filter
def min_price(List):
    return min(List)

@register.simple_tag
def min_vendor(prices, vendors):
    index = prices.index(min_price(prices))
    return vendors[index]

@register.filter
def list_count(list):
    return len(list)

@register.filter
def test(field):
    print(field.value())
