import rclpy
from rclpy.node import Node
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
