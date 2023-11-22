class ImageError(Exception): pass


class Image:
	def __init__(self, PillowImage):
		self.Image = PillowImage

	def retImage(self, Win):
		"""
		:param Win: CRS' Window
		:return: Returns PIL.Image pixels
		"""
		pixels = list(self.Image.getdata())
		if self.Image.size != (Win.x, Win.y):
			raise ImageError(f"Resolution of image: {self.Image.size}, but it must be ({Win.x}, {Win.y})!")
		pixels = [pixels[i * Win.x:(i + 1) * Win.x] for i in range(Win.y)]
		return pixels


def Text2List(filename):
	dm = open(filename, "r").read().split("\n")
	L = []
	for i in dm:
		L.append(list(i))
	return L
