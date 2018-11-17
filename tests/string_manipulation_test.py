import os
import os.path
import unittest
from string_manipulation import StringManipulation


class StringManipulationTest(unittest.TestCase):

	def setUp(self):
		""" Create new StringManipulation instance """
		self.string_manipulation = StringManipulation()

	def test_excepts_if_empty_input(self):
		""" Assert StringManipulation raises ValueError exception 
			when not input data given 
		"""
		self.assertRaises(ValueError, self.string_manipulation.format)

	def test_format_method(self):

		with open("input_file.txt", "r") as file:
			self.string_manipulation.set_input_text(file.read())

		formatted_text = self.string_manipulation.format()

		""" Assert all lines have respect defined line length limit """
		for line in formatted_text.splitlines():
			self.assertTrue(len(line) <= self.string_manipulation.LINE_LENGTH_LIMIT)

		if not self.string_manipulation.JUSTIFY_TEXT_LINE:
			return

		""" Assert first lines has exactly same characters as LINE_LENGTH_LIMIT """ 
		for line in formatted_text.splitlines()[:3]:
			self.assertTrue(len(line) == self.string_manipulation.LINE_LENGTH_LIMIT)


if __name__ == '__main__':
	unittest.main()