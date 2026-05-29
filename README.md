# Car_Evaluation-_Dataset
This is a repository of car_evaluation

Car Evaluation Prediction 🚗

A Machine Learning project that predicts the evaluation category of a car based on different features such as buying price, maintenance cost, doors, seating capacity, luggage boot size, and safety.

📌 Project Overview

The Car Evaluation Prediction System uses Machine Learning algorithms to classify cars into categories like:

unacc → Unacceptable
acc → Acceptable
good → Good
vgood → Very Good

The model is trained using the Car Evaluation dataset and helps understand classification problems in Machine Learning.

📂 Dataset Information

Dataset Features:

Feature	Description
buying	Buying price
maint	Maintenance cost
doors	Number of doors
persons	Capacity in terms of persons
lug_boot	Luggage boot size
safety	Safety level

Target Variable:

class
🛠️ Technologies Used
Python
Pandas
NumPy
Matplotlib
Seaborn
Scikit-learn
📊 Machine Learning Workflow
Import Dataset
Data Preprocessing
Handle Missing Values
Encode Categorical Data
Split Dataset into Train & Test
Train Machine Learning Model
Evaluate Accuracy
Predict Car Evaluation Class
🤖 Algorithms Used
Decision Tree Classifier
Support Vector Classifier (SVC)
Random Forest Classifier
📈 Model Evaluation

Evaluation metrics used:

Accuracy Score
Confusion Matrix
Classification Report

Example:

from sklearn.metrics import accuracy_score

accuracy = accuracy_score(y_test, y_pred)
print("Accuracy :", accuracy)
📦 Installation

Install required libraries using:

pip install pandas numpy matplotlib seaborn scikit-learn
▶️ How to Run
Clone the repository
git clone <your-repository-link>
Open project folder
cd car_evaluation
Run the Python file
python app.py
📁 Project Structure
car_evaluation/
│
├── dataset.csv
├── car_evaluation.ipynb
├── app.py
├── requirements.txt
└── README.md
📷 Sample Prediction

Input:

buying = 'low'
maint = 'low'
doors = '4'
persons = '4'
lug_boot = 'big'
safety = 'high'

Output:

good
🚀 Future Improvements
Deploy using Streamlit or Flask
Add GUI Interface
Improve model accuracy
Add real-time prediction system
👨‍💻 Author

Raj Sing

Machine Learning & Data Science Enthusiast

⭐ Conclusion

This project is a beginner-friendly Machine Learning classification project that helps in understanding:

Data preprocessing
Feature encoding
Classification algorithms
Model evaluation techniques
