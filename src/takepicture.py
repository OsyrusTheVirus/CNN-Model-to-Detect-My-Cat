#!/usr/bin/python3
from picamera2 import Picamera2
from datetime import datetime
import os
import time

def main() -> None:
    # set up directories
    dataset_path = os.path.expanduser(os.getcwd() + "/cat-dataset")
    labels = {"c": "my-cat", "n": "not-my-cat"}
    for name in labels.values():
        os.makedirs(os.path.join(dataset_path, name), exist_ok=True)
    
    # set up camera
    camera = Picamera2()
    camera.configure(camera.create_still_configuration(main={"size": (640, 640)}))
    camera.start()
    time.sleep(2)
    
    # start taking pictures
    try:
        print("c for cat in photo, n for no cat in photo, q to quit")
        while True:
            
            # get choice
            choice = input("").strip().lower()
            if choice == "q":
                break
            if choice not in labels:
                print("Please type c, n, or q")
                continue
            label = labels[choice]
            
            # store photo
            filename = datetime.now().strftime("%Y-%m-%d_%H:%M:%S_%f") + ".jpg"
            folder_path = os.path.join(dataset_path, label, filename)
            camera.capture_file(folder_path)
            count = len(os.listdir(os.path.join(dataset_path, label)))
            print(f"Saved to {label} ({count} photos in this folder)")
            
    finally:
        # stop camera 
        camera.stop()
        print("Camera stopped. Photos in cat-dataset")


if __name__ == "__main__":
    main()