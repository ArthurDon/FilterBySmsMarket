from request_handler import RequestHandler
from resources.sms_list import SmsList
# from resources.sms import sms

rh = RequestHandler()
#rh.add(sms, '/sms/<string:msisdn>')
rh.add(SmsList, '/sms')

def main(request):
    return rh.handle(request)
