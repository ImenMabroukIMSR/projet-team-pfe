import sys
from roboflow import Roboflow
import rclpy
from rclpy.node import Node
from std_msgs.msg import String
from sensor_msgs.msg import Image
from cv_bridge import CvBridge
import cv2
import numpy as np

class RoboflowNode(Node):

    def __init__(self):
        super().__init__('roboflow_node')

        # Remplacez par votre clé API Roboflow
        self.client = Roboflow(api_key="VlfWvA372gxPhEKHtqTp")  
        
        # Remplacez par votre workspace et projet
        self.model = self.client.workspace("siabar").project("ppe-dataset-for-workplace-safety").version(1).model
        
        # Publication des résultats de prédiction
        self.publisher = self.create_publisher(String, 'roboflow_predictions', 10)
        self.get_logger().info("Roboflow Node Started!")

        # Souscription à l'image
        self.bridge = CvBridge()
        self.subscription = self.create_subscription(
            Image,
            '/oakd/rgb/preview/image_raw',  # Nom du topic pour les images
            self.listener_callback,
            10)
        self.subscription

    def listener_callback(self, msg):
        # Convertir l'image ROS en format OpenCV
        cv_image = self.bridge.imgmsg_to_cv2(msg, "bgr8")

        # Sauvegarder l'image pour la prédiction
        filename = "/tmp/input_image.jpg"
        cv2.imwrite(filename, cv_image)

        # Effectuer la prédiction avec Roboflow
        predictions = self.model.predict(filename, confidence=40, overlap=30).json()
        self.get_logger().info(f"Roboflow predictions: {predictions}")


        # Extraire les résultats de la prédiction et les publier
        prediction_text = "Predictions:\n"
        for prediction in predictions['predictions']:
            category = prediction['class']
            confidence = prediction['confidence']
            prediction_text += f"Category: {category}, Confidence: {confidence:.2f}\n"

        # Publier les résultats sous forme de message String
        self.publisher.publish(String(data=prediction_text))
        self.get_logger().info("Published prediction results")

def main(args=None):
    rclpy.init(args=args)
    roboflow_node = RoboflowNode()
    rclpy.spin(roboflow_node)
    roboflow_node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
