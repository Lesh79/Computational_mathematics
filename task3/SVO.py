from copy import deepcopy
from struct import unpack, pack

import numpy as np
from PIL import Image

from task3.SVD import SVD, PrimitiveSVD, BlockPowerSVD, Encoder


class SVO:
    def __init__(self, file_path, encoder: Encoder):
        self.r = None
        self.g = None
        self.b = None
        with open(file_path, "rb") as f:
            magic_number = unpack("<4s", f.read(4))[0]
            if magic_number == b'SVO':
                self.load(f)
            else:
                self.encode(Image.open(file_path), encoder)

    def encode(self, img, encoder: Encoder):
        if encoder is None:
            encoder = SVD(2)
        r, g, b = img.split()
        self.r = deepcopy(encoder).compress(np.array(r))
        self.g = deepcopy(encoder).compress(np.array(g))
        self.b = deepcopy(encoder).compress(np.array(b))

    def decode(self):
        if self.r is None or self.g is None or self.b is None:
            raise ValueError("Image is empty, nothing to decode")
        img = np.zeros((self.r.u.shape[0], self.b.v.shape[1], 3), dtype=np.uint8)
        img[:, :, 0] = self.r.decompress()
        img[:, :, 1] = self.g.decompress()
        img[:, :, 2] = self.b.decompress()
        return Image.fromarray(img)

    def load(self, file, offset=0):
        file.seek(offset + 4)  # Skip magic number
        version = unpack("<b", file.read(1))[0]
        if version != 1:
            raise ValueError("Unsupported version")

        self.r = SVD(2).read(file.read())
        self.g = SVD(2).read(file.read())
        self.b = SVD(2).read(file.read())

    def save(self, file_path: str):
        with open(file_path, 'wb') as file:
            file.write(pack("<4s", b'SVO'))
            file.write(self.r.to_bytes())
            file.write(self.g.to_bytes())
            file.write(self.b.to_bytes())


def compress_img(img: str, new_img: str, ratio: float, encode: str):
    decoder = None
    if encode == "numpy":
        decoder = SVD(compression_ratio=ratio)
    elif encode == "power":
        decoder = PrimitiveSVD(compression_ratio=ratio)
    elif encode == "block":
        decoder = BlockPowerSVD(compression_ratio=ratio)
    svo = SVO(img, decoder)
    svo.save("ZOV.SVO")
    decoded_image = svo.decode()
    decoded_image.save(new_img)


compress_img("img/shape.bmp", "compress_img/shapeNP.bmp", 0.03, "numpy")
compress_img("img/shape.bmp", "compress_img/shapePower.bmp", 0.03, "power")
compress_img("img/shape.bmp", "compress_img/shapeBlock.bmp", 0.03, "block")
