import torch

# Model
model = torch.hub.load("ultralytics/yolov5", "yolov5x6")  # or yolov5n - yolov5x6, custom

# Images
img = "https://assets.epicurious.com/photos/54c7b962e231becc7f3df473/1:1/w_1920,c_limit/51261040_marinated-skirt-steak_1x1.jpg"  # or file, Path, PIL, OpenCV, numpy, list

# Inference
results = model(img)

# Results
results.show()  # or .show(), .save(), .crop(), .pandas(), etc.
