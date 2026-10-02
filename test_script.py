import pybullet as p
import pybullet_data
import time

# 1. Connect to the physics server (GUI mode opens the visualization window)
physicsClient = p.connect(p.GUI)

# 2. Set the search path for default test assets (planes, cubes, etc.)
p.setAdditionalSearchPath(pybullet_data.getDataPath())

# 3. Load a ground plane (test world setup)
planeId = p.loadURDF("plane.urdf")

# 4. Set gravity
p.setGravity(0, 0, -9.81)

# 5. Add a "Drop Test" sphere slightly above the ground
startPos = [0, 0, 2]
startOrientation = p.getQuaternionFromEuler([0, 0, 0])
sphereId = p.loadURDF("sphere_small.urdf", startPos, startOrientation)

# 6. Run the simulation clock loop
for i in range(500):
    p.stepSimulation()
    time.sleep(1.0 / 240.0)

p.disconnect()