from PIL import Image, ImageDraw
import cv2
import threading

from image_tools import model_detection, logger

"""
    Imagine you are tasked with designing a system for a network of IoT pet cameras. 
    These cameras are installed in homes to monitor pets when their owners are away. 
    The primary feature of these cameras is to detect when a cat is in the camera's 
    view and overlay a virtual accessory, like a top hat, on the cat in real-time as 
    well as provide metrics on various things like how often the cat is detected, etc. 
    The system should also provide owners with a live video feed and send alerts 
    when a cat is detected. The system should be scalable and should be able to operate efficiently.

    General Architecture Questions:

    1. What are the key components and services that you would include in this system? 
    Consider aspects such as data collection, processing, storage, as well as user interaction and alerts.

    2. Consider the trade-offs between processing data on the devices versus in the cloud. 
    How would you decide which types of tasks to perform locally and which to handle on the device?

"""

def process_frame(image_path):
    time.sleep(0.1)
    logger.info("Image processing complete.")

def main():
    cam = cv2.VideoCapture(0)
    if not cam.isOpened():
        logger.error("Error: Could not open camera.")
        return

    ...

    try:
        while camera_on:
            ret, frame = cam.read()
            if not ret:
                print("Error: Could not read frame.")
                break

            # Process and Display
            processed_frame = process_frame(frame)

            # Collect metrics and upload data
            collect_metrics(processed_frame)
            threading.Thread(target=upload_data).start()
            
            # Display the frame
            cv2.imshow('Camera Feed', processed_frame)

            if STOP:
                break
    finally:
        cam.release()
        cv2.destroyAllWindows()

if __name__ == '__main__':
    main()
