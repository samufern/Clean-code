"""Module """
import json
import re
from datetime import datetime

from uc3m_care.exception.vaccine_management_exception import VaccineManagementException
from uc3m_care.cfg.vaccine_manager_config import JSON_FILES_PATH
# pylint: disable=consider-using-enumerate
class FPMethods:
    """Class for store methods"""

    class FPMethods:
        """Class for store methods"""
        def __init__(self):
            pass
        PATIENT_ALREADY_VACCINATED_EXCEPTION = "Patient already vaccinated"
        APPOINTMENT_TIME_EXCEPTION = "Appointment Time has passed"
        DATE_DOES_NOT_EXIST_EXCEPTION = "Date does not exist"
        DATE_WAS_ALREADY_CANCELLED_EXCEPTION = "Date was already cancelled"
        DATE_SIGNATURE_NOT_VALID_EXCEPTION = "Date Signature not valid"
        DICT_TOO_LONG_EXCEPTION = "Dict too long"
        REASON_NOT_OK_EXCEPTION = "Reason Not OK"
        CANCEL_TYPE_NOT_VALID_EXCEPTION = "Cancel Type not valid"
        KEYERROR_EXCEPTION = "KeyError exception"
        JSONDECODE_EXCEPTION = "JsonDecode Exception"

        @classmethod
        def store_list_date(cls, date, store_path):
            """Method store_list_date from vaccine_manager"""
            with open(store_path, "r", encoding="utf-8", newline="") as file2:
                store_list = json.load(file2)
                for i in range(len(store_list)):
                    store_list[i]["_VaccinationAppointment__appointment_date"] = date
            return store_list

        @classmethod
        def convert_to_json(cls, store_path, to_dump):
            """Method convert_to_json from vaccine_manager"""
            with open(store_path, "w", encoding="utf-8", newline="") as file3:
                json.dump(to_dump, file3, indent=2)

        def read_store_vaccine(self, date_sig, store_vaccine):
            """Method read_store_vaccine from vaccine_manager"""
            with open(store_vaccine, "r", encoding="utf-8", newline="") as file0:
                vaccine_list = json.load(file0)
                for i in range(len(vaccine_list)):
                    if vaccine_list[i]["_VaccinationLog__date_signature"] == date_sig:
                        raise VaccineManagementException(self.PATIENT_ALREADY_VACCINATED_EXCEPTION)

        def check_appointment_time(self):
            """Method check_appointment_time from vaccine_manager"""
            store_date = JSON_FILES_PATH + "store_date.json"
            with open(store_date, "r", encoding="utf-8", newline="") as file1:
                store_list = json.load(file1)
                for i in range(len(store_list)):
                    utc_appointment_date = store_list[i]\
                                           ["_VaccinationAppointment__appointment_date"]
                    if utc_appointment_date < str(datetime.now()):
                        raise VaccineManagementException(self.APPOINTMENT_TIME_EXCEPTION)

        def check_if_date_exists(self, date_sig, store_date):
            """Method check_if_date_exists from vaccine_manager"""
            with open(store_date, "r", encoding="utf-8", newline="") as file1:
                store_list = json.load(file1)
                for i in range(len(store_list)):
                    if store_list[i]["_VaccinationAppointment__date_signature"] != date_sig:
                        raise VaccineManagementException(self.DATE_DOES_NOT_EXIST_EXCEPTION)

        def check_if_date_was_cancelled(self, cancelled_store, date_sig):
            """Method check_if_date_was_cancelled from vaccine_manager"""
            try:
                with open(cancelled_store, "r", encoding="utf-8", newline="") as file2:
                    try:
                        cancel_list = json.load(file2)
                        for i in range(len(cancel_list)):
                            if cancel_list[i]\
                                    ["date_signature"] == date_sig:
                                raise VaccineManagementException\
                                      (self.DATE_WAS_ALREADY_CANCELLED_EXCEPTION)
                    except json.decoder.JSONDecodeError:
                        cancel_list = file2.read()
            except FileNotFoundError:
                with open(cancelled_store, "x", encoding="utf-8", newline=""):
                    pass

        def validate_date_signature(self, signature):
            """Method for validating sha256 values"""
            myregex = re.compile(r"[0-9a-fA-F]{64}$")
            res = myregex.fullmatch(signature)
            if not res:
                raise VaccineManagementException(self.DATE_SIGNATURE_NOT_VALID_EXCEPTION)
            return signature

        @classmethod
        def save_cancelation(cls, can_type, cancelled_store, date_sig):
            """Method save_cancelation from vaccine_manager"""
            to_dump = {"date_signature": date_sig, "cancelation_type": can_type}
            with open(cancelled_store, "w", encoding="utf-8", newline="") as file3:
                json.dump(to_dump, file3, indent=2)

        def check_json_structure(self, input_file_path, my_methods):
            """Method check_json_structure from vaccine_manager"""
            try:
                with open(input_file_path, "r", encoding="utf-8", newline="") as file:
                    data_list = json.load(file)
                    date_sig = my_methods.validate_date_signature(data_list["date_signature"])
                    can_type = data_list["cancelation_type"]
                    reason = data_list["reason"]
                    if len(data_list) != 3:
                        raise VaccineManagementException(self.DICT_TOO_LONG_EXCEPTION)
                    if len(reason) > 100 or len(reason) < 2:
                        raise VaccineManagementException(self.REASON_NOT_OK_EXCEPTION)
                    if can_type not in ('Temporal', 'Final'):
                        raise VaccineManagementException(self.CANCEL_TYPE_NOT_VALID_EXCEPTION)
            except KeyError as exception:
                raise VaccineManagementException(self.KEYERROR_EXCEPTION) from exception
            except json.JSONDecodeError as exception:
                raise VaccineManagementException(self.JSONDECODE_EXCEPTION) from exception
            return can_type, date_sig

    instance = None

    def __new__ ( cls ):
        if not FPMethods.instance:
            FPMethods.instance = FPMethods.FPMethods()
        return FPMethods.instance

    def __getattr__ ( self, nombre ):
        return getattr(self.instance, nombre)

    def __setattr__ ( self, nombre, valor ):
        return setattr(self.instance, nombre, valor)
