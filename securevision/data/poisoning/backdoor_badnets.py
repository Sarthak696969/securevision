from PIL import ImageDraw

def inject_badnets_trigger(img, size=3, corner="br"):
    img = img.copy()
    draw = ImageDraw.Draw(img)
    w,h = img.size
    for i in range(size):
        for j in range(size):
            x = w-1-j if 'r' in corner else j
            y = h-1-i if 'b' in corner else i
            draw.point((x,y), fill=(255,255,255))
    return img
