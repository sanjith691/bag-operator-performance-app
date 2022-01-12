# Importing Required Packages
import streamlit as st
from PIL import Image
from operators import operators_list
from l2_l3_operators import l2_op_details, l3_op_details
from new_operators import new_op_details
from predictions import model_inputs


# Data configuration
l2_op, l3_op = operators_list()
decisions = ['Accept', 'Reject', 'Time out']

# Web Page Configuation
st.set_page_config(
    page_title='Bag Operator Performance Predictor',
    layout='wide',
    initial_sidebar_state='expanded'
)

# WebApp Style
with open('static/style.css') as f:
    st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)


# Title for the app
def title():
    image = Image.open('static/bags.png')
    img, mid, head = st.columns([25, 5, 80])
    with img:
        st.image(image, channels="BGR", width=220)
    with head:
        st.title("""
                    # Bag Operator's Performance Predictor App
                    Let's check the performance of the operators!!
                    """)


def main():
    # title of the webapp
    title()

    # operator selection
    st.sidebar.subheader('About:')
    st.sidebar.write('This webApp helps to find the performace of the L2 and L3 operators '
                     'at the airport.')
    st.empty()
    options = st.sidebar.radio('Operator Selection:', ['L2 Operator',
                                                       'L3 Operator',
                                                       'New Operator'])
    # L2 operator Details
    if options == 'L2 Operator':
        ids, df = l2_op_details(l2_op, decisions)

    # L3 operator Details
    elif options == 'L3 Operator':
        ids, df = l3_op_details(l3_op, decisions)

    # New Operator
    elif options == 'New Operator':
        st.header('New Operator Details:')
        options, ids, df = new_op_details(decisions)

    # Make predictions
    model_inputs(options, ids, df)


if __name__ == '__main__':
    main()
