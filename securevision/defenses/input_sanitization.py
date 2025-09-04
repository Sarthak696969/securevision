from PIL import Image
from securevision.utils.image_ops import jpeg_compress, bit_depth_reduction, median_filter

def apply_sanitization(img: Image.Image, method: str, **kwargs) -> Image.Image:
    if method == "jpeg":
        return jpeg_compress(img, quality=kwargs.get("quality",50))
    if method == "bitdepth":
        return bit_depth_reduction(img, bits=kwargs.get("bits",5))
    if method == "median":
        return median_filter(img, k=kwargs.get("k",3))
    raise ValueError("Unknown method")
