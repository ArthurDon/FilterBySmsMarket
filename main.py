from flask_cf_framework.request_handler import RequestHandler
from resources.sms_list import SmsList
from resources.sms import Sms

rh = RequestHandler()
rh.add(Sms, '/sms/<string:msisdn>')
rh.add(SmsList, '/sms')

def main(request):
    return rh.handle(request)
