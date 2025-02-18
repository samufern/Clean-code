"VaccineManagmenteException"
class VaccineManagementException(Exception):
    "clase VaccineManagmenteException"
    def __init__(self, message):
        self.message = message
        super().__init__(self.message)

    @property
    def message(self):
        "funcion message"
        return self.message

    @message.setter
    def message(self,value):
        "funcion message setter"
        self.message = value
