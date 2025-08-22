# 🛍 E-commerce Product Recommendation System

A **Streamlit-powered**, content-based recommendation web app that uses **TF-IDF** and **cosine similarity** to suggest products based on item descriptions.

---

## 🚀 Live Demo

👉 [Click here to view the deployed app](https://pwnchhimwal-e-commerce-product-recommendation-system-app-wxrz95.streamlit.app/)

---

## 🖥️ Tech Stack

- **Python 3**
- **Streamlit** — interactive web interface  
- **scikit-learn** — TF-IDF vectorization & cosine similarity  
- **NumPy** / **Pandas** — data processing  
- **Matplotlib** / **Seaborn** — visualization  

---

## 📂 Project Structure

- `app.py` — Main Streamlit app  
- `requirements.txt` — Project dependencies  
- `README.md` — Project documentation  

---

## ⚙️ Installation & Setup

1. **Clone the repository**  
   ```bash
   git clone https://github.com/pwnchhimwal/E-commerce-Product-Recommendation-System.git
   cd E-commerce-Product-Recommendation-System



 2> Create and activate a virtual environment

python3 -m venv venv
source venv/bin/activate   # Mac/Linux
venv\Scripts\activate      # Windows

3> Install dependencies

Install dependencies

▶️ Run the App Locally

streamlit run app.py


Then open http://localhost:8501
 in your browser

 🔎 How It Works

Input: User selects a product.

Vectorization: Product descriptions converted to vectors using TF-IDF.

Similarity: Compute cosine similarity with other products.

Output: Show top recommended products in the app


Requirements
streamlit
numpy
pandas
scikit-learn
matplotlib
seaborn


👨‍💻 Author

Pawan Chhimwal
🔗 GitHub Profile

🌟 Future Enhancements

Add image-based recommendations

Hybrid approach (content + collaborative filtering)

User feedback loop for personalization

More interactive visualizations

