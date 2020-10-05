import datetime

def is_expired(date, offset=-3, max_duration=2):        
        timezone_offset = datetime.timedelta(hours=offset)
        now = datetime.datetime.now() + timezone_offset

        minutes_offset = datetime.timedelta(minutes=max_duration)
        expiration_time = now - minutes_offset

        return date < expiration_time