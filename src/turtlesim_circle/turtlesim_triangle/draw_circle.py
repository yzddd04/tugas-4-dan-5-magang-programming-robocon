import rclpy
from rclpy.node import Node
from turtlesim.srv import TeleportAbsolute
import math
import time

class CircleDrawer(Node):
    def __init__(self):
        super().__init__('circle_drawer')
        
        # Buat klien untuk teleportasi
        self.client = self.create_client(TeleportAbsolute, 'turtle1/teleport_absolute')
        while not self.client.wait_for_service(timeout_sec=1.0):
            self.get_logger().info('Service not available, waiting again...')
        
        # Gambar lingkaran
        self.draw_circle()

    def teleport(self, x, y, theta):
        req = TeleportAbsolute.Request()
        req.x = x
        req.y = y
        req.theta = theta
        self.client.call_async(req)

    def draw_circle(self):
        # Koordinat pusat lingkaran
        center_x = 5.5
        center_y = 5.5
        radius = 4.0  # Radius lingkaran
        
        # Menggambar lingkaran
        for angle in range(0, 360):
            radian = math.radians(angle)  # Konversi derajat ke radian
            x = center_x + radius * math.cos(radian)  # Hitung koordinat x
            y = center_y + radius * math.sin(radian)  # Hitung koordinat y
            self.teleport(x, y, radian)  # Teleportasi turtle ke titik baru
            time.sleep(0.01)  # Tunggu sebentar sebelum teleportasi berikutnya

def main(args=None):
    rclpy.init(args=args)
    circle_drawer = CircleDrawer()
    rclpy.spin(circle_drawer)
    circle_drawer.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
