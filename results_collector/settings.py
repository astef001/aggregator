import re


WHERE_TO_SEARCH=[
    {
        'name': "EMAG",
        'url': "https://www.emag.ro/search/",
        "page_nav":{
            "page_format_string":"p%s",
            "out_of_bound": 301
        },
        "no_of_pages":{
            "tag": "ul",
            "attribute": "id",
            "value": 'listing_paginator'
        }
    },
    {
        'name': "CEL",
        'url': "https://www.cel.ro/cauta/",
        "page_nav":{
            "page_format_string":"0j-%s",
            "out_of_bound": 301
        },
    },
    {
        "name": "PCGarage",
        'url': "https://www.pcgarage.ro/cauta/",
        "page_nav":{
            "page_format_string": "pagina%s",
            "out_of_bound": 404
        },

    },
]

DATA_MAP={
    "EMAG":{
        "product":{
            "tag":"div",
            "attribute":"class",
            "value":"card"
        },
        "image":{
            "tag":"a",
            "attribute":"class",
            "value":"thumbnail js-product-url"
        },
        "link":{
            "tag":"a",
            "attribute":"class",
            "value":"thumbnail js-product-url"
        },
        "price":{
            "tag":"p",
            "attribute":"class",
            "value":"product-new-price",
            "decimals": 2
        },
        "name":{
            "tag":"a",
            "attribute":"class",
            "value":"product-title js-product-url"
        }
    },
    "CEL":{
        "product":{
            "tag":"div",
            "attribute":"class",
            "value":"productListingWrapper"
        },
        "image":{
            "tag":"a",
            "attribute":"href",
            "value":re.compile("http://www.cel.ro/.*")
        },
        "link":{
            "tag":"a",
            "attribute":"href",
            "value":re.compile("http://www.cel.ro/.*")
        },
        "price":{
            "tag":"b",
            "attribute":"itemprop",
            "value":"price",
            "decimals": 0
        },
        "name":{
            "tag":"span",
            "attribute":"itemprop",
            "value":"name"
        }
    },
    "PCGarage":{
        "product": {
            "tag": "div",
            "attribute": "class",
            "value": "product-box"
        },
        "image":{
            "tag":"a",
            "attribute":"href",
            "value":re.compile("https://www.pcgarage.ro/.*")
        },
        "link":{
            "tag":"a",
            "attribute":"href",
            "value":re.compile("https://www.pcgarage.ro/.*")
        },
        "price":{
            "tag":"p",
            "attribute":"class",
            "value":"price",
            "decimals": 2
        },
        "name":{
            "tag":"div",
            "attribute":"class",
            "value":"pb-name"
        }
    }
}
