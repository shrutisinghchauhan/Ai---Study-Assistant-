"""Warm editorial theme inspired by the supplied Wix vacation-rental preview.
Use with Streamlit: from wix_inspired_theme import apply_wix_theme
"""
import streamlit as st


def apply_wix_theme():
    st.markdown(r"""
<style>
/* Warm, spacious editorial palette */
:root { --cream:#f8f5ee; --ivory:#fffdf8; --sand:#eee8dd; --sage:#dce4d6; --olive:#65745b; --clay:#b77760; --ink:#302f2b; --muted:#736f67; --line:#ddd7cc; }
html,body,.stApp,[data-testid="stAppViewContainer"], [data-testid="stMain"] {background:var(--cream)!important;color:var(--ink)!important;color-scheme:light!important;}
[data-testid="stHeader"] {background:var(--cream)!important;}
[data-testid="stToolbar"] {background:transparent!important;}
[data-testid="stSidebar"],[data-testid="stSidebar"]>div:first-child {background:#eaece3!important;border-right:1px solid var(--line)!important;}
[data-testid="stMainBlockContainer"] {max-width:1580px!important;padding-top:2.2rem!important;}
.stApp h1 {font-family:Georgia,'Times New Roman',serif!important;font-weight:500!important;font-size:clamp(2rem,3vw,3.25rem)!important;line-height:1.15!important;color:var(--ink)!important;background:none!important;-webkit-text-fill-color:var(--ink)!important;letter-spacing:-.035em!important;}
.stApp h2,.stApp h3 {font-family:Georgia,'Times New Roman',serif!important;color:var(--ink)!important;font-weight:500!important;}
.stApp p,.stApp li,.stApp label,.stApp small,.stApp span {color:var(--ink);}
[data-testid="stCaptionContainer"] p {color:var(--muted)!important;}
/* Consistent calm controls */
.stButton>button,[data-testid="stPopover"] button,[data-testid="stBaseButton-secondary"],[data-testid="stBaseButton-primary"] {background:var(--sage)!important;color:#344231!important;border:1px solid #c4d0bc!important;border-radius:9px!important;box-shadow:none!important;font-weight:550!important;transition:background .15s ease!important;}
.stButton>button:hover,[data-testid="stPopover"] button:hover {background:#cddac6!important;border-color:#9eb195!important;color:#273325!important;}
.stButton>button p,.stButton>button span,[data-testid="stPopover"] button p {color:inherit!important;}
/* Inputs and uploaders */
[data-testid="stTextInput"] input,[data-testid="stTextArea"] textarea,[data-testid="stChatInput"] textarea {background:var(--ivory)!important;color:var(--ink)!important;-webkit-text-fill-color:var(--ink)!important;caret-color:var(--ink)!important;}
[data-testid="stTextInput"] input::placeholder,[data-testid="stChatInput"] textarea::placeholder {color:#8d887f!important;-webkit-text-fill-color:#8d887f!important;}
[data-testid="stTextInput"]>div>div,[data-testid="stChatInput"],[data-testid="stFileUploaderDropzone"] {background:var(--ivory)!important;border:1px solid var(--line)!important;border-radius:11px!important;box-shadow:none!important;}
[data-testid="stFileUploader"], [data-testid="stFileUploaderDropzone"] section {background:var(--ivory)!important;color:var(--ink)!important;border-radius:11px!important;}
[data-testid="stFileUploaderDropzone"] button {background:var(--sage)!important;color:var(--ink)!important;border:1px solid #c4d0bc!important;}
[data-testid="stFileUploaderDropzone"] *,[data-testid="stFileUploader"] small {color:var(--ink)!important;}
[data-testid="stChatInput"] button {background:var(--olive)!important;border-radius:8px!important;}
[data-testid="stChatInput"] button svg {color:white!important;}
/* Chat messages */
[data-testid="stChatMessage"] {background:var(--ivory)!important;border:1px solid var(--line)!important;border-radius:12px!important;padding:1.05rem!important;box-shadow:none!important;}
[data-testid="stChatMessage"]:has([data-testid="stChatMessageAvatarUser"]) {background:#eef0e8!important;border-color:#d9e0d3!important;}
[data-testid="stChatMessage"] p,[data-testid="stChatMessage"] li,[data-testid="stChatMessage"] span {color:var(--ink)!important;}
/* Metric panels */
[data-testid="stMetric"] {background:var(--ivory)!important;border:1px solid var(--line)!important;border-radius:10px!important;padding:14px!important;}
[data-testid="stMetricValue"] {color:var(--olive)!important;}
[data-testid="stMetricLabel"] * {color:var(--muted)!important;}
/* Expanders and popovers */
[data-testid="stExpander"], [data-testid="stPopoverBody"], [data-baseweb="popover"]>div {background:var(--ivory)!important;border:1px solid var(--line)!important;border-radius:10px!important;color:var(--ink)!important;}
[data-testid="stExpander"] summary {color:var(--ink)!important;}
/* Sliders and checkboxes */
[data-testid="stSlider"] [role="slider"] {background:var(--olive)!important;border-color:var(--olive)!important;}
[data-testid="stCheckbox"] input {accent-color:var(--olive)!important;}
hr {border-color:var(--line)!important;}
/* Existing custom sections from app.py */
.welcome-card {background:#f0e9df!important;border:1px solid #e3d8c8!important;border-radius:12px!important;padding:25px!important;box-shadow:none!important;}
.welcome-card h3 {color:#6b5748!important;font-family:Georgia,'Times New Roman',serif!important;}
.history-heading {background:#dce4d6!important;color:#3d4c38!important;border:1px solid #c6d2c0!important;border-radius:9px!important;box-shadow:none!important;padding:13px 16px!important;}
/* Avoid dark widgets from browser theme where possible */
[data-baseweb="input"], [data-baseweb="textarea"], [data-baseweb="select"]>div {background:var(--ivory)!important;color:var(--ink)!important;border-color:var(--line)!important;}
/* Keep mobile layouts comfortable */
@media(max-width:900px){[data-testid="stMainBlockContainer"]{padding:1.2rem!important}.stApp h1{font-size:2rem!important;}}
</style>
""", unsafe_allow_html=True)
