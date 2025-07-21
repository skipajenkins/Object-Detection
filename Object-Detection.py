import torch
print(torch.__version__)
3#from torch.serialization import add_safe_globals
#from ultralytics.nn.tasks import YOLOv10DetectionModel
#from torch.nn.modules.container import Sequential
import cv2  # Add OpenCV for manual display

# Allowlist all required classes
#add_safe_globals([YOLOv10DetectionModel, Sequential])

from ultralytics import YOLO

# Load model
model = YOLO("yolov10s.pt")

# Run inference
# Uncomment the line below to run inference on a specific image
#results = model("C:/Users/Alucard/Desktop/VisualStudio/Computer Vision/RTOTyolov10VSCode/yolov10/ultralytics/assets/Theboys.jpg")

display_img = results[0].plot()
display_img_resized = cv2.resize(display_img, (1920, 1080))
# Show result manually and wait for key press
cv2.imshow("YOLOv10 Detection", display_img_resized)
cv2.waitKey(0)  # Wait indefinitely until a key is pressed
cv2.destroyAllWindows()

# Save result
results.save()
