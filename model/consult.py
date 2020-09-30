from model.acesso_smsmarket import ConsultaSms
import json
import requests
from jsonschema import validate

def consult(msisdn=None):
    consulta = ConsultaSms()

    if msisdn:
        schema = {
            "type": "string",
            "pattern": "^[0-9]{13}$"
        }

        try:
            validate(msisdn, schema=schema)
        except Exception as e:
            return validation_error(e)

    url = consulta.url_format()
    consult_smsmarket = consulta.consult_smsmarket(msisdn, url)
    return_format = consulta.return_format(consult_smsmarket)

    return json.dumps({'response': return_format}), 200


def validation_error(e):
    return json.dumps({"message": "Telefone informado incorretamente"}), 400