from wand.image import Image as WImage
from PIL import Image as PImage
from io import BytesIO

def pillow2wand(pil, image_format = 'PNG'):
	"""
	Converts the incoming PIL image to a Wand image.
	The default image format for data exchange is PNG, which is fine for
	most use cases. You might want to override it only if you're using
	exotic channel combinations. Hint: TIFF is generally all-inclusive.
	"""
	byte_io = BytesIO()
	pil.save(byte_io, image_format)
	byte_io.seek(0)
	return WImage(blob=BytesIO.read(byte_io))

