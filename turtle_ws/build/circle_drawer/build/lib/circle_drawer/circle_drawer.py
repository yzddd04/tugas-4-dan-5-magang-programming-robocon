import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist

class CircleDrawer(Node):
    def __init__(self):
        super().__init__('circle_drawer')
        self.publisher_ = self.create_publisher(Twist, '/turtle1/cmd_vel', 10)
        timer_period = 0.1  # seconds
        self.timer = self.create_timer(timer_period, self.move_in_circle)
        self.get_logger().info("CircleDrawer node has been started.")
        
    def move_in_circle(self):
        msg = Twist()
        msg.linear.x = 1.0  # Adjust speed as desired
        msg.angular.z = 1.0  # Set angular speed to create a circle
        self.publisher_.publish(msg)

def main(args=None):
    rclpy.init(args=args)
    circle_drawer = CircleDrawer()
    rclpy.spin(circle_drawer)
    circle_drawer.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()

