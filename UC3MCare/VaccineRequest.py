"VaccineRequest"
import json
from datetime import datetime


class VaccineRequest:
    "clase VaccineRequest"
    def __init__( self, idcode, phoneNumber ):
        self.phoneNumber = phoneNumber
        self.idCode = idcode
        justnow = datetime.utcnow()
        self.timeStamp = datetime.timestamp(justnow)

    def __str__(self):
        return "VaccineRequest:" + json.dumps(self.__dict__)

    @property
    def phone( self ):
        "funcion phone"
        return self.phoneNumber
    @phone.setter
    def phone( self, value ):
        "funcion phone"
        self.phoneNumber = value

    @property
    def idDocument(self):
        "funcion DNI"
        return self.idCode
    @idDocument.setter
    def idDocument(self,value):
        "funcion DNI"
        self.idCode = value
