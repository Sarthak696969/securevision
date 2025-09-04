from PIL import Image, ImageFilter
import io

def jpeg_compress(img: Image.Image, quality: int = 50) -> Image.Image:
    buf = io.BytesIO()
    img.save(buf, format="JPEG", quality=quality)
    buf.seek(0)
    return Image.open(buf).convert("RGB")

def bit_depth_reduction(img: Image.Image, bits: int = 5) -> Image.Image:
    levels = 2 ** bits
    return img.point(lambda p: int(p / (256/levels)) * int(256/levels))

def median_filter(img: Image.Image, k: int = 3) -> Image.Image:
    return img.filter(ImageFilter.MedianFilter(size=k))
