from model.battery.battery import Battery


class Nubbin(Battery):

    def __init__(self, last_service_date, current_date):
        self.last_service_date = last_service_date
        self.current_date = current_date

    def needs_service(self):
        compare = self.last_service_date.replace(year=self.last_service_date.year + 4)
        if compare < self.current_date:
            return True
        else:
            return False
