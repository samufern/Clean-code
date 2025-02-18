"""Module """
from datetime import datetime
from uc3m_care.data.vaccine_patient_register import VaccinePatientRegister
from uc3m_care.data.vaccination_appointment import VaccinationAppointment
from uc3m_care.exception.vaccine_management_exception import VaccineManagementException
from uc3m_care.cfg.vaccine_manager_config import JSON_FILES_PATH
from uc3m_care.final_practice_methods import FPMethods

class VaccineManager:
    """Class for providing the methods for managing the vaccination process"""

    # pylint: disable=invalid-name
    class __VaccineManager:
        CANCELLED_STORE = JSON_FILES_PATH + "cancelled_store.json"
        STORE_DATE = JSON_FILES_PATH + "store_date.json"
        STORE_VACCINE = JSON_FILES_PATH + "store_vaccine.json"

        def __init__(self):
            pass

        #pylint: disable=too-many-arguments
        # pylint: disable=no-self-use
        def request_vaccination_id (self, patient_id,
                                    name_surname,
                                    registration_type,
                                    phone_number,
                                    age):
            """Register the patinent into the patients file"""
            my_patient = VaccinePatientRegister(patient_id,
                                                    name_surname,
                                                    registration_type,
                                                    phone_number,
                                                    age)

            my_patient.save_patient()
            return my_patient.patient_sys_id

        def get_vaccine_date(self, input_file, date):
            """Gets an appointment for a registered patient"""
            date_1 = str(datetime.today())
            current_date = datetime.fromisoformat(date_1)

            date_2 = date
            proposed_date = datetime.fromisoformat(date_2)

            if proposed_date <= current_date:
                raise VaccineManagementException("Date has passed")

            my_sign = VaccinationAppointment.create_appointment_from_json_file(input_file)
            my_sign.save_appointment()

            store_path = JSON_FILES_PATH + "store_date.json"
            my_methods = FPMethods()
            store_list = my_methods.store_list_date(date, store_path)
            to_dump = store_list
            my_methods.convert_to_json(store_path, to_dump)
            return my_sign.date_signature

        def vaccine_patient(self, date_signature):
            """Register the vaccination of the patient"""
            appointment = VaccinationAppointment.get_appointment_from_date_signature(date_signature)
            return appointment.register_vaccination()

        def cancel_appointment(self, input_file):
            "cancelation of the appointment"
            input_file_path = JSON_FILES_PATH + "cancel_appointment/" + input_file
            my_methods = FPMethods()
            can_type, date_sig = my_methods.check_json_structure(input_file_path, my_methods)
            my_methods.read_store_vaccine(date_sig, self.STORE_VACCINE)
            my_methods.check_appointment_time()
            my_methods.check_if_date_exists(date_sig, self.STORE_DATE)
            my_methods.check_if_date_was_cancelled(self.CANCELLED_STORE, date_sig)
            my_methods.save_cancelation(can_type, self.CANCELLED_STORE, date_sig)
            return date_sig

    instance = None

    def __new__(cls):
        if not VaccineManager.instance:
            VaccineManager.instance = VaccineManager.__VaccineManager()
        return VaccineManager.instance

    def __getattr__(self, nombre):
        return getattr(self.instance, nombre)

    def __setattr__(self, nombre, valor):
        return setattr(self.instance, nombre, valor)
