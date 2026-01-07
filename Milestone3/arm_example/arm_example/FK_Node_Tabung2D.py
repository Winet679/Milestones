import rclpy
from rclpy.node import Node
import numpy as np
from sensor_msgs.msg import JointState
from FK_Tabung2D import forward_kinematics

class ForwardKinematic(Node):
    def __init__(self):
        super().__init__('fk_node')

        self.joint_state_subscription = self.create_subscription(
            JointState,
            '/joint_states',
            self.callback,
            1
        )

    def callback(self, msg):
        result = forward_kinematics(msg.position[0],
                                    msg.position[1],
                                    msg.position[2])

        print(result)

def main(args=None):
    rclpy.init(args=args)
    node = ForwardKinematic()
    rclpy.spin(node)
    rclpy.shutdown()

if __name__ == '__main__':
    main()


# link1 = 9
# link2 = 7
# link3 = 5
# teta1 = 1.57079632679 # dalam radian - 90 derajat
# teta2 = 1.57079632679
# teta3 = 1.57079632679

# T_03 = np.array([[np.cos(teta1)*np.cos(teta2+teta3), -np.cos(teta1)*np.cos(teta2+teta3), np.sin(teta1), np.cos(teta1)*((link3*np.cos(teta2+teta3))+(link2*np.cos(teta2)))],
#                  [np.sin(teta1)*np.cos(teta2+teta3), -np.sin(teta1)*np.cos(teta2+teta3), -np.cos(teta1), np.sin(teta1)*((link3*np.cos(teta2+teta3))+(link2*np.cos(teta2)))],
#                  [np.sin(teta2+teta3), np.cos(teta2+teta3), 0, (link3*np.sin(teta2+teta3))+(link2*np.sin(teta2))],
#                  [0, 0, 0, 1]])

# print(T_03[0:3, 3])

'''
Docstring for arm_example.FK
DH-Parameter
ai = jarak Z(i-1) ke Z(i) dilihat dari Xi (panjang link)
alpha_i = sudut antara Z(i-1) dan Z(i) dilihat dari Xi 
di = jarak X(i-1) ke X(i) dilihat dari Zi
teta_i = sudut antara X(i-1) dan X(i) dilihat dari Zi
file:///home/winet/Downloads/aaltahtawi,+139-150%20(1).pdf
'''