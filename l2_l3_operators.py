import streamlit as st
import pandas as pd


def l2_op_details(l2_op, decisions):
    """
    L2 Operator's Details.

    Parameters:
        l2_op (int): L2 Operator ID
        decisions (str, optional): Operator's Decision

    Returns:
        L2 operator's ID, Decision, Decision Time in DataFrame
    """
    # L2 operator
    st.header('L2 operator Details')

    # L2 operator ID
    option_id_l2 = st.selectbox('L2 operator ID', l2_op)

    # L2 opertaor decision
    option_decision_l2 = st.selectbox('L2 operator decision', decisions)

    # L2 decision time
    option_decision_time_l2 = st.number_input('Decision Time (secs)', 1, 100, 6)

    # Creating the dataframe from L2 inputs
    inputs_l2 = {'L2LoginID': option_id_l2,
                 'L2Decision': option_decision_l2,
                 'L2_Op_Time': option_decision_time_l2}
    input_data_l2 = pd.DataFrame(inputs_l2, index=[0])
    input_data_l2["L2Decision"] = input_data_l2["L2Decision"].map({'Accept': 0,
                                                                   'Reject': 1,
                                                                   'Time out': 2})

    return option_id_l2, input_data_l2


def l3_op_details(l3_op, decisions):
    """
    L3 Operator's Details.

    Args:
        l3_op: L3 Operator ID
        decisions: Operator's Decision

    Returns:
        L3 operator's ID, Decision, Decision Time in DataFrame
    """
    # L3 operator
    st.header('L3 operator Details')

    # L3 operator ID
    option_id_l3 = st.selectbox('L3 operator ID', l3_op)

    # L3 opertaor decision
    option_decision_l3 = st.selectbox('L3 operator decision', decisions)

    # L3 decision time
    option_decision_time_l3 = st.number_input('Decision Time (secs)', 1, 150, 10)

    # Creating the dataframe from inputs
    inputs_l3 = {'L3LoginID': option_id_l3,
                 'L3Decision': option_decision_l3,
                 'L3_Op_Time': option_decision_time_l3}
    input_data_l3 = pd.DataFrame(inputs_l3, index=[0])
    input_data_l3["L3Decision"] = input_data_l3["L3Decision"].map({'Accept': 0,
                                                                   'Reject': 1,
                                                                   'Time out': 2})

    return option_id_l3, input_data_l3

