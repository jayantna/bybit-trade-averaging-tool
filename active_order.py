import urllib.request, urllib.parse, urllib.error
import requests
import json
import hmac
import logging
import os
logger=logging.getLogger()
logger.handlers = []
logging.basicConfig(filename=f"{os.getcwd()}/rest_api.log",format='%(asctime)s - %(process)d-%(levelname)s - %(message)s', datefmt='%d-%b-%y %H:%M:%S', level=logging.DEBUG)

def timenow():
    time_url='https://api-testnet.bybit.com/v2/public/time'
    data=requests.get(time_url)
    result=data.json()
    time =str(int(round(float(result["time_now"]))-1))+"000"
    return time
#str(int(round(time.time())-1))+"000"

def get_signature(secret, param_str):
    """
    :param secret    : str, your api-secret
    :param req_params: dict, your request params
    :return: signature
    
    _val = '&'.join([str(k)+"="+str(v) for k, v in sorted(req_params.items()) if (k != 'sign') and (v is not None)])
    # print(_val)
    return str(hmac.new(bytes(secret, "utf-8"), bytes(_val, "utf-8"), digestmod="sha256").hexdigest())"""
    return str(hmac.new(bytes(secret, "utf-8"), bytes(param_str, "utf-8"), digestmod="sha256").hexdigest())


def get_active_order():
    timestamp=timenow()
    param_str = f"api_key={API_KEY}&symbol=BTCUSD&timestamp={timestamp}"
    sign=get_signature(PRIVATE_KEY ,param_str)
    data={
        "api_key":API_KEY,
        "sign":sign,
        "symbol":"BTCUSD",
        "timestamp":timestamp
        }
    logging.info('get_active_order')
    r=requests.get(url+'/open-api/order/list',data)
    logging.info(r.text)
    return json.loads(r.text)

#############################################


API_KEY="xxxxxxxxxxxxxxxxx"	
PRIVATE_KEY="xxxxxxxxxxxxxxxxxxxx"
url="https://api-testnet.bybit.com"
jsondata=json.dumps(get_active_order(),indent=4)
fh=open("activeorder.json","w")
fh.write(jsondata)
fh.close()





