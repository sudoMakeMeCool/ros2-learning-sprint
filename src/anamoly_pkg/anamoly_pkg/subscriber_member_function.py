import rclpy
from rclpy.node import Node
from std_msgs.msg import String

class SensorListener(Node):
    def __init__(self):
        super().__init__('sensor_listener')
        self.subscription = self.create_subscription(
            String, 
            'sensor_data', 
            self.listener_callback, 
            10
        )

    def listener_callback(self, msg):
        self.get_logger().info(f'I heard {msg.data}')
        if "21" in msg.data:
            self.get_logger().warn('Anamoly Detected!')

def main(args=None):
    rclpy.init(args=args)
    sensorListener = SensorListener()
    rclpy.spin(sensorListener)

    sensorListener.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()  