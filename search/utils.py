from search.models import Courier, CourierParams
from bs4 import BeautifulSoup
import requests
import re
import json
from search.models import CourierParams

def get_package_status(awb):
    couriers = Courier.objects.all()
    for courier in couriers:
        result = scrap_courier(courier, awb)
        if result:
            return result
    return None

def scrap_courier(courier, awb):
    params = CourierParams.objects.filter(courier_id=courier).all()
    data = {}
    for row in params:
        if 'awb' in row.param_label:
            data.update({row.param_label: awb})
        else:
            data.update({row.param_label: row.param_value})
    result = requests.post(courier.url, data)
    if courier.is_json:
        content = re.search("{.*}", result.content).group(0)
        content = json.loads(content)
        result_tag = int(courier.result_tag)
        status = []
        for entry in content.values():
            try:
                for step in range(0,result_tag+1):
                    status.append(entry.get(str(step)))
            except AttributeError:
                pass
        if [s for s in status if s is not None]:
            result=[]
            for step in status:
                result.append("{} {}".format(step.get('mstex'), step.get('dstex')))
            return result
    else:
        bs = BeautifulSoup(result.content)
        elem = bs.find(courier.result_tag, {courier.result_attribute: courier.result_value})
        return elem.text

    return ["Statusul expeditiei nu a putut fi verificat"]
#2129810250193
