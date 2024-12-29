import streamlit as st
from streamlit_option_menu import option_menu
from pathlib import Path
from PIL import Image
from descriptions import WORK_NAME, TC_NAME, DESCRIPTION_a, DESCRIPTION_b, EMAIL, SOCIAL_MEDIA, PROJECTS, EDU, CAREER, SKILLS
from print_txt import txt

# --- Path Settings ---
current_dir = Path(__file__).parent if "__file__" in locals() else Path.cwd()
resume_file = current_dir / "assets" / "CV.pdf"
profile_pic = current_dir / "assets" / "profile_pic.jpg"

# --- Load Assets ---
with open(resume_file, "rb") as pdf_file:
    PDFbyte = pdf_file.read()

profile_pic = Image.open(profile_pic)

# --- Top Header ---
st.set_page_config(layout = "centered")

with st.container():
    col_01, col_02 = st.columns(2, 
                                gap = "small", 
                                vertical_alignment = "center",
                        )

    with col_01:
        st.title(WORK_NAME)
        st.subheader(TC_NAME)
        st.warning(DESCRIPTION_a)
        st.info(DESCRIPTION_b)

    with col_02:
        st.image(profile_pic, width = 300)
        st.download_button(
            label = " ⬇︎ Download Resume",
            data = PDFbyte,
            file_name = resume_file.name,
            mime = "application/octet-stream",
        )

# --- Format Layout ---
with st.container():
    selected = option_menu(
        menu_title = None,
        options = ['About', 'Skills', 'Projects', 'Contact'],
        icons = ['person-fill', 'wrench', 'table', 'telephone-plus-fill'],
        orientation = 'horizontal'
    )

if selected == 'About':
    tab_a1, tab_a2 = st.tabs(['Career Summary',
                              'Education'])
    with tab_a1:

        txt(f"{CAREER['shopee']['title']}, {CAREER['shopee']['corp_name']}", f"{CAREER['shopee']['period']}")
        st.markdown(CAREER['shopee']['info'])

        st.divider()

        txt(f"{CAREER['ailabs']['title']}, {CAREER['ailabs']['corp_name']}", f"{CAREER['ailabs']['period']}")
        st.markdown(CAREER['ailabs']['info'])

        st.divider()

        txt(f"{CAREER['eland']['title']}, {CAREER['eland']['corp_name']}", f"{CAREER['eland']['period']}")
        st.markdown(CAREER['eland']['info'])

    with tab_a2:

        txt(f"{EDU['degree']}, {EDU['school']}", f"{EDU['period']}")
        st.markdown(EDU['info'])

if selected == 'Skills':
    tab_s1, tab_s2 = st.tabs(['Hard Skill', 
                              'Soft Skill'])
    with tab_s1:
        st.markdown(SKILLS['hard'])

    with tab_s2:
        st.markdown(SKILLS['soft'])

if selected == 'Projects':
    tab_p1, tab_p2 = st.tabs(['Side Projects',
                              'Work Projects'])
    with tab_p1:

        st.markdown(PROJECTS['side']['app']['name'])
        st.markdown(PROJECTS['side']['app']['info'])
        st.info(PROJECTS['side']['app']['access'])

        st.divider()

        st.markdown(PROJECTS['side']['wal']['name'])
        st.markdown(PROJECTS['side']['wal']['info'])
        st.info(PROJECTS['side']['wal']['access'])

    with tab_p2:

        st.markdown(PROJECTS['work']['rfm']['name'])
        st.markdown(PROJECTS['work']['rfm']['info'])
        st.info(PROJECTS['work']['rfm']['access'])

        st.divider()

        st.markdown(PROJECTS['work']['dws']['name'])
        st.markdown(PROJECTS['work']['dws']['info'])
        
        st.divider()

        st.markdown(PROJECTS['work']['ls']['name'])
        st.markdown(PROJECTS['work']['ls']['info'])

if selected == 'Contact':
    st.write('Gamil : ', EMAIL)
    st.write('LinkedIn : ', SOCIAL_MEDIA['LinkedIn'])
    st.write('GitHub : ', SOCIAL_MEDIA['GitHub'])
