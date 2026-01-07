import numpy as np

import rclpy
from rclpy.node import Node

from sensor_msgs.msg import JointState


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
        th0 = msg.position[0]
        th1 = msg.position[1]
        th2 = msg.position[2]

        trans0 = 0.9
        trans1 = 0.7
        trans2 = 0.5
        trans3 = 0.3

        T0 = self.transformation(th0, 0, trans0)
        T1 = self.transformation(th1, 0, trans1)
        T2 = self.transformation(th2, 0, trans2)
        T3 = self.transformation(0, 0, trans3)

        TFinal = T0 @ T1 @ T2 @ T3

        print(TFinal)

    def transformation(self, theta, x, y):
        c = np.cos(theta)
        s = np.sin(theta)
        return np.array([
            [c, -s, x],
            [s,  c, y],
            [0.0, 0.0, 1.0]
        ])

def main(args=None):
    rclpy.init(args=args)
    node = ForwardKinematic()
    rclpy.spin(node)
    rclpy.shutdown()

if __name__ == '__main__':
    main()