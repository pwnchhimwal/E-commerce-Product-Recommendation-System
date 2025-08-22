import streamlit as st
import pandas as pd
import json
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

st.title(" Interactive Product Recommendation System")

# File uploader
uploaded_file = st.file_uploader("Upload a JSON file with product data", type="json")

if uploaded_file is not None:
    try:
        # Load uploaded JSON
        data = json.load(uploaded_file)

        if 'products' not in data:
            st.error("Uploaded JSON does not contain a 'products' key.")
        else:
            product_list = data['products']
            df = pd.DataFrame(product_list)

            # Rename columns
            df.rename(columns={
                'id': 'Product ID',
                'name': 'Product Name',
                'category': 'Category',
                'price': 'Price',
                'description': 'Description'
            }, inplace=True)

            # Combine text for TF-IDF
            df['Combined'] = (
                df['Product Name'] + ' ' +
                df['Category'] + ' ' +
                df['Price'].astype(str) + ' ' +
                df['Description']
            )

            # TF-IDF and similarity
            vectorizer = TfidfVectorizer()
            tfidf_matrix = vectorizer.fit_transform(df['Combined'])
            cosine_sim = cosine_similarity(tfidf_matrix, tfidf_matrix)

            # Recommend function
            def recommend(product_index, num_recommendations=5):
                sim_scores = list(enumerate(cosine_sim[product_index]))
                sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)[1:num_recommendations+1]
                recommended_indices = [i[0] for i in sim_scores]
                return df.iloc[recommended_indices][['Product ID', 'Product Name', 'Category', 'Price', 'Description']]

            # Sidebar controls
            st.sidebar.header("Recommendation Settings")
            selected_product = st.sidebar.selectbox("Select a product", df['Product Name'].unique())
            num_recs = st.sidebar.slider("Number of recommendations", 1, 10, 5)

            # Generate recommendations
            product_index = df[df['Product Name'] == selected_product].index[0]
            results = recommend(product_index, num_recs)

            # Show data
            st.subheader("Uploaded Product Data")
            st.dataframe(df)

            # Show results
            st.subheader(f"Recommendations for: {selected_product}")
            st.dataframe(results)

    except Exception as e:
        st.error(f"Error reading file: {e}")

else:
    st.info("Please upload a JSON file to begin.")
        


