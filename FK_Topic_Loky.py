import numpy as np

import rclpy
from rclpy.node import Node

from sensor_msgs.msg import JointState


class ForwardKinematic(Node):
    def __init__(self):
        super().__init__('loky_node')

        self.joint_state_subscription = self.create_subscription(
            JointState,
            '/joint_states',
            self.callback,
            1
        )

    def callback(self, msg):
        th0 = msg.position[0]
        th1 = msg.position[1]
        th2 = msg.position[2]

        trans0 = -0.45
        trans1 = 0.25
        trans2 = 0.55
        trans3 = -0.7129

        T0 = self.homogeneus_transform_matrix_z(0, 0, trans0, th0)
        T1 = self.homogeneus_transform_matrix_y(trans1, 0, 0, th1)
        T2 = self.homogeneus_transform_matrix_y(trans2, 0, 0, th2)
        T3 = self.homogeneus_transform_matrix_y(0, 0, trans3, 0)

        TFinal = T0 @ T1 @ T2 @ T3

        print(TFinal)

    def homogeneus_transform_matrix_z(self, x, y, z, theta):
        c, s = np.cos(theta), np.sin(theta)
        return np.array([[c, -s, 0, x],
                        [s, c, 0, y],
                        [0, 0, 1, z],
                        [0, 0, 0, 1]])

    def homogeneus_transform_matrix_y(self, x, y, z, theta):
        c, s = np.cos(theta), np.sin(theta)
        return np.array([[c, 0, s, x],
                        [0, 1, 0, y],
                        [-s, 0, c, z],
                        [0, 0, 0, 1]])

def main(args=None):
    rclpy.init(args=args)
    node = ForwardKinematic()
    rclpy.spin(node)
    rclpy.shutdown()

if __name__ == '__main__':
    main()