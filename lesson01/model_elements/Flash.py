class Flash:
    def __init__(self, location: Point3D, angle: angle3D, color: color, power: float) -> None:
        self.location = location
        self.angle = angle
        self.color = color
        self.power = power

    def rotate(self, data: angle3D) -> None:
        pass

    def move(self, data: Point3D) -> None:
        pass