# Patrol run log

Output of `./scripts/patrol.sh` from a full run with Gazebo and RViz open. The robot visited all 5 waypoints with no recoveries and no failed goals.

| Goal | Target (x, y, yaw) | Result | Time |
|---|---|---|---|
| 1 | (-1.20, 1.80, 0 deg) | reached | ~14 s |
| 2 | (1.20, 1.80, -45 deg) | reached | ~15 s |
| 3 | (1.20, -1.80, 180 deg) | reached | ~23 s |
| 4 | (-1.20, -1.80, 135 deg) | reached | ~16 s |
| 5 | (-2.00, -0.50, 0 deg) | reached | ~12 s |

Total route time: about 80 seconds.

## Raw log

```
ubuntu@anurag-ubuntu22:~/projects/navturtle$ ./scripts/patrol.sh
[env] ROS_DISTRO=humble TURTLEBOT3_MODEL=burger
[INFO] [1793469680.918376411] [basic_navigator]: Publishing Initial Pose
[INFO] [1793469685.991005380] [basic_navigator]: Nav2 is ready for use!
[INFO] [1793469685.991468976] [basic_navigator]: Goal 1/5: x=-1.20 y=1.80 yaw=0
[INFO] [1793469685.992378924] [basic_navigator]: Navigating to goal: -1.2 1.8...
[INFO] [1793469688.007448670] [basic_navigator]:   distance remaining: 2.30 m
[INFO] [1793469690.021254455] [basic_navigator]:   distance remaining: 1.77 m
[INFO] [1793469692.035122433] [basic_navigator]:   distance remaining: 1.42 m
[INFO] [1793469694.049263277] [basic_navigator]:   distance remaining: 0.95 m
[INFO] [1793469696.064222298] [basic_navigator]:   distance remaining: 0.50 m
[INFO] [1793469698.077660749] [basic_navigator]:   distance remaining: 0.25 m
[INFO] [1793469700.091311043] [basic_navigator]:   distance remaining: 0.26 m
[INFO] [1793469700.406742123] [basic_navigator]: Goal 1 reached
[INFO] [1793469700.407319829] [basic_navigator]: Goal 2/5: x=1.20 y=1.80 yaw=-45
[INFO] [1793469700.408236960] [basic_navigator]: Navigating to goal: 1.2 1.8...
[INFO] [1793469702.429501077] [basic_navigator]:   distance remaining: 2.37 m
[INFO] [1793469704.449549924] [basic_navigator]:   distance remaining: 1.97 m
[INFO] [1793469706.465877871] [basic_navigator]:   distance remaining: 1.50 m
[INFO] [1793469708.482047871] [basic_navigator]:   distance remaining: 1.07 m
[INFO] [1793469710.494503729] [basic_navigator]:   distance remaining: 0.65 m
[INFO] [1793469712.508378468] [basic_navigator]:   distance remaining: 0.22 m
[INFO] [1793469714.524195516] [basic_navigator]:   distance remaining: 0.24 m
[INFO] [1793469715.122196314] [basic_navigator]: Goal 2 reached
[INFO] [1793469715.122739809] [basic_navigator]: Goal 3/5: x=1.20 y=-1.80 yaw=180
[INFO] [1793469715.123923509] [basic_navigator]: Navigating to goal: 1.2 -1.8...
[INFO] [1793469717.143141755] [basic_navigator]:   distance remaining: 3.90 m
[INFO] [1793469719.156254378] [basic_navigator]:   distance remaining: 3.52 m
[INFO] [1793469721.169164949] [basic_navigator]:   distance remaining: 3.02 m
[INFO] [1793469723.182754054] [basic_navigator]:   distance remaining: 2.65 m
[INFO] [1793469725.196688888] [basic_navigator]:   distance remaining: 2.15 m
[INFO] [1793469727.209555318] [basic_navigator]:   distance remaining: 1.75 m
[INFO] [1793469729.226814702] [basic_navigator]:   distance remaining: 1.30 m
[INFO] [1793469731.241184312] [basic_navigator]:   distance remaining: 0.87 m
[INFO] [1793469733.256672781] [basic_navigator]:   distance remaining: 0.42 m
[INFO] [1793469735.269890767] [basic_navigator]:   distance remaining: 0.22 m
[INFO] [1793469737.285136947] [basic_navigator]:   distance remaining: 0.18 m
[INFO] [1793469737.750080811] [basic_navigator]: Goal 3 reached
[INFO] [1793469737.750630132] [basic_navigator]: Goal 4/5: x=-1.20 y=-1.80 yaw=135
[INFO] [1793469737.751677961] [basic_navigator]: Navigating to goal: -1.2 -1.8...
[INFO] [1793469739.774622793] [basic_navigator]:   distance remaining: 2.45 m
[INFO] [1793469741.789536417] [basic_navigator]:   distance remaining: 2.05 m
[INFO] [1793469743.803664314] [basic_navigator]:   distance remaining: 1.55 m
[INFO] [1793469745.817183747] [basic_navigator]:   distance remaining: 1.15 m
[INFO] [1793469747.833994008] [basic_navigator]:   distance remaining: 0.67 m
[INFO] [1793469749.849944951] [basic_navigator]:   distance remaining: 0.27 m
[INFO] [1793469751.863089556] [basic_navigator]:   distance remaining: 0.21 m
[INFO] [1793469753.274801449] [basic_navigator]: Goal 4 reached
[INFO] [1793469753.275313533] [basic_navigator]: Goal 5/5: x=-2.00 y=-0.50 yaw=0
[INFO] [1793469753.276282102] [basic_navigator]: Navigating to goal: -2.0 -0.5...
[INFO] [1793469755.299701205] [basic_navigator]:   distance remaining: 1.19 m
[INFO] [1793469757.313980272] [basic_navigator]:   distance remaining: 0.80 m
[INFO] [1793469759.329951331] [basic_navigator]:   distance remaining: 0.37 m
[INFO] [1793469761.347187792] [basic_navigator]:   distance remaining: 0.28 m
[INFO] [1793469763.360666857] [basic_navigator]:   distance remaining: 0.26 m
[INFO] [1793469765.372506764] [basic_navigator]:   distance remaining: 0.20 m
[INFO] [1793469765.891373852] [basic_navigator]: Goal 5 reached
```
