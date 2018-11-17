

class StringManipulation:

	""" Limit per line"""
	LINE_LENGTH_LIMIT = 40

	""" Define if should justify each line"""
	JUSTIFY_TEXT_LINE = True

	def __init__(self):
		self.input_text = ""
		self.output_text = ""
		self.current_line = ""

	def format(self):
		""" Return the given text whit setted indentation"""

		if not self.input_text:
			raise ValueError('No input text given.')

		self.limit_line_length()
		return self.output_text

	def set_input_text(self, input_text):
		"""Set text that should be formatted
			remove possible paragraphs at end of the file before set 
		"""
		input_text = self.remove_paragraphs_at_end(input_text)
		self.input_text = input_text.replace("\r", "").replace("\n", " \n")

	def remove_paragraphs_at_end(self, input_text):
		"""Check for paragraphs at end of the input"""
		if not input_text.endswith("\n") and not input_text.endswith("\r"):
			return input_text

		input_text = input_text[:-1]
		return self.remove_paragraphs_at_end(input_text)

	def limit_line_length(self):
		"""Apply current indentation settings to a given input"""
		input_words = self.input_text.split(" ")
		
		for word in input_words:
			if word.startswith("\n"):
				self.output_text += self.current_line
				self.current_line = word
			elif self.have_space_to_add(" " + word):
				self.current_line = self.concat_word(self.current_line, word)
			else:
				self.concat_new_line(word)

		self.concat_new_line("")

	def have_space_to_add(self, word):
		"""Check if there is still enough space to add current word"""
		return (len(self.current_line) + len(word)) <= self.LINE_LENGTH_LIMIT

	def concat_word(self, line, word):
		if not line:
			return word

		return line + " " + word


	def check_tabs_to_apply(self, tabs_to_apply, length_words):

		total = round(tabs_to_apply / length_words)

		if total < 1: return 1
		
		return total

	def concat_new_line(self, word):
		self.output_text += self.justify_text_line(self.current_line) + "\n"
		self.current_line = word

	def justify_text_line(self, line):
		if not self.JUSTIFY_TEXT_LINE:
			return line

		tabs_to_apply = 0
		line = line.rstrip()

		line_length = len(line) - line.count("\n")
		if line_length < self.LINE_LENGTH_LIMIT:
			tabs_to_apply = self.LINE_LENGTH_LIMIT - line_length

		if tabs_to_apply <= 0:
			return line

		new_line = ""
		words = line.split(" ")
		tab_by_word = self.check_tabs_to_apply(tabs_to_apply, len(words))

		tabs_applied = 0
		for word in words:
			if (tabs_applied + tab_by_word) <= tabs_to_apply:
				word += (" " * tab_by_word)
				tabs_applied += tab_by_word
			new_line = self.concat_word(new_line, word)

		line = self.justify_text_line(new_line)
		return line
