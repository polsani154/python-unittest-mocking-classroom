from unittest import TestCase
from unittest.mock import patch
from src.db_helper import DbHelper


class TestDb(TestCase):
    def setUp(self):
        self.db = DbHelper()

    # def test_sum_without_mocking(self):
    #     database = DbHelper()
    #     self.assertGreater(database.get_maximum_salary,database.get_manimum_salary)

    @patch("src.db_helper.DbHelper")
    def test_max_salary_is_greater_than_min_salary(self, MockDbHelper):
        database = MockDbHelper()
        # create a mock object of Calculator class. This will help to customize output of class methods

        """
        mock the sum() method of Calculator class to return value '1'. Noth that since we have mocked/stubbed the
        sum method, it will not execute the actual logic whenever called and just return 1 irrespective of input.
        """
        database.get_maximum_salary.return_value = 100
        database.get_manimum_salary.return_value = 50

        actual = (
            database.get_maximum_salary() - database.get_manimum_salary()
        )  # calling the sum method but the mocked version will actually get called

        self.assertGreater(database.get_maximum_salary(), database.get_manimum_salary())

        # now override the mocked sum method to return 10
        database.get_maximum_salary.return_value = 10
        database.get_manimum_salary.return_value = 5

        self.assertGreater(
            database.get_maximum_salary(), database.get_manimum_salary(), msg=None
        )

