import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.datasets import load_iris
from sklearn.ensemble import RandomForestClassifier

iris = load_iris()
X = iris.data
y = iris.target
model = RandomForestClassifier()
model.fit(X, y)

st.title("Iris Flower Species Predictor")
st.write(   """
    This web app allows you to input features of an iris flower and predicts its species using a trained machine learning model.
    """
)

st.sidebar.header("Input Features")

def user_input_features():
    sepal_length = st.sidebar.slider('Sepal length (cm)', float(X[:,0].min()), float(X[:,0].max()), float(X[:,0].mean()))
    sepal_width = st.sidebar.slider('Sepal width (cm)', float(X[:,1].min()), float(X[:,1].max()), float(X[:,1].mean()))
    petal_length = st.sidebar.slider('Petal length (cm)', float(X[:,2].min()), float(X[:,2].max()), float(X[:,2].mean()))
    petal_width = st.sidebar.slider('Petal width (cm)', float(X[:,3].min()), float(X[:,3].max()), float(X[:,3].mean()))
    data = {
        'sepal length (cm)': sepal_length,
        'sepal width (cm)': sepal_width,
        'petal length (cm)': petal_length,
        'petal width (cm)': petal_width
    }
    features = pd.DataFrame(data, index=[0])
    return features

input_df = user_input_features()

st.subheader("User Input Features")
st.write(input_df)

prediction = model.predict(input_df.values)
prediction_proba = model.predict_proba(input_df.values)

st.subheader("Prediction")
st.write(f"Predicted species: **{iris.target_names[prediction][0]}**")

st.subheader("Prediction Probabilities")
proba_df = pd.DataFrame(prediction_proba, columns=iris.target_names)
st.write(proba_df)

st.subheader("Model Feature Importances")
fig, ax = plt.subplots()
ax.barh(iris.feature_names, model.feature_importances_)
ax.set_xlabel("Importance")
st.pyplot(fig)


