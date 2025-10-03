# Reddit-Comments-Sentiment-Analysis

This project provides a simple **Flask-based REST API** that predicts the sentiment of a given text (negative, neutral, or positive).  
The model uses **TF-IDF vectorization** and a classifier trained on labeled Reddit comments.

---

##  Project Overview

This project analyzes text input (such as Reddit comments) and classifies it into three categories: **negative**, **neutral**, or **positive** sentiment.  
It provides an easy-to-use API endpoint (`/predict`) that returns both the predicted label and probability scores for each sentiment class.

- Helps in **sentiment analysis** of user-generated content like Reddit comments, reviews, or tweets.  
- Can be integrated into applications for **content moderation**, **user feedback analysis**, or **opinion mining**.  
- Provides a **ready-to-use API** so developers don’t need to retrain models from scratch.

### 🔹 How users can get started with the project
1. Clone the repository and install dependencies.  
2. Start the Flask server with `python app.py`.  
3. Send a `POST` request to `http://127.0.0.1:5000/predict` with JSON body:  
   ```json
   { "text": "Your message here" }
   ```  
4. The API will return the predicted sentiment along with probabilities.

### 🔹 Where users can get help with your project
- Check the **README.md** for setup instructions.  
- Open an **issue** on the GitHub repository.  
- Contact the maintainer via the provided email in the repository.

### 🔹 Who maintains and contributes to the project
This project is maintained by **Tiba**.  
Contributions are welcome via pull requests. Anyone interested in improving the model, adding new features, or extending the dataset is encouraged to contribute.

---

## 🚀 Features
- Sentiment classification into **Negative**, **Neutral**, or **Positive**.
- Returns **probability scores** for each class.
- Easy-to-use **REST API** endpoint (`/predict`).

---

## 📦 Installation & Setup

### 1. Clone the Repository
```bash
git clone https://github.com/tibashh/Reddit-Comments-Sentiment-Analysis.git
cd reddit-sentiment-api
```

### 2. Create Virtual Environment (Optional but Recommended)
```bash
python -m venv venv
source venv/bin/activate   # On Linux/Mac
venv\Scripts\activate    # On Windows
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Start the Project
```bash
python app.py
```
By default, the API will be running at:
```
http://127.0.0.1:5000/predict
```

---

## 📡 API Usage

<img width="1062" height="837" alt="Ekran görüntüsü 2025-10-03 213555" src="https://github.com/user-attachments/assets/8fd76720-ddc6-4ced-9e74-413dd9d671eb" />


<img width="1082" height="816" alt="Ekran görüntüsü 2025-10-03 213743" src="https://github.com/user-attachments/assets/897ec21d-9094-4579-ad09-0ea91e03451a" />


<img width="1077" height="807" alt="Ekran görüntüsü 2025-10-03 213957" src="https://github.com/user-attachments/assets/8b861791-c39a-46d2-9cf1-54f8969207b4" />



## 🛠 Tech Stack
- **Python 3**
- **Flask** (REST API)
- **scikit-learn** (ML model)
- **Postman** (testing)


