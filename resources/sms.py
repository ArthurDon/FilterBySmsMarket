from flask_cf_framework.endpoint import Endpoint
from model.consult import consult

class Sms(Endpoint):
    def __init__(self, request):
        super().__init__(request)
    
    def get(self):
        print(f'Class: SMS, Method: GET => {self.parameters}')
        msisdn = self.parameters['msisdn']['value']
        return consult(msisdn)