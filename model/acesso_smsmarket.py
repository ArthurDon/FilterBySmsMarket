import requests
import datetime
import time
from config import sms_market_url, sms_market_status


class ConsultaSms:

    def url_format(self, minutes_from=10, minutes_to=0):
        now = datetime.datetime.now()

        start_search_time = now - datetime.timedelta(minutes=minutes_from)
        end_search_time = now - datetime.timedelta(minutes=minutes_to)

        url_start_date = start_search_time.strftime("%Y-%m-%dT%H:%M:%S")
        url_end_date = end_search_time.strftime("%Y-%m-%dT%H:%M:%S")

        return sms_market_url.format(url_start_date, url_end_date)

    def consult_smsmarket(self, number, url):
        r = requests.get(url)
        messages = r.json()
        return_filtered = []
        keys = ['number', 'sent_date', 'status']
        for message in messages['messages']:
            if number == message['number'] or number is None:
                return_filtered.append({key: message[key] for key in keys})

        return self.filter_by(return_filtered, 'status', ['-1'])

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
