# Berkay Gurkan 2024-28-10
# This code generates empty scene

import argparse    
from omni.isaac.lab.app import AppLauncher


# create argument parser
parser = argparse.ArgumentParser(description="Create empty scene")
# append AppLauncher cli args
AppLauncher.add_app_launcher_args(parser)
# parse the arguments
# command line arguments include launching the app headless, configuring different Livestream options, and enabling off-screen rendering.
args_cli = parser.parse_args()  
# launch omniverse app
app_launcher = AppLauncher(args_cli)
simulation_app = app_launcher.app

from omni.isaac.lab.sim import SimulationCfg, SimulationContext

def main():
    """Main function."""

    # Initialize the simulation context
    sim_cfg = SimulationCfg(dt=0.01)
    sim = SimulationContext(sim_cfg)
    
    # Set main camera
    sim.set_camera_view((2.5, 2.5, 2.5), (0.0, 0.0, 0.0))
    # Play the simulator
    sim.reset()
    
    # Now we are ready!
    print("[INFO]: Setup complete...")

    # Simulate physics
    while simulation_app.is_running():
        # perform step
        sim.step()

if __name__ == "__main__":
    # run the main function
    main()
    # close sim app
    simulation_app.close()