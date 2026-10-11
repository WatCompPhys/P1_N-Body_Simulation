import numpy as np
import math
import constants
import simulation

class ForceCalculator: 
    def computeForces(self, bodies: list[Body]) -> None: 
        for body in bodies:
            body.accel = simulation.BodyVector(0, 0, 0)  
            
        for i in range(len(bodies)):
            for j in range(i + 1, len(bodies)):
                r_vec = bodies[i].pos - bodies[j].pos
                r_mag = r_vec.magnitude()
                if r_mag == 0:
                    continue  
                f_mag = (constants.physicsConstants.G * bodies[i].mass * bodies[j].mass) / (r_mag ** 2)
                f_vec = scale(r_vec, f_mag / r_mag) 
                bodies[i].accel += scale(f_vec, 1 / bodies[i].mass)
                bodies[j].accel -= scale(f_vec, 1 / bodies[j].mass)
        