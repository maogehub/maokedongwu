"""check if photo is black and white

lazy:http://stackoverflow.com/questions/20068945/detect-if-image-is-color-grayscale-or-black-and-white-with-python-pil
author: Gepeto

"""
from PIL import Image, ImageStat

def isblack(filename):
    """check if filename is a black & white photo
    """    
    MONOCHROMATIC_MAX_VARIANCE = 0.005
    COLOR = 1000
    MAYBE_COLOR = 200
    v = ImageStat.Stat(Image.open(filename)).var
    is_monochromatic = reduce(lambda x, y: x and y < MONOCHROMATIC_MAX_VARIANCE, v, True)
    if is_monochromatic:
        return True
    else:
        if len(v)==3:
            maxmin = abs(max(v) - min(v))
            if maxmin > COLOR:
                return False
            elif maxmin > MAYBE_COLOR:
                return False
            else:
                return True
        elif len(v)==1:
            return True
        else:
            #don't know
            return None  
    return False