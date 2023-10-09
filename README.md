# SVNIT_MLIP

# Capsule Endoscopy

## Evaluation Metrics

 ### Classification Metrics
| Metric (in probability)| Value    |
|------------------------|----------|
| Accuracy               |   0.4937 |
| Recall                 |   0.5753 |
| F1-Score               |   0.661  |


### Detection Metrics
| Metric (in probability)| Value          |
|------------------------|----------------|
| Average Precision      |     0.5081     |
| Mean Average Precision |     0.652      |
| Intersection over Union|     0.4937     |

# Validation Dataset
## Detection and Classification

| **Imagename** | **img- (271).png** | **img- (386).png**|**img- (389).png**|**img- (406).png**|**img- (409).png**|
|------ |---------------------|---------------------|---------------------|---------------------|---------------------|
|**Images** | <img src="Images_README\validation_dataset\classification_and_detection\img- (271).png" alt="Image 1">| <img src="Images_README\validation_dataset\classification_and_detection\img- (386).png" alt="Image 1">|<img src="Images_README\validation_dataset\classification_and_detection\img- (389).png" alt="Image 1">| <img src="Images_README\validation_dataset\classification_and_detection\img- (406).png" alt="Image 1">|<img src="Images_README\validation_dataset\classification_and_detection\img- (409).png" alt="Image 1">|
|**Confidance**| 0.96 | 0.96 |0.96 | 0.96 |0.96 |
                                                                                                         

| **Imagename** | **img- (608).png** | **img- (609).png**|**img- (797).png**|**img- (908).png**|**img- (912).png**|
|------ |---------------------|---------------------|---------------------|---------------------|---------------------|
|**Images** | <img src="Images_README\validation_dataset\classification_and_detection\img- (608).png" alt="Image 1">| <img src="Images_README\validation_dataset\classification_and_detection\img- (609).png" alt="Image 1">|<img src="Images_README\validation_dataset\classification_and_detection\img- (797).png" alt="Image 1">| <img src="Images_README\validation_dataset\classification_and_detection\img- (908).png" alt="Image 1">|<img src="Images_README\validation_dataset\classification_and_detection\img- (912).png" alt="Image 1">|
|**Confidance**| 0.96 | 0.96 |0.97 | 0.97 |0.97 |

## Interpretability Plots (Cam Plots of 2nd last layer)

| **Imagename** | **img- (271).png** | **img- (386).png**|**img- (389).png**|**img- (406).png**|**img- (409).png**|
|------ |---------------------|---------------------|---------------------|---------------------|---------------------|
|**Images** | <img src="Images_README\validation_dataset\interpretability_plots\img- (271)_cam.png" alt="Image 1">| <img src="Images_README\validation_dataset\interpretability_plots\img- (386)_cam.png" alt="Image 1">|<img src="Images_README\validation_dataset\interpretability_plots\img- (389)_cam.png" alt="Image 1">| <img src="Images_README\validation_dataset\interpretability_plots\img- (406)_cam.png" alt="Image 1">|<img src="Images_README\validation_dataset\interpretability_plots\img- (409)_cam.png" alt="Image 1">|
                                                                                                         
| **Imagename** | **img- (608).png** | **img- (609).png**|**img- (797).png**|**img- (908).png**|**img- (912).png**|
|------ |---------------------|---------------------|---------------------|---------------------|---------------------|
|**Images** | <img src="Images_README\validation_dataset\interpretability_plots\img- (608)_cam.png" alt="Image 1">| <img src="Images_README\validation_dataset\interpretability_plots\img- (609)_cam.png" alt="Image 1">|<img src="Images_README\validation_dataset\interpretability_plots\img- (797)_cam.png" alt="Image 1">| <img src="Images_README\validation_dataset\interpretability_plots\img- (908)_cam.png" alt="Image 1">|<img src="Images_README\validation_dataset\interpretability_plots\img- (912)_cam.png" alt="Image 1">|


# Testing Dataset 1
## Detection and Classification

| **Imagename** | **A0001.png** | **A0033.png**|**A0035.png**|**A0040.png**|**A0041.png**|
|------ |---------------------|---------------------|---------------------|---------------------|---------------------|
|**Images** | <img src="Images_README\testing_dataset_1\Classification_and_detection\A0001.png" alt="Image 1">| <img src="Images_README\testing_dataset_1\Classification_and_detection\A0033.png" alt="Image 1">|<img src="Images_README\testing_dataset_1\Classification_and_detection\A0035.png" alt="Image 1">| <img src="Images_README\testing_dataset_1\Classification_and_detection\A0040.png" alt="Image 1">|<img src="Images_README\testing_dataset_1\Classification_and_detection\A0041.png" alt="Image 1">|
|**Confidance**| 0.29 | 0.75 |0.44 | 0.37 | 0.27 |

## Interpretability Plots (Cam Plots of 2nd last layer)                                                                                                         
| **Imagename** | **A0001_cam.png** | **A0033_cam.png**|**A0035_cam.png**|**A0040_cam.png**|**A0041_cam.png**|
|------ |---------------------|---------------------|---------------------|---------------------|---------------------|
|**Images** | <img src="Images_README\testing_dataset_1\Interpretability_plots\A0001_cam.png" alt="Image 1">| <img src="Images_README\testing_dataset_1\Interpretability_plots\A0033_cam.png" alt="Image 1">|<img src="Images_README\testing_dataset_1\Interpretability_plots\A0035_cam.png" alt="Image 1">| <img src="Images_README\testing_dataset_1\Interpretability_plots\A0040_cam.png" alt="Image 1">|<img src="Images_README\testing_dataset_1\Interpretability_plots\A0041_cam.png" alt="Image 1">|

# Testing Dataset 2
## Detection and Classification

| **Imagename** | **A0211.png** | **A0498.png**|**A0500.png**|**A0532.png**|**A0551.png**|
|------ |---------------------|---------------------|---------------------|---------------------|---------------------|
|**Images** | <img src="Images_README\testing_dataset_2\classification_and_detection\A0211.png" alt="Image 1">| <img src="Images_README\testing_dataset_2\classification_and_detection\A0498.png" alt="Image 1">|<img src="Images_README\testing_dataset_2\classification_and_detection\A0500.png" alt="Image 1">| <img src="Images_README\testing_dataset_2\classification_and_detection\A0532.png" alt="Image 1">|<img src="Images_README\testing_dataset_2\classification_and_detection\A0551.png" alt="Image 1">|
|**Confidance**| 0.27 | 0.28 |0.62 | 0.27 |0.32 |

## Interpretability Plots (Cam Plots of 2nd last layer)                                                                                                         
| **Imagename** | **A0211_cam.png** | **A0498_cam.png**|**A0500_cam.png**|**A0532_cam.png**|**A0551_cam.png**|
|------ |---------------------|---------------------|---------------------|---------------------|---------------------|
|**Images** | <img src="Images_README\testing_dataset_2\Interpretability_plots\A0211_cam.png" alt="Image 1">| <img src="Images_README\testing_dataset_2\Interpretability_plots\A0498_cam.png" alt="Image 1">|<img src="Images_README\testing_dataset_2\Interpretability_plots\A0500_cam.png" alt="Image 1">| <img src="Images_README\testing_dataset_2\Interpretability_plots\A0532_cam.png" alt="Image 1">|<img src="Images_README\testing_dataset_2\Interpretability_plots\A0551_cam.png" alt="Image 1">|

# Training Procedure
Using training.ipynb and config.yaml, you can train model using train_model function which takes model destination path (model_path), config.yaml file (config_yaml), epochs(total_epochs), image size (image_size) and device type (device_) as input and trains the model.

**Note:** Please give full path of you dataset in config.yaml instead of giving relative path.

# Prediction procedure
For prediction use function prediction which is present in prediction.ipynb. This function takes the model destination path, test data directory path as input, and returns boundary box parameters as output.
