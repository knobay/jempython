# A swimmer at position A wants to cross the river of width w. The swimmer can swim with a
# constant velocity v but only along the x-axis. The water itself flows with velocity
# v along the y-axis. Once the swimmer enters the water and starts to cross the river,
# the water will carry him with it and cause him to drift downstream with respect to his
# original position. Write a code that calculates the position B at which the swimmer reaches
# the other shore for: vSwimmer = 0.5, vWater = 1, and w = 10. Display your result.

vSwimmer=0.5
vWater=1.0
w=10.0
drift=0.0 # how far the swimmer has drifted downstream
y=0.5 # y coordinate initialisation
time=0.0

time=w/vSwimmer
drift=vWater*time
y-=drift

print('B=', y)