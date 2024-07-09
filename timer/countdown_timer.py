from datetime import datetime

class CountdownTimer:
    def __init__(self, target_date):
        self.set_target_date(target_date)
        
    def set_target_date(self, target_date):
        try:
            self.target_date = datetime.strptime(target_date, "%Y-%m-%d %H:%M:%S")
            self.valid_date = True
        except ValueError:
            self.valid_date = False
        
    def get_time_remaining(self):
        if self.valid_date:
            now = datetime.now()
            remaining = self.target_date - now
            if remaining.total_seconds() > 0:
                days, seconds = remaining.days, remaining.seconds
                hours = seconds // 3600
                minutes = (seconds % 3600) // 60
                seconds = seconds % 60
                milliseconds = remaining.microseconds // 1000
                return f"{days}d {hours}h {minutes}m {seconds}s {milliseconds}ms"
            else:
                return "Time's up!"
        else:
            return "Invalid Date"
