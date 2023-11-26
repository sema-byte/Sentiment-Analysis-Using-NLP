# %%
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer

# %%
import pickle

# Load the TF-IDF matrix from the file
with open("C:/Users/nz390/Downloads/tf.pkl", "rb") as file:
    tf = pickle.load(file)

# %%
merged = pd.read_csv('C:/Users/nz390/Downloads/filename.csv')

# %%
with open("C:/Users/nz390/Downloads/rf.pkl", 'rb') as f:
    model = pickle.load(f)

# %%
def prediction(reviews_text):
    # Convert the input reviews_text into an iterable of raw text documents
    if isinstance(reviews_text, str):
        reviews_text = [reviews_text]  # Wrap single string into a list

    tfidf_data = pd.DataFrame(tf.transform(reviews_text).toarray())
    
    # Get the column names
    column_names = tf.get_feature_names_out()

    # Assign the column names to the DataFrame
    tfidf_data.columns = column_names
    predictions = model.predict(tfidf_data)
     
  # Convert numeric predictions to string labels
    sentiment_mapping = {1: 'positive', -1: 'negative', 0: 'neutral'}
    sentiment_labels = [sentiment_mapping[prediction] for prediction in predictions]
    
    return sentiment_labels
 




