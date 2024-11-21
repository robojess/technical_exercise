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

    1. What are the key components and services that you would include in this system? Consider aspects such as data collection, processing, storage, as well as user interaction and alerts.

    2. Consider the trade-offs between processing data on the devices versus in the cloud. How would you decide which types of tasks to perform locally and which to handle on the device?

"""

"""
Developers are tasked with adding the feature for overlaying accessories on the cats when they are detected.  Below is an example implementation of this feature.
"""

def overlay_accessory_with_detection(image_path):
    # Detect cat
    image = cv2.imread('/dev/image_test.jpg')
    if image is None:
        raise ValueError("Image not found or unable to open")

    # Image processing for model
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    edges = cv2.Canny(gray, 100, 200)
    feature_sum = edges.sum()
    average_intensity = 0.5
    ... 

    detected_object = model_detection(image, feature_sum, average_intensity)

    # Add Accessory
    x,y,w,h = detected_object.coords

    accessory_height = h // 2
    accessory_width = w

    draw.rectangle([x, y - accessory_height, x + accessory_width, y], image="black_top_hat.jpg")

    # Save the modified image
    img.save("output_with_accessory.jpg")
    print("Accessory overlaid and image saved as output_with_accessory.jpg")

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

            # Overlay accessories
            overlay_accessory_with_detection("cat_image.jpg")

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
