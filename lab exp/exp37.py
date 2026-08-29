import cv2
import numpy as np

def subtract_foreground(image_path, lower_color, upper_color):

    # Read the image
    image = cv2.imread(image_path)

    if image is None:
        print("Image could not be loaded.")
        return

    # Convert to HSV color space
    hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

    # Define lower and upper range
    lower_bound = np.array(lower_color, dtype=np.uint8)
    upper_bound = np.array(upper_color, dtype=np.uint8)

    # Create mask
    foreground_mask = cv2.inRange(hsv, lower_bound, upper_bound)

    # Extract foreground
    foreground = cv2.bitwise_and(image, image, mask=foreground_mask)

    # Display results
    cv2.imshow("Original Image", image)
    cv2.imshow("Foreground", foreground)

    cv2.waitKey(0)
    cv2.destroyAllWindows()


# Image path
image_path = r"C:\Users\archu\OneDrive\Pictures\Camera Roll\moonlight.png"

# HSV color range
lower_color = [0, 50, 50]
upper_color = [120, 255, 255]

# Run the program
subtract_foreground(image_path, lower_color, upper_color)
