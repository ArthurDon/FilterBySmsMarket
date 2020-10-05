from flask_cf_framework.request_handler import RequestHandler
from resources.sms_list import SmsList
from resources.sms import Sms
from resources.health import Health

rh = RequestHandler()
rh.add(Sms, '/sms/<string:msisdn>')
rh.add(SmsList, '/sms')
rh.add(Health, '/health')

def main(request):
    
    response, code = rh.handle(request)
    print(f'\n\n {response}{code}')
    
    return response


class Request:
    def __init__(self):
        self.method = 'GET'
        self.path = '/health'
        self.headers = '<>HEADERS</>'
        self.body = '<>BODY</>'
        self.args = 'Test Parameters'

    def get_json(self, silent=False):
        return self.body

request = Request()
main(request)
