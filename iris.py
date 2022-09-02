import streamlit as st
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
    
st.write("""
# Simple Iris Flower Prediction App
This app predicts the **Iris flower** type!
""")

st.sidebar.header('User Input Parameters')

def user_input_features():
    sepal_length = st.sidebar.slider('Sepal length', 4.3, 7.9, 5.4)
    sepal_width = st.sidebar.slider('Sepal width', 2.0, 4.4, 3.4)
    petal_length = st.sidebar.slider('Petal length', 1.0, 6.9, 1.3)
    petal_width = st.sidebar.slider('Petal width', 0.1, 2.5, 0.2)
    data = {'sepal_length': sepal_length,
            'sepal_width': sepal_width,
            'petal_length': petal_length,
            'petal_width': petal_width}
    features = pd.DataFrame(data, index=[0])
    return features

df = user_input_features()

st.subheader('User Input parameters')
st.write(df)

iris = pd.read_csv('https://raw.githubusercontent.com/Ansolehah/streamlit-example/main/iris_csv.csv')
X = iris[['sepal_length','sepal_width','petal_length','petal_width']]
Y = iris['species']

clf = RandomForestClassifier()
clf.fit(X, Y)

prediction = clf.predict(df)
prediction_proba = clf.predict_proba(df)

st.subheader('Class labels and their corresponding index number')

####dipslay in list###########
#st.write(Y.unique().tolist())

####dipslay in table###########
st.write(Y.unique())

st.subheader('Prediction')
#st.write(iris.speciest_names[prediction])
st.write(prediction)

st.subheader('Prediction Probability')
st.write(prediction_proba)

st.image("https://www.thespruce.com/thmb/xTuQCqR8TSPq_bb2D4yFIe54FPg=/4200x2362/smart/filters:no_upscale()/iris-flowers-plant-profile-5120188-hero-ccb44fcb101b4314b913ce5af09f9c1c.jpg")

st.success("Congratulations Ain! You have completed Final Assignment (For Beginners). Let's proceed with advanced version.")

def convert_df(iris):
   return iris.to_csv().encode('utf-8')


csv = convert_df(iris)

st.download_button(
   "Download Iris Data",
   csv,
   "iris_csv.csv",
   "text/csv",
   key='download-csv'
)
