class Vector4:
    def __init__(self, x, y, z, w):
        self.x = x
        self.y = y
        self.z = z
        self.w = w

    def multiply(self, f):
        self.x *= f
        self.y *= f
        self.z *= f
        self.w += f
