import cv2
from mtcnn import MTCNN

# Initialize MTCNN face detector
detector = MTCNN()

# Load the image
image_path = r"C:\\Users\\HP\\OneDrive\\Pictures\\id\\sample1.jpg"  # Replace with your image file path
image = cv2.imread(image_path)

# Detect faces
results = detector.detect_faces(image)

# Draw bounding boxes
for result in results:
    x, y, width, height = result['box']
    cv2.rectangle(image, (x, y), (x + width, y + height), (255, 0, 0), 2)

# Display the image with detected faces
cv2.imshow('Detected Faces', image)

# Wait until a key is pressed, then close the window
cv2.waitKey(0)
cv2.destroyAllWindows()
