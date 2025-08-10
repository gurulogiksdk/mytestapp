import streamlit as st
from config import widget_key
from config import constants
from backend.utils import generate_response, generate_response_with_files
from datetime import date

def generate_resilience_helper():
    st.session_state[widget_key.RESPONSE_DATA] = None
    openAI_client = st.session_state[widget_key.OPEN_AI_CLIENT_OBJ]
    tier_level = st.session_state[widget_key.TIER_LEVEL_DROPDOWN_WIDGET]
    file_inputs = {
        "Files": st.session_state.get(widget_key.ARCH_HLD_FILE_SELECTOR_WIDGET, []),
    }
    st.session_state[widget_key.RESPONSE_DATA] = generate_response(openAI_client=openAI_client, tier_level=tier_level, files_dict=file_inputs)
    


def first_row():

    application_name_col, tier_col, file_col, but_col = st.columns([0.25, 0.25, 0.25, 0.25])

    with application_name_col:
        st.text_input("Application Name", key=widget_key.APPLICATION_NAME_WIDGET)

    with tier_col:
        st.selectbox("Tier Level", options=[0,1], key=widget_key.TIER_LEVEL_DROPDOWN_WIDGET)

    with file_col:
        st.write("")
        with st.expander("Upload Files"):
            st.file_uploader(
                "",
                type=constants.file_types_allowed_list,  # Extendable
                accept_multiple_files=True, key=widget_key.ARCH_HLD_FILE_SELECTOR_WIDGET
            )
    
    with but_col:
        st.write("")
        st.button("Generate Resilience Assessment Summary", key=widget_key.GET_ANSWER_WIDGET, on_click=lambda : generate_resilience_helper())

"""
# def files_upload_row():

#     file_1_col, file_2_col, file_3_col, file_4_col = st.columns([0.25, 0.25, 0.25, 0.25])
#     with file_1_col:
#         with st.expander("HLD/Detailed Design Docs, Architecture Diagrams"):
#             st.file_uploader(
#                 "Upload",
#                 type=constants.file_types_allowed_list,  # Extendable
#                 accept_multiple_files=True, key=widget_key.ARCH_HLD_FILE_SELECTOR_WIDGET
#             )
#     with file_2_col:
#         with st.expander("DR Plan, DR Procedures/Runbooks"):
#             st.file_uploader(
#                 "Upload",
#                 type=constants.file_types_allowed_list,  # Extendable
#                 accept_multiple_files=True, key=widget_key.DR_PLAN_PROCEDURE_SELECTOR_WIDGET
#             )

#     with file_3_col:
#         with st.expander("DR Test Results, TTX results/minutes"):
#             st.file_uploader(
#                 "Upload",
#                 type=constants.file_types_allowed_list,  # Extendable
#                 accept_multiple_files=True, key=widget_key.DR_TEST_TTX_FILE_SELECTOR_WIDGET
#             )

#     with file_4_col:
#         with st.expander("RCA reports (P1/P2 last 12–18 months)"):
#             st.file_uploader(
#                 "Upload",
#                 type=constants.file_types_allowed_list,  # Extendable
#                 accept_multiple_files=True, key=widget_key.RCA_REPORTS_FILE_SELECTOR_WIDGET
#             )

#     file_5_col, file_6_col, file_7_col, get_res_col = st.columns([0.25, 0.25, 0.25, 0.25])

#     with file_5_col:
#         with st.expander("Monitoring dashboards, synthetic definitions"):
#             st.file_uploader(
#                 "Upload",
#                 type=constants.file_types_allowed_list,  # Extendable
#                 accept_multiple_files=True, key=widget_key.MONITORING_DASHBOARDS_FILE_SELECTOR_WIDGET
#             )
#     with file_6_col:
#         with st.expander("Backup/restore settings and reports"):
#             st.file_uploader(
#                 "Upload",
#                 type=constants.file_types_allowed_list,  # Extendable
#                 accept_multiple_files=True, key=widget_key.BACKUP_SETTINGS_REPORTS_FILE_SELECTOR_WIDGET
#             )
#     with file_7_col:
#         with st.expander("Any prior patterns/standards"):
#             st.file_uploader(
#                 "Upload",
#                 type=constants.file_types_allowed_list,  # Extendable
#                 accept_multiple_files=True, key=widget_key.PRIOR_PATTERN_STANDARDS_FILE_SELECTOR_WIDGET
#             )

#     with get_res_col:
#         st.button("Generate Resilience Assessment Summary", key=widget_key.GET_ANSWER_WIDGET, on_click=lambda : generate_resilience_helper())

"""

def main_UI():
    first_row()

    if widget_key.RESPONSE_DATA in st.session_state and st.session_state[widget_key.RESPONSE_DATA] is not None:
        st.write(f"Application Name : {st.session_state[widget_key.APPLICATION_NAME_WIDGET]}")
        st.write(f"Date : {date.today()}")
        st.write(st.session_state[widget_key.RESPONSE_DATA])


