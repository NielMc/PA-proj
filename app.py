import streamlit as st
from app_pages.multi_page import MultiPage

from app_pages.page_summary import page_summary_body
# from app_pages.page_cherry_leaf_visualizer import page_cherry_leaf_visualizer_body
from app_pages.page_mildew_detector import page_mildew_detector_body
# from app_pages.page_ml_performance import page_ml_performance_metrics

# instantiate app
app = MultiPage(app_name= "Mildew Detector") 

# Add your app pages here using .add_page()
app.app_page("Quick Project Summary", page_summary_body)
# app.app_page("Cherry Leaf Visualizer", page_cherry_leaf_visualizer_body)
app.app_page("Mildew Detector", page_mildew_detector_body)
# app.app_page("ML Performance Metrics", page_ml_performance_metrics)

app.run() # run app