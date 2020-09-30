from resource.endpoint import Endpoint
from model import consult

class SmsList(Endpoint):
    def __init__(self, request):
        super().__init__(request)
    
    def get(self):
        return consult()
    