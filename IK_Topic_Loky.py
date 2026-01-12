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
        z_end = t.transform.translation.z + 0.45
        link1 = 0.25 #coxa
        link2 = 0.55 #femur
        link3 = -0.7129 #tibia

        X0 = np.sqrt(x_end**2 + y_end**2)
        tetaf1 = -np.arctan(z_end / (X0-link1))
        a = np.sqrt(z_end**2 + (X0-link1)**2)
        tetaf2 = -np.arccos((link2**2 + a**2 - link3**2)/(2*a*link2))
        
        teta1 = np.arctan(y_end/x_end)
        teta2 = tetaf1 + tetaf2
        teta3 = np.arccos((link2**2 + link3**2 - a**2)/(2*link3*link2)) - np.radians(90)      

        print(
            f'\nEnd Effector Position: X = {x_end:.3f}, Y = {y_end:.3f}, Z = {z_end-0.45:.3f}'
            f'\ntheta1 = {teta1:.3f} | {np.degrees(teta1):.3f}, theta2 = {teta2:.3f} | {np.degrees(teta2):.3f}, theta3 = {teta3:.3f} | {np.degrees(teta3):.3f}'
        )
        
def main(args=None):
    rclpy.init(args=args)
    node = InverseKinematics()
    rclpy.spin(node)
    rclpy.shutdown()

if __name__ == '__main__':
    main()