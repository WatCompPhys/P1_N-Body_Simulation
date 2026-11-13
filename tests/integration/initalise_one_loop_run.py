##Test initialise_one_loop_run

##This test will perform a single run of the simulation loop however, instead of directly passing the list of bodies,
## the list will be initialised in Simulation.py and then passed to the force calculator, this is essentially the combination of
## the 10_body_initialisation and compute_forces_loop tests.