# SVNIT_MLIP

# Capsule Endoscopy

## Evaluation Metrics

 ### Classification Metrics
| Metric      | Value    |
|-------------|----------|
| Accuracy    |   0.4937   |
| Recall      |   0.5753   |
| F1-Score    |   0.661 |


### Detection Metrics
| Metric                 | Value          |
|------------------------|----------------|
| Average Precision      |       0.5081         |
| Mean Average Precision |     0.652       |
| Intersection over Union|     0.4937   |

## In Validation Dataset

### Classification and Detection 

1. img- (271).png <br/>
   <img src="Images_README/validation_dataset/classification_and_detection/img- (271).png" alt="Image 1" width="350" height="350"><br/> 
   Confidence: 

2. img- (386).png <br/>
   <img src="Images_README/validation_dataset/classification_and_detection/img- (386).png" alt="Image 1" width="350" height="350"><br/> 
   Confidence: 

3. img- (389).png <br/>
   <img src="Images_README/validation_dataset/classification_and_detection/img- (389).png" alt="Image 1" width="350" height="350"><br/> 
   Confidence: 

4. img- (406).png <br/>
   <img src="Images_README/validation_dataset/classification_and_detection/img- (406).png" alt="Image 1" width="350" height="350"><br/> 
   Confidence: 

5. img- (409).png <br/>
   <img src="Images_README/validation_dataset/classification_and_detection/img- (409).png" alt="Image 1" width="350" height="350"><br/> 
   Confidence: 

6. img- (608).png <br/>
   <img src="Images_README/validation_dataset/classification_and_detection/img- (608).png" alt="Image 1" width="350" height="350"><br/> 
   Confidence: 

7. img- (609).png <br/>
   <img src="Images_README/validation_dataset/classification_and_detection/img- (609).png" alt="Image 1" width="350" height="350"><br/> 
   Confidence: 

8. img- (797).png <br/>
   <img src="Images_README/validation_dataset/classification_and_detection/img- (797).png" alt="Image 1" width="350" height="350"><br/> 
   Confidence: 

9. img- (908).png <br/>
   <img src="Images_README/validation_dataset/classification_and_detection/img- (908).png" alt="Image 1" width="350" height="350"><br/> 
   Confidence: 

10. img- (912).png <br/>
   <img src="Images_README/validation_dataset/classification_and_detection/img- (912).png" alt="Image 1" width="350" height="350"><br/> 
   Confidence:

### Interpretability Plots 

1. Confusion Matrix <br/>
   <img src="Images_README/validation_dataset/interpretability_plots/confusion_matrix.png" alt="Image 1" width="400" height="300"><br/>

2. Normalized Confusion Matrix <br/>
   <img src="Images_README/validation_dataset/interpretability_plots/confusion_matrix_normalized.png" alt="Image 1" width="400" height="300"><br/>

3. P curve <br/>
   <img src="Images_README/validation_dataset/interpretability_plots/P_curve.png" alt="Image 1" width="400" height="300"><br/>

4. PR curve <br/>
   <img src="Images_README/validation_dataset/interpretability_plots/PR_curve.png" alt="Image 1" width="400" height="300"><br/>

5. R curve <br/>
   <img src="Images_README/validation_dataset/interpretability_plots/R_curve.png" alt="Image 1" width="400" height="300"><br/>

## In Testing Dataset 1

### Classification and Detection 

1. A0001 <br/>
   <img src="Images_README/testing_dataset_1/Classification_and_detection/A0001.png" alt="Image 1" width="350" height="350"><br/> 
   Confidence: 0.29

2. A0033 <br/>
   <img src="Images_README/testing_dataset_1/Classification_and_detection/A0033.png" alt="Image 1" width="350" height="350"><br/> 
   Confidence: 0.75

3. A0035 <br/>
   <img src="Images_README/testing_dataset_1/Classification_and_detection/A0035.png" alt="Image 1" width="350" height="350"><br/> 
   Confidence: 0.44

4. A0040 <br/>
   <img src="Images_README/testing_dataset_1/Classification_and_detection/A0040.png" alt="Image 1" width="350" height="350"><br/> 
   Confidence: 0.37

5. A0041 <br/>
   <img src="Images_README/testing_dataset_1/Classification_and_detection/A0041.png" alt="Image 1" width="350" height="350"><br/> 
   Confidence: 

### Interpretability Plots (Cam Plots)

1. A0041 <br/>
   <img src="Images_README/testing_dataset_1/Interpretability_plots/A0001_cam.png" alt="Image 1" width="350" height="350"><br/> 

2. A0041 <br/>
   <img src="Images_README/testing_dataset_1/Interpretability_plots/A0041_cam.png" alt="Image 1" width="350" height="350"><br/> 

## In Testing Dataset 2

### Classification and Detection

1. A0211 <br/>
   <img src="Images_README/testing_dataset_2/classification_and_detection/A0211.png" alt="Image 1" width="350" height="350"><br/> 
   Confidence: 0.27

2. A0498 <br/>
   <img src="Images_README/testing_dataset_2/classification_and_detection/A0498.png" alt="Image 1" width="350" height="350"><br/> 
   Confidence: 0.28

3. A0500 <br/>
   <img src="Images_README/testing_dataset_2/classification_and_detection/A0500.png" alt="Image 1" width="350" height="350"><br/> 
   Confidence: 0.62

4. A0532 <br/>
   <img src="Images_README/testing_dataset_2/classification_and_detection/A0532.png" alt="Image 1" width="350" height="350"><br/> 
   Confidence: 0.27

5. A0551 <br/>
   <img src="Images_README/testing_dataset_2/classification_and_detection/A0551.png" alt="Image 1" width="350" height="350"><br/> 
   Confidence: 0.32

### Interpretability Plots (Cam Plots)

1. A0500 <br/>
   <img src="Images_README/testing_dataset_2/Interpretability_plots/A0500_cam.png" alt="Image 1" width="350" height="350"><br/> 

2. A0532 <br/>
   <img src="Images_README/testing_dataset_2/Interpretability_plots/A0532_cam.png" alt="Image 1" width="350" height="350"><br/> 

# Training Procedure
Using training.py and config.yaml, you can train model using train_model function which takes model destination path (model_path), config.yaml file (config_yaml), epochs(total_epochs), image size (image_size) and device type (device_) as input and trains the model.

# Prediction procedure
For prediction use function prediction which is present in prediction.py. This function takes the model destination path, test data directory path as input, and returns boundary box parameters as output.
