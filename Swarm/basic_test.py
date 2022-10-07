# def step_2(i, tello):
# 	swarm.sync()
# 	if i == 1:
# 		print(i)
# 		# Do Stuff
# 	if i == 2:
# 		print(i)
# 		# Do Stuff
# 	if i == 3:
# 		print(i)
# 		# Do Stuff

from djitellopy import TelloSwarm

swarm = TelloSwarm.fromIps([
    "11.1.1.100",
    "11.1.1.101",
    "11.1.1.102"
])

swarm.connect()
swarm.takeoff()

def step_1(i, tello):
	tello.move_up(30)
	swarm.sync()

	if i == 1:
		tello.move_up(50)

	if i == 0:
		print(i)
	
	if i == 2:
		tello.move_up(100)

	swarm.sync()

def step_2(i, tello):
	swarm.sync()
	if i == 1:
		print(i)
		tello.move_forward(250)
		# Do Stuff
	if i == 0:
		tello.move_right(500)
		# Do Stuff
	if i == 2:
		print(i)
		tello.move_left(500)
		# Do Stuff
	
	swarm.sync()
	

def step_3(i, tello):
	swarm.sync()
	if i == 1:
		print(i)
		tello.move_down(50)
		# Do Stuff
	if i == 0:
		tello.move_back(250)
		# Do Stuff
	if i == 2:
		print(i)
		tello.move_down(100)
		# Do Stuff
	
	swarm.sync()

swarm.parallel(step_1)
swarm.parallel(step_2)
swarm.parallel(step_3)

swarm.land()
swarm.end()

