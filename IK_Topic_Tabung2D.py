import rclpy
from rclpy.node import Node

from tf2_ros import TransformException
from tf2_ros.buffer import Buffer
from tf2_ros.transform_listener import TransformListener
import numpy as np

class InverseKinematics(Node):
    def __init__(self):
        super().__init__('ik_node')
        self.tf_buffer = Buffer()
        self.tf_listener = TransformListener(self.tf_buffer, self)
        self.timer = self.create_timer(1.0, self.on_timer)

    def on_timer(self):
        base = 'base_link'
        end_effector = 'end_effector'
        try:
            t = self.tf_buffer.lookup_transform(base, end_effector, rclpy.time.Time())
        except TransformException as exc:
            self.get_logger().info(f'Could not transform {base} to {end_effector}: {exc}')
            return 
        
        x_end = t.transform.translation.x
        y_end = t.transform.translation.y
        z_end = t.transform.translation.z - 0.9
        link1 = 0.7
        link2 = 0.5

        X0 = np.sqrt(x_end**2 + y_end**2)
        tetaf1 = np.arctan(z_end / X0)
        a = np.sqrt(z_end**2 + X0**2)
        tetaf2 = np.arccos((link1**2 + a**2 - link2**2)/(2*a*link1))
        teta1 = tetaf1 + tetaf2 - np.radians(90)
        teta2 = np.arccos((link1**2 + link2**2 - a**2)/(2*link2*link1)) - np.radians(180)      

        print(
            f'\nEnd Effector Position: X = {x_end:.3f}, Y = {y_end:.3f}, Z = {z_end+0.9:.3f}'
            f'\ntheta1 = {teta1:.3f} | {np.degrees(teta1):.3f}, theta2 = {teta2:.3f} | {np.degrees(teta2):.3f}'
        )
        
def main(args=None):
    rclpy.init(args=args)
    node = InverseKinematics()
    rclpy.spin(node)
    rclpy.shutdown()

if __name__ == '__main__':
    main()