import numpy as np
import math
import constants
import simulation

class ForceCalculator: 
    def computeForces(self, bodies: list[Body]) -> None: 
        for i in range(len(bodies)):
            for j in range(i + 1, len(bodies)):
                r_vec = bodies[i].pos - bodies[j].pos
                r_mag = r_vec.magnitude()
                if r_mag == 0:
                    continue  # Avoid division by zero
                g_mag = (constants.physicsConstants.G * bodies[i].mass) / (r_mag ** 2)
                g_vec = scale(r_vec, g_mag / r_mag) 
                bodies[i].accel += g_vec
                bodies[j].accel -= g_vec
        