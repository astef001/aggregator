from bs4 import BeautifulSoup
from math import pow


def get_image_from_tag(tag):
    """ This method is meant to get image tag attributes inside a html element using BS4
        :param tag - HTML element from which the methd should extract the image src
        :return Image src attribute if it exists, else None
    """
    try:
        img = tag.find('img')
        return img.attrs.get('src')
    except:
        return None


def get_link_from_tag(tag):
    """ This method is meant to get link tag attributes inside a html element using BS4
        :param tag - HTML element from which the methd should extract the link href
        :return anchor href attribute if it exists, else None
    """
    if tag:
        try:
            result = tag.attrs.get('href', None)
            if not result:
                raise AttributeError
            return result
        except AttributeError:
            tag = tag.find('a')
            if tag:
                return tag.attrs.get('href', None)
    return None


def get_attr(data, map, post_process=None, pp_extra_param=None):
    """ This method is meant to get a generic attributes inside a html element using BS4 and call another method on the
        result if it's specified
        :param data - HTML element from which the methd should extract the image src
        :param map - Dictionary containing tag attribute and attribute value used for extracting data
        :param post_process - function to call on the found element
        :param pp_extra_param - extra parameters for post_process function
        :return Found attribute in data variable
    """
    tag = data.find(map.get('tag'),
                    {map.get('attribute'): map.get('value')})
    if not post_process:
        return tag
    if pp_extra_param is not None:
        return post_process(tag, pp_extra_param)
    return post_process(tag)


def get_price_from_tag(tag, dec):
    """ This method is meant to get a price value from a string. This method is needed because sites have
    different representations for prices i.e using ',' instad of '.'
        :param tag - HTML element containing the price
        :param dec - number of price decimals
        :return Price value as integer
    """
    text = tag.text
    price = 0
    for char in text:
        if char.isdigit():
            price = price * 10 + int(char)
    return price/pow(10, dec)


def get_name_from_tag(tag):
    """This method is meant to get element inner text
        :param tag -the tag from whish we should extract the inner text
        :return Tag text if exists else None"""

    try:
        return tag.text
    except:
        return None


def get_data_map_from_object(object, prefix, extra_params=[]):
    """This method is meant to extract a map used for processing the a HTML element
        :param object - HTML object
        :param prefix - Tag prefix
        :param extra_params - extra params for witch map is needed
        :return Dictionary map for processing the HTML element"""
    result = {
        "tag": getattr(object, "%s_tag" % prefix),
        "attribute": getattr(object, "%s_attribute" % prefix),
        "value": getattr(object, "%s_value" % prefix)
    }
    for param in extra_params:
        result[param] = getattr(object, "%s_%s" % (prefix,param))
    return result


def get_products(data, location):
    """This method is meant to extract all products from a request
        :param data - response data provided by requests.get
        :param location - site witch is currently searched
        :return Dictionary containing products data"""
    bs = BeautifulSoup(data)
    results = {}
    product_map = get_data_map_from_object(location, 'product')
    products = bs.findAll(product_map.get('tag'),
                          {product_map.get('attribute'): product_map.get('value')})
    for product in products:
        image = get_attr(product, get_data_map_from_object(location, "image"), get_image_from_tag)
        print("iamge", image)
        link = get_attr(product, get_data_map_from_object(location, "link"), get_link_from_tag)
        print("link", link)
        price = get_attr(product, get_data_map_from_object(location, "price"), get_price_from_tag, location.price_decimal)
        print("price", price)
        name = get_attr(product, get_data_map_from_object(location, "name"), get_name_from_tag)
        print("name", name)
        if image and link and price and name:
            results[name] = {
                'vendor': [location.vendor_logo],
                'image': image,
                'link': [link],
                'price': [price],
                'range': range(0, 1)
            }
    return results


def update_dict(dest, source, vendor_name):
    """This method is meant to update a dictionary key if it exists or create it if it doesn't exists
        :param dest - destination dictionary
        :param source - source dictionary
        :param vendor_name - vendor name for the site which sells the product"""
    for key in source.keys():
        if key in dest.keys():
            dest[key]['vendor'].extend(vendor_name)
            dest[key]['price'].extend(source[key].get('price'))
            dest[key]['link'].extend(source[key].get('link'))
            dest[key]['range']=range(0, dest[key]['price'].length-1)
        else:
            dest[key] = source[key]
    return dest
