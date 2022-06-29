import streamlit as st
import numpy as np
import pandas as pd
import plotly.express as px
from tensorflow.keras.models import load_model
from PIL import Image
from src.data_management import load_pkl_file


def plot_predictions_probabilities(pred_proba, pred_class, version):
    """
    Plot prediction probability results
    """

    st.warning(
        f"* The bar plot below shows the prediction probability for the "
        f"cherry leaf sample to be healthy or mildewed.")

    class_indices = load_pkl_file(file_path=f"outputs/{version}/class_indices.pkl")
    
    prob_per_class= pd.DataFrame(
            data=[0,0],
            index=class_indices.keys(),
            columns=['Probability']
        )
    prob_per_class.loc[pred_class] = pred_proba
    for x in prob_per_class.index.to_list():
        if x not in pred_class: prob_per_class.loc[x] = 1 - pred_proba
    prob_per_class = prob_per_class.round(3)
    prob_per_class['Diagnostic'] = prob_per_class.index
    
    fig = px.bar(
            prob_per_class,
            x = 'Diagnostic',
            y = prob_per_class['Probability'],
            range_y=[0,1],
            width=600, height=300,template='seaborn')
    st.plotly_chart(fig)



def resize_input_image(img, version):  
    """
    Reshape image to average image size
    """
    image_shape = load_pkl_file(file_path=f"outputs/{version}/image_shape.pkl")
    img_resized = img.resize((image_shape[1], image_shape[0]), Image.ANTIALIAS)
    my_image = np.expand_dims(img_resized, axis=0) / 255 # it needs to rescale the live data,
                                                         # since the model was trained with scaled data 

    return my_image




def load_model_and_predict(my_image, version):
    """
    Load and perform ML prediction over live images
    """
    model = load_model(f"outputs/{version}/mildew_detector_model.h5")


    prediction_proba = model.predict(my_image)
    prediction_index = np.argmax(prediction_proba, axis=1)[0] 



    class_indices = load_pkl_file(file_path=f"outputs/{version}/class_indices.pkl")
    target_map = {v: k for k, v in class_indices.items()}
    
    pred_class =  target_map[prediction_index] 
    pred_proba = prediction_proba[0,prediction_index]

    if pred_class == 'healthy': msg = 'is healthy'
    else: msg = 'is mildewed'
    st.info(f"The predictive analysis indicates the sample cherry leaf **{msg}**")
    
    return pred_proba, pred_class