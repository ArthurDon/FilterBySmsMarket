from acesso_smsmarket import ConsultaSms
import json
import requests
from jsonschema import validate, exceptions

def consult(msisdn=None):
    consulta = ConsultaSms()

    if msisdn:
        schema = {
            "type": "string",
            "pattern": "^[0-9]{13}$"
        }

        validate(msisdn, schema=schema)

    url = consulta.url_format()
    consult_smsmarket = consulta.consult_smsmarket(msisdn, url)
    return_format = consulta.return_format(consult_smsmarket)

    return json.dumps({'response': return_format}), 200


@app.errorhandler(exceptions.ValidationError)
def validation_error(e):
    return json.dumps({"message": "Telefone informado incorretamente"}), 400