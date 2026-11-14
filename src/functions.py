import numpy as np
import math
import constants
import simulation

class ForceCalculator: 
    def gravitationalForces(self, a : Body, b : Body) -> BodyVector:
        r_vec = a.pos - b.pos
        r_mag = r_vec.magnitude()
        
        if r_mag == 0:
            return simulation.BodyVector(0, 0, 0)  
        
        f_mag = (constants.physicsConstants.G * a.mass * b.mass) / (r_mag ** 2)
        f_vec = r_vec.scale(f_mag / r_mag) 
        
        return f_vec
    
    def computeForces(self, bodies: list[Body]) -> None:
        for body in bodies:
            body.accel = simulation.BodyVector(0, 0, 0)
            
        for i in range(len(bodies)):
            for j in range(i + 1, len(bodies)):
                bodies[i].accel += self.gravitationalForces(bodies[i], bodies[j]).scale(1 / bodies[i].mass)
                bodies[j].accel -= self.gravitationalForces(bodies[i], bodies[j]).scale(1 / bodies[j].mass)

class KinematicCalculator: 
    # int time_each_step
    
    ''' 
    As I need to access the acceleration of the bodies from a prior step, 
    I will need to pass in a list of accelerations.
    
    An additional step is needed before calling the computeForces function to 
    store the current accelerations of the bodies in a list, which will then be 
    passed into this function
    '''
       
    def KinemtaticCalculator(self, bodies: list[Body], oldacc, time_each_step: float): 
        i = 0
        for body in bodies: 
            body.pos = body.pos + body.vel.scale(time_each_step) + body.accel.scale(0.5 * time_each_step ** 2)
            body.vel = body.vel + (oldacc[i]+body.accel).scale(0.5 * time_each_step)
            i += 1
        