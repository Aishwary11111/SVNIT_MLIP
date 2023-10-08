from ultralytics import YOLO

# Function to train the model
def train_model(model_path="detection_model.pt", config_yaml, total_epochs, image_size, device_):
    detection_model = YOLO(model_path) 
    detection_model.train(data=config_yaml, epochs=total_epochs, imgsz=image_size, device=device_)
    return detection_model


