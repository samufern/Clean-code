"""Tests for cancel_appointment"""
import unittest
import os
from freezegun import freeze_time
from uc3m_care import VaccineManager
from uc3m_care import VaccineManagementException
from uc3m_care import JSON_FILES_PATH, JSON_FILES_RF2_PATH
# pylint: disable=R0904

class MyTestCase(unittest.TestCase):
    """Class Test for cancel_appointment"""
    @freeze_time("2022-04-08")
    def test_ok(self):
        """Test ok"""
        file_test = JSON_FILES_RF2_PATH + "test_ok.json"
        cancelled_store = JSON_FILES_PATH + "cancelled_store.json"
        store_date = JSON_FILES_PATH + "store_date.json"
        if os.path.exists(cancelled_store):
            os.remove(cancelled_store)
        if os.path.exists(store_date):
            os.remove(store_date)


        my_manager = VaccineManager()

        value = my_manager.get_vaccine_date(file_test, "2022-08-08")
        cancelation = my_manager.cancel_appointment("test_ok.json")
        self.assertEqual(value, cancelation)  # add assertion here

        not_empty = False
        with open(cancelled_store, "r", encoding="utf-8", newline="") as file:
            store_list = file.read()
            if len(store_list) > 0:
                not_empty = True
            self.assertEqual(not_empty, True)

    @freeze_time("2022-04-08")
    def test_ok_2(self):
        """Test ok"""
        file_test = JSON_FILES_RF2_PATH + "test_ok.json"
        cancelled_store = JSON_FILES_PATH + "cancelled_store.json"
        store_date = JSON_FILES_PATH + "store_date.json"
        if os.path.exists(cancelled_store):
            os.remove(cancelled_store)
        if os.path.exists(store_date):
            os.remove(store_date)


        my_manager = VaccineManager()

        value = my_manager.get_vaccine_date(file_test, "2022-08-08")
        print(value)
        cancelation = my_manager.cancel_appointment("test_ok_2.json")
        self.assertEqual(value, cancelation)  # add assertion here

        not_empty = False
        with open(cancelled_store, "r", encoding="utf-8", newline="") as file:
            store_list = file.read()
            if len(store_list) > 0:
                not_empty = True
            self.assertEqual(not_empty, True)

    @freeze_time("2022-04-08")
    def test_2(self):
        """Test 2"""
        my_manager = VaccineManager()
        with self.assertRaises(VaccineManagementException) as exception:
            my_manager.cancel_appointment("test_2.json")
        self.assertEqual(exception.exception.message, "JsonDecode Exception")

    @freeze_time("2022-04-08")
    def test_3(self):
        """Test 3"""
        my_manager = VaccineManager()
        with self.assertRaises(VaccineManagementException) as exception:
            my_manager.cancel_appointment("test_3.json")
        self.assertEqual(exception.exception.message, "JsonDecode Exception")

    @freeze_time("2022-04-08")
    def test_4(self):
        """Test 4"""
        my_manager = VaccineManager()
        with self.assertRaises(VaccineManagementException) as exception:
            my_manager.cancel_appointment("test_4.json")
        self.assertEqual(exception.exception.message, "JsonDecode Exception")

    @freeze_time("2022-04-08")
    def test_5(self):
        """Test 5"""
        my_manager = VaccineManager()
        with self.assertRaises(VaccineManagementException) as exception:
            my_manager.cancel_appointment("test_5.json")
        self.assertEqual(exception.exception.message, "JsonDecode Exception")

    @freeze_time("2022-04-08")
    def test_6(self):
        """Test 6"""
        my_manager = VaccineManager()
        with self.assertRaises(VaccineManagementException) as exception:
            my_manager.cancel_appointment("test_6.json")
        self.assertEqual(exception.exception.message, "JsonDecode Exception")

    @freeze_time("2022-04-08")
    def test_7(self):
        """Test 7"""
        my_manager = VaccineManager()
        with self.assertRaises(VaccineManagementException) as exception:
            my_manager.cancel_appointment("test_7.json")
        self.assertEqual(exception.exception.message, "JsonDecode Exception")

    @freeze_time("2022-04-08")
    def test_8(self):
        """Test 8"""
        my_manager = VaccineManager()
        with self.assertRaises(VaccineManagementException) as exception:
            my_manager.cancel_appointment("test_8.json")
        self.assertEqual(exception.exception.message, "JsonDecode Exception")

    @freeze_time("2022-04-08")
    def test_9(self):
        """Test 9"""
        my_manager = VaccineManager()
        with self.assertRaises(VaccineManagementException) as exception:
            my_manager.cancel_appointment("test_9.json")
        self.assertEqual(exception.exception.message, "JsonDecode Exception")

    @freeze_time("2022-04-08")
    def test_10(self):
        """Test 10"""
        my_manager = VaccineManager()
        with self.assertRaises(VaccineManagementException) as exception:
            my_manager.cancel_appointment("test_10.json")
        self.assertEqual(exception.exception.message, "JsonDecode Exception")

    @freeze_time("2022-04-08")
    def test_14(self):
        """Test 14"""
        my_manager = VaccineManager()
        with self.assertRaises(VaccineManagementException) as exception:
            my_manager.cancel_appointment("test_14.json")
        self.assertEqual(exception.exception.message, "JsonDecode Exception")

    @freeze_time("2022-04-08")
    def test_15(self):
        """Test 15"""
        my_manager = VaccineManager()
        with self.assertRaises(VaccineManagementException) as exception:
            my_manager.cancel_appointment("test_15.json")
        self.assertEqual(exception.exception.message, "JsonDecode Exception")

    @freeze_time("2022-04-08")
    def test_16(self):
        """Test 16"""
        my_manager = VaccineManager()
        with self.assertRaises(VaccineManagementException) as exception:
            my_manager.cancel_appointment("test_16.json")
        self.assertEqual(exception.exception.message, "JsonDecode Exception")

    @freeze_time("2022-04-08")
    def test_23(self):
        """Test 23"""
        my_manager = VaccineManager()
        with self.assertRaises(VaccineManagementException) as exception:
            my_manager.cancel_appointment("test_23.json")
        self.assertEqual(exception.exception.message, "JsonDecode Exception")

    @freeze_time("2022-04-08")
    def test_24(self):
        """Test 24"""
        my_manager = VaccineManager()
        with self.assertRaises(VaccineManagementException) as exception:
            my_manager.cancel_appointment("test_24.json")
        self.assertEqual(exception.exception.message, "JsonDecode Exception")

    @freeze_time("2022-04-08")
    def test_25(self):
        """Test 25"""
        my_manager = VaccineManager()
        with self.assertRaises(VaccineManagementException) as exception:
            my_manager.cancel_appointment("test_25.json")
        self.assertEqual(exception.exception.message, "JsonDecode Exception")

    @freeze_time("2022-04-08")
    def test_26(self):
        """Test 26"""
        my_manager = VaccineManager()
        with self.assertRaises(VaccineManagementException) as exception:
            my_manager.cancel_appointment("test_26.json")
        self.assertEqual(exception.exception.message, "KeyError exception")

    @freeze_time("2022-04-08")
    def test_27(self):
        """Test 27"""
        my_manager = VaccineManager()
        with self.assertRaises(VaccineManagementException) as exception:
            my_manager.cancel_appointment("test_27.json")
        self.assertEqual(exception.exception.message, "KeyError exception")

    @freeze_time("2022-04-08")
    def test_28(self):
        """Test 28"""
        my_manager = VaccineManager()
        with self.assertRaises(VaccineManagementException) as exception:
            my_manager.cancel_appointment("test_28.json")
        self.assertEqual(exception.exception.message, "KeyError exception")

    @freeze_time("2022-04-08")
    def test_35(self):
        """Test 35"""
        my_manager = VaccineManager()
        with self.assertRaises(VaccineManagementException) as exception:
            my_manager.cancel_appointment("test_35.json")
        self.assertEqual(exception.exception.message, "Date Signature not valid")

    @freeze_time("2022-04-08")
    def test_36(self):
        """Test 36"""
        my_manager = VaccineManager()
        with self.assertRaises(VaccineManagementException) as exception:
            my_manager.cancel_appointment("test_36.json")
        self.assertEqual(exception.exception.message, "Date Signature not valid")

    @freeze_time("2022-04-08")
    def test_37(self):
        """Test 37"""
        my_manager = VaccineManager()
        with self.assertRaises(VaccineManagementException) as exception:
            my_manager.cancel_appointment("test_37.json")
        self.assertEqual(exception.exception.message, "Date Signature not valid")

    @freeze_time("2022-04-08")
    def test_44(self):
        """Test 44"""
        my_manager = VaccineManager()
        with self.assertRaises(VaccineManagementException) as exception:
            my_manager.cancel_appointment("test_44.json")
        self.assertEqual(exception.exception.message, "KeyError exception")

    @freeze_time("2022-04-08")
    def test_45(self):
        """Test 45"""
        my_manager = VaccineManager()
        with self.assertRaises(VaccineManagementException) as exception:
            my_manager.cancel_appointment("test_45.json")
        self.assertEqual(exception.exception.message, "KeyError exception")

    @freeze_time("2022-04-08")
    def test_46(self):
        """Test 46"""
        my_manager = VaccineManager()
        with self.assertRaises(VaccineManagementException) as exception:
            my_manager.cancel_appointment("test_46.json")
        self.assertEqual(exception.exception.message, "KeyError exception")

    @freeze_time("2022-04-08")
    def test_53(self):
        """Test 53"""
        my_manager = VaccineManager()
        with self.assertRaises(VaccineManagementException) as exception:
            my_manager.cancel_appointment("test_53.json")
        self.assertEqual(exception.exception.message, "Cancel Type not valid")

    @freeze_time("2022-04-08")
    def test_54(self):
        """Test 54"""
        my_manager = VaccineManager()
        with self.assertRaises(VaccineManagementException) as exception:
            my_manager.cancel_appointment("test_54.json")
        self.assertEqual(exception.exception.message, "Cancel Type not valid")

    @freeze_time("2022-04-08")
    def test_55(self):
        """Test 55"""
        my_manager = VaccineManager()
        with self.assertRaises(VaccineManagementException) as exception:
            my_manager.cancel_appointment("test_55.json")
        self.assertEqual(exception.exception.message, "Cancel Type not valid")

    @freeze_time("2022-04-08")
    def test_62(self):
        """Test 62"""
        my_manager = VaccineManager()
        with self.assertRaises(VaccineManagementException) as exception:
            my_manager.cancel_appointment("test_62.json")
        self.assertEqual(exception.exception.message, "KeyError exception")

    @freeze_time("2022-04-08")
    def test_63(self):
        """Test 63"""
        my_manager = VaccineManager()
        with self.assertRaises(VaccineManagementException) as exception:
            my_manager.cancel_appointment("test_63.json")
        self.assertEqual(exception.exception.message, "KeyError exception")

    @freeze_time("2022-04-08")
    def test_64(self):
        """Test 64"""
        my_manager = VaccineManager()
        with self.assertRaises(VaccineManagementException) as exception:
            my_manager.cancel_appointment("test_64.json")
        self.assertEqual(exception.exception.message, "KeyError exception")

    @freeze_time("2022-04-08")
    def test_71(self):
        """Test 71"""
        my_manager = VaccineManager()
        with self.assertRaises(VaccineManagementException) as exception:
            my_manager.cancel_appointment("test_71.json")
        self.assertEqual(exception.exception.message, "Reason Not OK")

    @freeze_time("2022-04-08")
    def test_72(self):
        """Test 72"""
        my_manager = VaccineManager()
        with self.assertRaises(VaccineManagementException) as exception:
            my_manager.cancel_appointment("test_72.json")
        self.assertEqual(exception.exception.message, "Reason Not OK")

    @freeze_time("2022-04-08")
    def test_73(self):
        """Test 73"""
        my_manager = VaccineManager()
        with self.assertRaises(VaccineManagementException) as exception:
            my_manager.cancel_appointment("test_73.json")
        self.assertEqual(exception.exception.message, "Reason Not OK")

    @freeze_time("2022-04-08")
    def test_77(self):
        """Test 77"""
        my_manager = VaccineManager()
        with self.assertRaises(VaccineManagementException) as exception:
            my_manager.cancel_appointment("test_77.json")
        self.assertEqual(exception.exception.message, "JsonDecode Exception")

    @freeze_time("2022-04-08")
    def test_78(self):
        """Test 78"""
        my_manager = VaccineManager()
        with self.assertRaises(VaccineManagementException) as exception:
            my_manager.cancel_appointment("test_78.json")
        self.assertEqual(exception.exception.message, "KeyError exception")

    @freeze_time("2022-04-08")
    def test_79(self):
        """Test 79"""
        my_manager = VaccineManager()
        with self.assertRaises(VaccineManagementException) as exception:
            my_manager.cancel_appointment("test_79.json")
        self.assertEqual(exception.exception.message, "Dict too long")

    @freeze_time("2022-04-08")
    def test_80(self):
        """Test 80"""
        my_manager = VaccineManager()
        with self.assertRaises(VaccineManagementException) as exception:
            my_manager.cancel_appointment("test_80.json")
        self.assertEqual(exception.exception.message, "JsonDecode Exception")

    @freeze_time("2022-04-08")
    def test_81(self):
        """Test 81"""
        my_manager = VaccineManager()
        with self.assertRaises(VaccineManagementException) as exception:
            my_manager.cancel_appointment("test_81.json")
        self.assertEqual(exception.exception.message, "JsonDecode Exception")

    @freeze_time("2022-04-08")
    def test_82(self):
        """Test 82"""
        my_manager = VaccineManager()
        with self.assertRaises(VaccineManagementException) as exception:
            my_manager.cancel_appointment("test_82.json")
        self.assertEqual(exception.exception.message, "KeyError exception")

    @freeze_time("2022-04-08")
    def test_83(self):
        """Test 83"""
        my_manager = VaccineManager()
        with self.assertRaises(VaccineManagementException) as exception:
            my_manager.cancel_appointment("test_83.json")
        self.assertEqual(exception.exception.message, "JsonDecode Exception")

    @freeze_time("2022-04-08")
    def test_84(self):
        """Test 84"""
        my_manager = VaccineManager()
        with self.assertRaises(VaccineManagementException) as exception:
            my_manager.cancel_appointment("test_84.json")
        self.assertEqual(exception.exception.message, "JsonDecode Exception")

    @freeze_time("2022-04-08")
    def test_85(self):
        """Test 85"""
        my_manager = VaccineManager()
        with self.assertRaises(VaccineManagementException) as exception:
            my_manager.cancel_appointment("test_85.json")
        self.assertEqual(exception.exception.message, "KeyError exception")

    @freeze_time("2022-04-08")
    def test_86(self):
        """Test 86"""
        my_manager = VaccineManager()
        with self.assertRaises(VaccineManagementException) as exception:
            my_manager.cancel_appointment("test_86.json")
        self.assertEqual(exception.exception.message, "JsonDecode Exception")

    @freeze_time("2022-04-08")
    def test_87(self):
        """Test 87"""
        my_manager = VaccineManager()
        with self.assertRaises(VaccineManagementException) as exception:
            my_manager.cancel_appointment("test_87.json")
        self.assertEqual(exception.exception.message, "JsonDecode Exception")

    @freeze_time("2022-04-08")
    def test_88(self):
        """Test 88"""
        my_manager = VaccineManager()
        with self.assertRaises(VaccineManagementException) as exception:
            my_manager.cancel_appointment("test_88.json")
        self.assertEqual(exception.exception.message, "KeyError exception")

    @freeze_time("2022-04-08")
    def test_89(self):
        """Test 89"""
        my_manager = VaccineManager()
        with self.assertRaises(VaccineManagementException) as exception:
            my_manager.cancel_appointment("test_89.json")
        self.assertEqual(exception.exception.message, "JsonDecode Exception")

    @freeze_time("2022-04-08")
    def test_90(self):
        """Test 90"""
        my_manager = VaccineManager()
        with self.assertRaises(VaccineManagementException) as exception:
            my_manager.cancel_appointment("test_90.json")
        self.assertEqual(exception.exception.message, "JsonDecode Exception")

    @freeze_time("2022-04-08")
    def test_91(self):
        """Test 91"""
        my_manager = VaccineManager()
        with self.assertRaises(VaccineManagementException) as exception:
            my_manager.cancel_appointment("test_91.json")
        self.assertEqual(exception.exception.message, "KeyError exception")

    @freeze_time("2022-04-08")
    def test_92(self):
        """Test 92"""
        my_manager = VaccineManager()
        with self.assertRaises(VaccineManagementException) as exception:
            my_manager.cancel_appointment("test_92.json")
        self.assertEqual(exception.exception.message, "JsonDecode Exception")

    @freeze_time("2022-04-08")
    def test_93(self):
        """Test 93"""
        my_manager = VaccineManager()
        with self.assertRaises(VaccineManagementException) as exception:
            my_manager.cancel_appointment("test_93.json")
        self.assertEqual(exception.exception.message, "JsonDecode Exception")

    @freeze_time("2022-04-08")
    def test_94(self):
        """Test 94"""
        my_manager = VaccineManager()
        with self.assertRaises(VaccineManagementException) as exception:
            my_manager.cancel_appointment("test_94.json")
        self.assertEqual(exception.exception.message, "Date Signature not valid")

    @freeze_time("2022-04-08")
    def test_95(self):
        """Test 95"""
        my_manager = VaccineManager()
        with self.assertRaises(VaccineManagementException) as exception:
            my_manager.cancel_appointment("test_95.json")
        self.assertEqual(exception.exception.message, "JsonDecode Exception")

    @freeze_time("2022-04-08")
    def test_96(self):
        """Test 96"""
        my_manager = VaccineManager()
        with self.assertRaises(VaccineManagementException) as exception:
            my_manager.cancel_appointment("test_96.json")
        self.assertEqual(exception.exception.message, "JsonDecode Exception")

    @freeze_time("2022-04-08")
    def test_97(self):
        """Test 97"""
        my_manager = VaccineManager()
        with self.assertRaises(VaccineManagementException) as exception:
            my_manager.cancel_appointment("test_97.json")
        self.assertEqual(exception.exception.message, "KeyError exception")

    @freeze_time("2022-04-08")
    def test_98(self):
        """Test 98"""
        my_manager = VaccineManager()
        with self.assertRaises(VaccineManagementException) as exception:
            my_manager.cancel_appointment("test_98.json")
        self.assertEqual(exception.exception.message, "Cancel Type not valid")

    @freeze_time("2022-04-08")
    def test_99(self):
        """Test 99"""
        my_manager = VaccineManager()
        with self.assertRaises(VaccineManagementException) as exception:
            my_manager.cancel_appointment("test_99.json")
        self.assertEqual(exception.exception.message, "JsonDecode Exception")

    @freeze_time("2022-04-08")
    def test_100(self):
        """Test 100"""
        my_manager = VaccineManager()
        with self.assertRaises(VaccineManagementException) as exception:
            my_manager.cancel_appointment("test_100.json")
        self.assertEqual(exception.exception.message, "Cancel Type not valid")

    @freeze_time("2022-04-08")
    def test_101(self):
        """Test 101"""
        my_manager = VaccineManager()
        with self.assertRaises(VaccineManagementException) as exception:
            my_manager.cancel_appointment("test_101.json")
        self.assertEqual(exception.exception.message, "KeyError exception")

    @freeze_time("2022-04-08")
    def test_102(self):
        """Test 102"""
        my_manager = VaccineManager()
        with self.assertRaises(VaccineManagementException) as exception:
            my_manager.cancel_appointment("test_102.json")
        self.assertEqual(exception.exception.message, "JsonDecode Exception")

    @freeze_time("2022-04-08")
    def test_103(self):
        """Test 103"""
        my_manager = VaccineManager()
        with self.assertRaises(VaccineManagementException) as exception:
            my_manager.cancel_appointment("test_103.json")
        self.assertEqual(exception.exception.message, "KeyError exception")
    @freeze_time("2022-04-08")
    def test_104(self):
        """Test 104"""
        my_manager = VaccineManager()
        with self.assertRaises(VaccineManagementException) as exception:
            my_manager.cancel_appointment("test_104.json")
        self.assertEqual(exception.exception.message, "JsonDecode Exception")

    @freeze_time("2022-04-08")
    def test_105(self):
        """Test 105"""
        my_manager = VaccineManager()
        with self.assertRaises(VaccineManagementException) as exception:
            my_manager.cancel_appointment("test_105.json")
        self.assertEqual(exception.exception.message, "JsonDecode Exception")

    @freeze_time("2022-04-08")
    def test_106(self):
        """Test 106"""
        my_manager = VaccineManager()
        with self.assertRaises(VaccineManagementException) as exception:
            my_manager.cancel_appointment("test_106.json")
        self.assertEqual(exception.exception.message, "JsonDecode Exception")

if __name__ == '__main__':
    unittest.main()
