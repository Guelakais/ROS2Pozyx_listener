import serial
import rclpy
from rclpy.node import Node
from std_msgs.msg import String

class pozyx_listener(Node):
    serialport
    def __init__(self):
        super().__init__('pozyx_listener')
        serialPort = serial.Serial(
        port = "/dev/ttyUSB1", baudrate=115200
        )

        self.publisher_ = self.create_publisher(String, 'topic', 10)
        timer_period = 0.5  # seconds
        self.timer = self.create_timer(timer_period, self.timer_callback)
        self.i = 0

    def timer_callback(self):
        data = serialPort.readline().decode().strip()
        msg = String()
        msg.data = 'Position Data: %d' % serialPort.readline().decode().strip()
        self.publisher_.publish(msg)
        self.get_logger().info('Publishing: "%s"' % msg.data)
        self.i += 1
    def getData()



def main(args=None):
    rclpy.init(args=args)

    minimal_publisher = MinimalPublisher()

    rclpy.spin(minimal_publisher)

    # Destroy the node explicitly
    # (optional - otherwise it will be done automatically
    # when the garbage collector destroys the node object)
    minimal_publisher.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()
