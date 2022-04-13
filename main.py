from motorLLC import *

mc = motorLLC()

mc.open()
mc.toruqe_enable()

index = 0
dxl_goal_position = [DXL_MINIMUM_POSITION_VALUE, DXL_MAXIMUM_POSITION_VALUE]         # Goal position

for i in range(1, 6):
    mc.moveto(dxl_goal_position[index])

    # Change goal position
    if index == 0:
        index = 1
    else:
        index = 0

mc.close()
