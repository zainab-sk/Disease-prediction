# 🏥 Disease Prediction System using Machine Learning  

This project is an **AI-powered Disease Prediction System** that assists in early detection of **Diabetes, Heart Disease, and Parkinson’s Disease**. It leverages **Machine Learning (ML)** models to analyze medical parameters and provide real-time health risk assessments.  

## 🚀 Project Overview  
This system enables users to input basic medical data, which is then analyzed using ML models to predict the likelihood of certain diseases.  

### 🔹 Features  
- ✅ Predicts the risk of **Diabetes, Heart Disease, and Parkinson’s Disease**  
- ✅ Uses **Tomek Links** to handle imbalanced datasets  
- ✅ Implements **multiple ML models** for improved accuracy  
- ✅ Provides **real-time predictions**  
- ✅ **User-friendly** web interface built with **Streamlit**  

## 🔹 Technologies Used  
- **Python**  
- **Machine Learning Models:**  
  - **Diabetes Prediction:** Support Vector Machine (SVM)  
  - **Heart Disease Prediction:** Random Forest Classifier & Logistic Regression 
  - **Parkinson’s Disease Prediction:** SVM, Decision Trees & **Tomek Links** (for handling imbalanced datasets)  
- **Pandas, NumPy, Scikit-learn** (for data preprocessing & model training)  
- **Streamlit** (for web application)  
- **Pickle** (for saving and loading ML models)  

## 📂 Project Structure  
Disease Prediction/ │-- Dataset/</br>
│ ├── diabetes.csv</br>
│ ├── heart.csv</br>
│ ├── parkinsons.csv</br>
│-- training_model/</br>
│ ├── diabetes.ipynb</br>
│ ├── heart.ipynb</br>
│ ├── parkinsons.ipynb</br>
│ ├── diabetes_model.sav</br>
│ ├── heart_model.sav</br>
│ ├── parkinsons_model.sav</br>
│-- .gitignore</br>
│-- requirements.txt</br>
│-- web.py</br> 

## 📸 Project Snippets 
#### 1. Diabetes Prediction
![d](https://github.com/user-attachments/assets/1d7b9374-9756-4cf1-b826-2b5e14d773b6)

#### 2. Heart Disease Prediction
![h](https://github.com/user-attachments/assets/ed2c1766-0e78-4fe5-9ddd-dcb1c8f7d72e)

#### 3. Parkinson Prediction
![p](https://github.com/user-attachments/assets/011491ce-f9e7-43c4-b533-b37be5ee6bb0)

## 🔧 Installation & Setup  
Follow these steps to download and run the project:  

### 1️⃣ Clone the Repository  
```bash
git clone https://github.com/zainab-sk/Disease-prediction.git
cd disease-prediction
```
2️⃣ Create a Virtual Environment
```bash
python -m venv venv
source venv/bin/activate  # On macOS/Linux
venv\Scripts\activate     # On Windows
```
3️⃣ Install Dependencies
```bash
pip install -r requirements.txt
```
4️⃣ Run the Web App
```bash
streamlit run web.py
```
🌐 Live Demo</br>
🔗 Check out the live website here: https://disease-prediction00.streamlit.app/










