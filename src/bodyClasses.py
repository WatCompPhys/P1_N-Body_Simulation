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
    mass:    float        ## kg
    pos:     BodyVector   ## m
    vel:     BodyVector   ## m/s
    accel:   BodyVector   ## m/s^2
    prevPos: BodyVector   ## m
    
    def __init__(self, mass=0, pos=BodyVector(), vel=BodyVector(), accel=BodyVector(), prevPos=BodyVector()) -> None:
        self.mass    = mass
        self.pos     = pos
        self.vel     = vel
        self.accel   = accel
        self.prevPos = prevPos


    def __repr__(self) -> str:
        return f"Body({self.mass}, {self.pos}, {self.vel}, {self.accel}, {self.prevPos})"


    def __str__(self) -> str:
        return f"""
Mass:              {self.mass}
Position:          {self.pos}
Velocity:          {self.vel}
Acceleration:      {self.accel}
Previous Position: {self.prevPos}
"""


Earth = Body((5.972*10**24))

print(Earth)

