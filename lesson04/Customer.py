from TicketProvider import TicketProvider


class Customer(TicketProvider):
    def __init__(self):
        self.id = None
        self.name = None
        self.email = None
        self.creditcardNumber = None
        self.passportNumber = None

    def get_name(self, ):
        pass

    def set_name(self, String):
        pass

    def get_email(self, ):
        pass

    def set_email(self, String):
        pass

    def set_creditcard_number(self, ):
        pass

    def get_creditcard_number(self, int):
        pass

    def set_passport_number(self, ):
        pass

    def get_passport_number(self, int):
        pass
