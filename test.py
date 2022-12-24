from unittest import TestCase
from two_one import *


class ReportTableUnitTests(TestCase):
    def test_clean_html(self):
        self.assertEqual(DataSet.delete_html("abc"), "abc")

    def test_spaces_with_one_tag(self):
        self.assertEqual(DataSet.delete_html("<div>abc"), 'abc')

    def test_spaces_with_double_tag(self):
        self.assertEqual(DataSet.delete_html("<div>abc</div>"), 'abc')

    def test_spaces_with_spaces(self):
        self.assertEqual(DataSet.delete_html("   abd  "), "abd")

    def test_spaces_with_spaces_and_two_words(self):
        self.assertEqual(DataSet.delete_html(" abc     abd"), 'abc abd')

    def test_spaces_with_many_spaces_and_tags(self):
        self.assertEqual(DataSet.delete_html(" <div><strong><i>  abc <i>  abd  <string>"), 'abc abd')

    def test_spaces_with_many_spaces_and_tags_and_incorrect_tag(self):
        self.assertEqual(DataSet.delete_html(" <div> abc <iqewwewr> <  div   > abd <i>"), 'abc abd')

    def test_salary_from(self):
        self.assertEqual(Salary(10.0, 20.4, 'RUR').salary_from, 10.0)

    def test_salary_to(self):
        self.assertEqual(Salary(10.0, 20.4, 'RUR').salary_to, 20.4)

    def test_salary_currency(self):
        self.assertEqual(Salary(10.0, 20.4, 'RUR').salary_currency, 'RUR')

    def test_currency_to_rub(self):
        self.assertEqual(Salary(10, 20, 'EUR').to_rub(10 + 20), 1797.0)

    def test_float_salary_from_to_rub(self):
        self.assertEqual(Salary(10.0, 20, 'RUR').to_rub(10.0 + 20), 30.0)

    def test_float_salary_to_rub(self):
        self.assertEqual(Salary(10, 20.0, 'RUR').to_rub(10 + 20.0), 30.0)

    def test_AZN_currency_to_rub(self):
        self.assertEqual(Salary(10, 20, 'AZN').to_rub(10 + 20), 1070.4)

    def test_vacancy_type(self):
        vacancy_roll = Vacancy({'name': 'IT', 'salary_from': '200.00', 'salary_to': '240.00', 'salary_currency': 'GEL',
                                     'area_name': 'Russia', 'published_at': '2020-10-20'})
        self.assertEqual((type(vacancy_roll).__name__), 'Vacancy')

    def test_vacancy_name(self):
        vacancy_roll = Vacancy({'name': 'IT', 'salary_from': '200.00','salary_to': '240.00', 'salary_currency': 'GEL',
                                     'area_name': 'Russia', 'published_at': '2020-10-20'})
        self.assertEqual((vacancy_roll.name), 'IT')

    def test_vacancy_area_name(self):
        vacancy_for_tests = Vacancy({'name': 'IT', 'salary_from': '200.00','salary_to': '240.00', 'salary_currency': 'GEL',
                                     'area_name': 'Russia', 'published_at': '2020-10-20'})
        self.assertEqual((vacancy_for_tests.area_name),  'Russia')

    def test_vacancy_published_at(self):
        vacancy_roll = Vacancy({'name': 'IT', 'salary_from': '200.00','salary_to': '240.00', 'salary_currency': 'GEL',
                                     'area_name': 'Russia', 'published_at': '2020-10-20'})
        self.assertEqual((vacancy_roll.published_at), '2020-10-20')
