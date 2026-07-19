class BodyVector:
    """This class stores a single 3D vector"""
    x: float
    y: float
    z: float

    def __init__(self, x=0, y=0, z=0) -> None:
        self.x = x
        self.y = y
        self.z = z


    def __repr__(self) -> str:
        return f"BodyVector({self.x}, {self.y}, {self.z})"


    def __str__(self) -> str:
        return f"[{self.x}, {self.y}, {self.z}]"




class Body:
    """This class stores all relevant information for a single body."""
    mass:             float
    position:         BodyVector
    velocity:         BodyVector
    acceleration:     BodyVector
    previousPosition: BodyVector 
    
    def __init__(self, mass=0, position=BodyVector(), velocity=BodyVector(), acceleration=BodyVector(), previousPosition=BodyVector()) -> None:
        self.mass             = mass
        self.position         = position
        self.velocity         = velocity
        self.acceleration     = acceleration
        self.previousPosition = previousPosition


    def __repr__(self) -> str:
        return f"Body({self.mass}, {self.pos}, {self.vel}, {self.accel}, {self.prevPos})"


    def __str__(self) -> str:
        return f"""
mass:              {self.mass}
position:          {self.position}
velocity:          {self.velocity}
acceleration:      {self.acceleration}
previous position: {self.previousPosition}
"""


Earth = Body((5.972*10**24))

print(Earth)

