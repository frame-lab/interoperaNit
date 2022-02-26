from tqdm import tqdm


class Verbose:
	def __init__(self, text, lines):
		self.bar = tqdm(total=lines, desc=text, unit="line", ncols=80)

	def update(self):
		self.bar.update(1)

	def end(self):
		self.bar.close()
