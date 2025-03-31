# Predictive Maintenance for Industrial Machines

## Introduction
Predictive maintenance is a crucial approach in industrial settings to minimize unexpected machine failures and reduce downtime. Traditional maintenance methods—corrective (reactive) and preventive—often lead to either high repair costs or unnecessary maintenance actions. This project leverages **machine learning techniques** to predict potential failures based on operational data, helping industries optimize maintenance schedules and prevent costly downtimes.

## Features
- **Automated Failure Prediction**: Uses machine learning models to detect potential failures before they occur.
- **Data Preprocessing & Cleaning**: Handles outliers, encodes categorical variables, and converts temperature readings.
- **Machine Learning Models**: Evaluates multiple models to determine the most accurate approach.
- **Hyperparameter Tuning**: Optimizes models for better performance.
- **Visual Analysis & Reporting**: Provides insights into failure patterns and model performance.

## Dataset
The dataset contains **10,000 instances** with **14 features**, capturing various operational parameters of industrial machines, such as:
- Air Temperature
- Process Temperature
- Rotational Speed
- Torque
- Tool Wear

The target variable, **Failure Type**, indicates whether a machine failure occurred.

## Methodology
### 1. Data Preprocessing
- Removed irrelevant columns (UDI, Product ID) to reduce noise.
- Converted temperature values from Kelvin to Celsius for better interpretability.
- Detected and managed outliers using the **Interquartile Range (IQR) method**.
- Encoded categorical variables using **ordinal encoding**.

### 2. Data Splitting
- **Training Set**: 80% of the data
- **Testing Set**: 20% of the data

### 3. Machine Learning Models
We evaluated the following models for failure prediction:
- **Logistic Regression**
- **K-Nearest Neighbors (KNN)**
- **Random Forest Classifier**
- **Decision Tree Classifier**

### 4. Model Evaluation
Each model was trained and tested to measure its accuracy. Hyperparameter tuning was performed using **Grid Search** to improve results.

#### Initial Accuracy Scores
| Model                 | Accuracy Before Tuning |
|-----------------------|----------------------|
| Random Forest        | 97.99%               |
| Decision Tree        | 97.29%               |
| K-Nearest Neighbors  | 96.09%               |
| Logistic Regression  | 96.09%               |

#### After Hyperparameter Tuning
| Model                 | Best Parameters | Accuracy After Tuning |
|-----------------------|----------------|----------------------|
| **Random Forest**     | n_estimators=300, min_samples_split=2, max_depth=None | **98.19%** |
| Decision Tree        | min_samples_split=10, min_samples_leaf=2, criterion='gini' | 97.84% |
| K-Nearest Neighbors  | weights='distance', n_neighbors=12 | 96.39% |
| Logistic Regression  | solver='liblinear', penalty='l1', C=1438.4 | 96.59% |

### 5. Best Model Selection
The **Random Forest Classifier** achieved the highest accuracy (**98.19%**) and was selected for implementation.

## Results & Insights
- **Hyperparameter tuning improved all models**, with Random Forest achieving the best accuracy.
- **Predictive maintenance reduces unexpected downtime** and enhances machine efficiency.
- **Feature engineering and preprocessing significantly impacted model performance.**

## Future Enhancements
- **Real-Time Deployment**: Integrate the model into an industrial monitoring system for real-time failure prediction.
- **Deep Learning Methods**: Apply advanced deep learning techniques to further enhance predictive accuracy.
- **Generalization**: Adapt the model to larger datasets and more complex failure types.

## Conclusion
This project demonstrates the potential of **machine learning for predictive maintenance**, helping industries prevent failures and optimize maintenance schedules. By leveraging operational data, we can **enhance machine reliability, reduce costs, and improve overall efficiency**.

---
### How to Run the Project
1. **Install dependencies**:
   ```sh
   pip install -r requirements.txt
   ```
2. **Run the script**:
   ```sh
   python app.py
   ```
3. **Use the web dashboard** (if applicable) to visualize maintenance insights.


