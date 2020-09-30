from request_handler import RequestHandler
from resource.sms_list import sms_list
from resource.sms import sms

rh = RequestHandler()
#rh.add(sms, '/sms/<string:msisdn>')
rh.add(sms_list, '/sms')

def main(request):
    return rh.handle(request)
