import requests
import datetime
import time
from config import sms_market_url, sms_market_status


class ConsultaSms:

    def url_format(self, minutes_from=10, minutes_to=0):
        timezone_offset = datetime.timedelta(hours=3)
        now = datetime.datetime.now() - timezone_offset

        start_search_time = now - datetime.timedelta(minutes=minutes_from)
        end_search_time = now - datetime.timedelta(minutes=minutes_to)

        url_start_date = start_search_time.strftime("%Y-%m-%dT%H:%M:%S")
        url_end_date = end_search_time.strftime("%Y-%m-%dT%H:%M:%S")

        return sms_market_url.format(url_start_date, url_end_date)

    def consult_smsmarket(self, number, url):
        r = requests.get(url)
        print(f'URL: {url}')
        messages = r.json()
        return_filtered = []
        keys = ['number', 'sent_date', 'status', 'carrier_name']

        print(f'Messages: {messages}')

        if messages['messageCount'] == 0:
            return []
        
        for message in messages['messages']:
            if number == message['number'] or number is None:
                return_filtered.append({key: message[key] for key in keys})

        return return_filtered
        return self.filter_by(return_filtered, 'status', ['-1', '0'])

    def return_format(self, filtered_response):       

        for element in filtered_response:
            element['status'] = sms_market_status.get(element.get('status'))

            format_date = datetime.datetime.strptime(
                element['sent_date'], "%Y-%m-%d %H:%M:%S")
            format_date = format_date.strftime("%d-%m-%Y %H:%M:%S")
            element['sent_date'] = format_date

        return filtered_response

    def filter_by(self, data, field, values):
        return [e for e in data if e[field] in values]
    
    def health(self):
        url = self.url_format()
        numbers_in_error = self.consult_smsmarket(None, url)
        carriers = {}
        
        for number in numbers_in_error:
            carrier = number['carrier_name']
            carriers[carrier] = carriers.get(carrier, [])
            if self.is_expired(number['sent_date']):
                carriers[carrier].append(number['number'])
        
        print(f'Carriers: {carriers}')  
        
        
    def is_expired(self, sent_date):
        sent_date = datetime.datetime.strptime(sent_date, '%Y-%m-%d %H:%M:%S')

        timezone_offset = datetime.timedelta(hours=3)
        now = datetime.datetime.now() - timezone_offset

        minutes_offset = datetime.timedelta(minutes=2)
        expiration_time = now - minutes_offset

        return sent_date < expiration_time
            
