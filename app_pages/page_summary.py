import streamlit as st

def page_summary_body():

    st.write("### Quick Project Summary")

    # text based on README file - "Dataset Content" section
    st.info(
        f"**General Information**\n"
        f"* The cherry plantation crop is failing due to the presance of "
        f"a powdery mildew. Currently, the detection process is a manual inspection \n"
        f"* To save time,  an ML system that is capable of detection has bee proposed. \n\n"
        f"**Project Dataset**\n"
        f"* The dataset contains upwards of 4000 leaf images. "
        f"The images show cherry leaves that are healthy and those that have powdery mildew, "
        f"which is a fungal disease affecting a wide range of plants.")

    # Link to README file, so the users can have access to full project documentation
    st.write(
        f"* For additional information, please visit and **read** the "
        f"Project README file (https://github.com/NielMc/PA-proj/README.md).")
    

    # copied from README file - "Business Requirements" section
    st.success(
        f"The project has two business requirements:\n"
        f"* 1 - The client is interested in conducting a study to differentiate "
        f"healthy and mildewed cherry leaves visually. \n"
        f"* 2 - The client is interested to predict if a cherry leaf is healthy or not."
        )

        