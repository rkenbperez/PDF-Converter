import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from config import EXPORTS_DIR, IMAGE_CONVERSION_MODE

import uuid
from pathlib import Path

from PIL import Image
from config import EXPORTS_DIR, IMAGE_CONVERSION_MODE

def pdf(directory: Path) -> Path:
    images = []
    for file in directory.iterdir():
        with Image.open(file) as image:
            images.append(image.convert(IMAGE_CONVERSION_MODE))
    export_pdf = EXPORTS_DIR / f'{uuid.uuid4()}.pdf'
    images[0].save(export_pdf, save_all=True, append_images=images[1:])
    return export_pdf