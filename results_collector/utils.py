from BeautifulSoup import BeautifulSoup
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


def get_products(data, map, vendor):
    bs = BeautifulSoup(data)
    results = {}
    product_map = map.get('product')
    products = bs.findAll(product_map.get('tag'),
                          {product_map.get('attribute'): product_map.get('value')})
    for product in products:
        image = get_attr(product, map.get('image'), get_image_from_tag)
        link = get_attr(product, map.get('link'), get_link_from_tag)
        price = get_attr(product, map.get('price'), get_price_from_tag, map.get('price').get('decimals'))
        name = get_attr(product, map.get('name'), get_name_from_tag)
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
