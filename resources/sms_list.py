from resources.endpoint import Endpoint
from model.consult import consult

class SmsList(Endpoint):
    def __init__(self, request):
        super().__init__(request)
    
    def get(self):
        return consult()
    