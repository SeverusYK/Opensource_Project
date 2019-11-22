from ev3dev.ev3 import*

btn = Button()

# x, y, r은 입력 상수임


mB = LargeMotor('outB')
mC = LargeMotor('outC')

Center_x = 50    # 임의 값 width/2
Center_y = 25    # 임의 값 height/2
Config_r = 10    # 임의의 반지름(단위 모름)


if (x-Center_x) > 0:       # 원점을 기준으로 오른쪽에 위치할 때
    # turn right 
    mB.run_forever(speed_sp=450) 
    mC.stop(stop_action='brake') 
    if Config_r > r:       # 원의 반지름이이 기존 값보다 크게 보이면 거리가 가깝다고 판단 
        mB.run_to_rel_pos(position_sp=-360, speed_sp=200)
        mC.run_to_rel_pos(position_sp=-360, speed_sp=200)
    elif Config_r < r:     # 원의 반지름이 기존 값보다 작게 보이면 거리가 멀다고 판단
        mB.run_to_rel_pos(position_sp=360, speed_sp=200)
        mC.run_to_rel_pos(position_sp=360, speed_sp=200)       
    else:                  # 같으면 그냥 멈춤 
        mB.stop(stop_action='brake')
        mC.stop(stop_action='brake') 
elif x-Center_x <0:        # 원점을 기준으로 왼쪽에 위치할 때 
    # turn left 
    mB.stop(stop_action='brake') 
    mC.run_forever(speed_sp=450)
    if Config_r > r:
        mB.run_to_rel_pos(position_sp=-360, speed_sp=200)
        mC.run_to_rel_pos(position_sp=-360, speed_sp=200)
    elif Config_r < r:
        mB.run_to_rel_pos(position_sp=360, speed_sp=200)
        mC.run_to_rel_pos(position_sp=360, speed_sp=200)       
    else:
        mB.stop(stop_action='brake')
        mC.stop(stop_action='brake') 

else:
    if Config_r > r:
        mB.run_to_rel_pos(position_sp=-360, speed_sp=200)
        mC.run_to_rel_pos(position_sp=-360, speed_sp=200)
    elif Config_r < r:
        mB.run_to_rel_pos(position_sp=360, speed_sp=200)
        mC.run_to_rel_pos(position_sp=360, speed_sp=200)       
    else:
        mB.stop(stop_action='brake')
        mC.stop(stop_action='brake') 
