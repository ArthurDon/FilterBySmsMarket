from datetime import datetime


def number_status(numbers_in_error):
    carriers = {}
    for number in numbers_in_error:
        carrier = number['carrier_name']
        carriers[carrier] = carriers.get(carrier, [])
        sent_date = datetime.strptime(number['sent_date'], '%Y-%m-%d %H:%M:%S')
        if dates.is_expired(sent_date):
            carriers[carrier].append(number['number'])

    return carrier_status(carriers), 200


def carrier_status(carriers):
    carrier_status = {}
    for carrier, msisdns in carriers.items():                          
        carrier_status[carrier] = len(msisdns) > 5
        
    return carrier_status

    
