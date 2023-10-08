from ultralytics import YOLO
import pandas as pd

# Function to train the model
def prediction(model_path="detection_model.pt", test_data_directory, show_images_while_prediction=False, save_results=True, iou=0.5):
    detection_model = YOLO(model_path)
    
    result_df = pd.DataFrame(columns=["Image Name", "Predicted Class", "Classification Confidence Level", "Bounding Box Location", "Detection Confidence Level"])
    
    if save_results:
        for root, dirs, files in os.walk(test_data_directory):
            for file in files:
                path = root + file
        
                # Initialising Result Row
                res_row = [file]
                res_row.append("")
                
                detection_result = detection_model(path,iou=iou, show=show_images_while_prediction)
                detection_boxes = detection_result[0].boxes
                
                predicted_boxes = []
                confidence_for_all_boxes = []
        
                if detection_boxes:
                    for box in detection_boxes:
                        predicted_bounding_box = box.xyxy.flatten().tolist() # Predicted bounding box
                        box_confidence_score = box.conf.item()  # Prediction confidence score
                        predicted_boxes.append(predicted_bounding_box)
                        confidence_for_all_boxes.append(box_confidence_score)
                    res_row.append("Bleeding")
                    res_row.append(predicted_boxes)
                    res_row.append(confidence_for_all_boxes)
                else:
                    res_row.append("Non Bleeding")
                    res_row.append("")
                    res_row.append("")
                    
                result_df.loc[len(result_df)] = res_row
            
            result_df.to_csv("prediction_results.csv")
        
