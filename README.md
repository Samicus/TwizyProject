# TwizyProject
Github repository for bachelor thesis

Starting the car requiers the correct codes on both micro controller in in the front of the car,
contact the group members from 2018 for more info. There are some elctrical problems in the car 
(from previus projects), if the car dashnoard says "stop" the car will not drive and needs a restart 
if it does not go away. After every run the power cabel (USB connecting on the left side)for the
throttle will need to be disconectet, otherwise it will store last value and drive unwanted. 
Also be aware of the throttle, as it is a PI regulator it can essaly build up and give 100% 
throttle in unwanted situations. 

Read \catikin_workspace\beginner_tutorials\scripts\darkflow-master\bin\readMe.txt for instructions on how to get the required files for YOLO.



Step 1
  - start roscore, open a terminal$ roscore
  
Step 2 
  - start realsense camera1, in new terminal$ roslaunch realsense2_camera rs_camera.launch camera:=cam_1 serial_no:=817412071115
  
Ny terminal:

  - start realsense camera2, in new terminal$ roslaunch realsense2_camera rs_camera.launch camera:=cam_2 serial_no:=938422076468
  
step 3
  - start yolo, in new terminal$ conda activate yolo $ roscd beginner_tutorials/scripts/darkflow-master/ $ rosrun beginner_tutorial yoloPub2_7a.py
  
  step 4
  - start yolo, in new terminal$ conda activate yolo $ roscd beginner_tutorials/scripts/darkflow-master/ $ rosrun beginner_tutorial yoloPub2_7b.py

step 5
- for wheel odmerty, $ cd _apllo/apollo $ bash dev_start.sh $ bash dev_into.sh $ bash start_wheelodometry.sh, in new termianl $ rosrun beginner_tutorials read_position.py

step 6
  - start depth camera, in new terminal $ rosrun beginner_tutorials depthOutputSam.py
Ny termnial:
$ rosrun beginner_tutorials depthOutputErik.py       
  - start map/planning, in new terminal $ rosrun beginner_tutorials ppNoa.py
  - start aim, in new terminal $ rosrun beginner_tutorials aim_goal_fixed.py
step 7
  - start canbus, warning will make the car drive, in new termianl $ rosrun beginner_tutorials control_node
