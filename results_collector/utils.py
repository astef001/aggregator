from bs4 import BeautifulSoup
from math import pow


def get_image_from_tag(tag):
    img = tag.find('img')
    for attr in img.attrs:
        if attr[0] == 'src':
            return attr[1]


def get_link_from_tag(tag):
    for attr in tag.attrs:
        if attr[0] == 'href':
            return attr[1]


def get_attr(data, map, post_process=None, pp_extra_param=None):
    tag = data.find(map.get('tag'),
                    {map.get('attribute'): map.get('value')})
    if not post_process:
        return tag
    if pp_extra_param is not None:
        return post_process(tag, pp_extra_param)
    return post_process(tag)


def get_price_from_tag(tag, dec):
    text = tag.text
    price = 0
    for char in text:
        if char.isdigit():
            price = price * 10 + int(char)
    return price/pow(10, dec)


def get_name_from_tag(tag):
    return tag.text


def get_data_map_from_object(object, prefix, extra_params=[]):
    result = {
        "tag": getattr(object, "%s_tag" % prefix),
        "attribute": getattr(object, "%s_attribute" % prefix),
        "value": getattr(object, "%s_value" % prefix)
    }
    for param in extra_params:
        result[param] = getattr(object, "%s_%s" % (prefix,param))
    return result


def get_products(data, location, vendor):
    bs = BeautifulSoup(data)
    results = {}
    product_map = get_data_map_from_object(location, 'product')
    products = bs.findAll(product_map.get('tag'),
                          {product_map.get('attribute'): product_map.get('value')})
    for product in products:
        image = get_attr(product, get_data_map_from_object(location,"image"), get_image_from_tag)
        link = get_attr(product, get_data_map_from_object(location,"link"), get_link_from_tag)
        price = get_attr(product, get_data_map_from_object(location,"price"), get_price_from_tag, location.price_decimal)
        name = get_attr(product, get_data_map_from_object(location,"name"), get_name_from_tag)
        results[name]={
            'vendor': [vendor],
            'image': image,
            'link': [link],
            'price': [price]
        }
    return results;


def update_dict(dest, source, vendor_name):
    for key in source.keys():
        if key in dest.keys():
            dest[key]['vendor'].extend(vendor_name)
            dest[key]['price'].extend(source[key].get('price'))
            dest[key]['link'].extend(source[key].get('link'))
        else:
            dest[key]=source[key]
    return dest;
