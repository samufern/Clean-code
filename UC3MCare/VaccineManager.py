"Docstring"

import json
import re
from UC3MCare.VaccineMangementException import VaccineManagementException
from UC3MCare.VaccineRequest import VaccineRequest


class VaccineManager:
    "clase vaccine manager"
    def __init__(self):
        pass

    @staticmethod
    def VALIDATE_GUID(guid):
        "metodo de validacion del GUID"
        r = re.compile(r'^[0-9A-F]{8}-[0-9A-F]{4}-4[0-9A-F]{3}-[89AB][0-9A-F]{3}-'
                                 r'[0-9A-F]{12}$',re.IGNORECASE)

        res = r.search(guid)
        if res is None:
            return False
        return True

    def READ_ACCESS_REQUIEST_FROM_JSON(self, fileTo):
        "funcion de lectura del acceso del json"
        try:
            with open(fileTo, "w", encoding="utf8") as f:
                DATA = json.load(f)
        except FileNotFoundError as e:
            raise VaccineManagementException("Wrong file or file path") from e
        except json.JSONDecodeError as e:
            raise VaccineManagementException("JSON Decode Error - Wrong JSON Format") from e


        try:
            guid = DATA["id"]
            Zip = DATA["phoneNumber"]
            req = VaccineRequest(guid, Zip)
        except KeyError as e:
            raise VaccineManagementException("JSON Decode Error - Invalid JSON Key") from e
        if not self.VALIDATE_GUID(guid):
            raise VaccineManagementException("Invalid GUID")

        # Close the file
        return req
