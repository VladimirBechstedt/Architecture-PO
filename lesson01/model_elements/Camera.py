class Camera:
    def __init__(self, location: Point3D, angle: Angle3D) -> None:
        self.location = location
        self.angle = angle

    def rotate(self, data: Angle3D) -> None:
        pass

    def move(self, data: Point3D) -> None:
        pass