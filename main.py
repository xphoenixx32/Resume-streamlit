import streamlit as st
from streamlit_option_menu import option_menu
from pathlib import Path
from descriptions import WORK_NAME, TC_NAME, DESCRIPTION_a, DESCRIPTION_b, EMAIL, SOCIAL_MEDIA, PROJECTS, EDU, CAREER, SKILLS
from print_txt import txt

# --- Path Settings ---
current_dir = Path(__file__).parent if "__file__" in locals() else Path.cwd()
resume_file = current_dir / "assets" / "CV_Leanlinmy.pdf"

# --- Load Assets ---
with open(resume_file, "rb") as pdf_file:
    PDFbyte = pdf_file.read()

# --- Top Header ---
st.set_page_config(layout = "centered")
st.caption('''
*A Web-based Resume Built with Streamlit*
''')
st.logo("assets/profile.png")
st.title(f'''***{WORK_NAME}***''')
st.markdown(f'''##### ***{TC_NAME}***''')
st.warning(DESCRIPTION_a, icon = "💡")
st.success(DESCRIPTION_b, icon = "⚡")

st.download_button(
    label = "  ⏬ **Download Resume** (*.pdf*)  ",
    data = PDFbyte,
    file_name = resume_file.name,
    mime = "application/octet-stream",
    help = "Click to download the resume as a PDF file."
)

# --- Format Layout ---
with st.container():
    selected = option_menu(
        menu_title = None,
        options = ['About', 'Skills', 'Projects', 'Contact'],
        icons = ['person-circle', 'tools', 'bar-chart-steps', 'telephone-plus-fill'],
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
        st.markdown(PROJECTS['side']['ml']['name'])
        st.markdown(PROJECTS['side']['ml']['info'])
        st.info(PROJECTS['side']['ml']['access'])

        st.divider()
        
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
    col1, col2 = st.columns(2)
    with col1:
        st.image('assets/gmail.png', width = 60)
        # st.error(f'''
        # ##### ***Gmail***
        # > {EMAIL}
        # ''')
        st.markdown(
            f'''
            <div style="
                background-color: #eea2ad; 
                padding: 15px 20px; 
                border-radius: 8px; 
                color: #000000; 
                box-shadow: 0px 2px 5px rgba(0, 0, 0, 0.1);">
                <h5 style="margin: 0;"><b>Gmail</b></h5>
                <p style="margin: 5px 0 0 0;">
                    <a href="{EMAIL}" target="_blank" style="color: #0000EE; text-decoration: none;">
                        {EMAIL}
                    </a>
                </p>
            </div>
            ''',
            unsafe_allow_html=True
        )
    with col2:
        st.image('assets/line.png', width = 60)
        # st.success(f'''
        # ##### ***LINE id***
        # > {SOCIAL_MEDIA['Line ID']}
        # ''')
        st.markdown(
            f'''
            <div style="
                background-color: #caff70; 
                padding: 15px 20px; 
                border-radius: 8px; 
                color: #000000; 
                box-shadow: 0px 2px 5px rgba(0, 0, 0, 0.1);">
                <h5 style="margin: 0;"><b>LINE id</b></h5>
                <p style="margin: 5px 0 0 0;">
                    <a href="{SOCIAL_MEDIA['Line ID']}" target="_blank" style="color: #0000EE; text-decoration: none;">
                        {SOCIAL_MEDIA['Line ID']}
                    </a>
                </p>
            </div>
            ''',
            unsafe_allow_html=True
        )
    st.divider()
    col3, col4 = st.columns(2)
    with col3:
        st.image('assets/linkedin.png', width = 60)
        # st.info(f'''
        # ##### ***LinkedIn***
        # > [{SOCIAL_MEDIA['LinkedIn']}]({SOCIAL_MEDIA['LinkedIn']})
        # ''')
        st.markdown(
            f'''
            <div style="
                background-color: #b0e2ff; 
                padding: 15px 20px; 
                border-radius: 8px; 
                color: #000000; 
                box-shadow: 0px 2px 5px rgba(0, 0, 0, 0.1);">
                <h5 style="margin: 0;"><b>LinkedIn</b></h5>
                <p style="margin: 5px 0 0 0;">
                    <a href="{SOCIAL_MEDIA['LinkedIn']}" target="_blank" style="color: #0000EE; text-decoration: none;">
                        {SOCIAL_MEDIA['LinkedIn']}
                    </a>
                </p>
            </div>
            ''',
            unsafe_allow_html=True
        )
    with col4:
        st.image('assets/github.png', width = 60)
        st.markdown(
            f'''
            <div style="
                background-color: #bebebe; 
                padding: 15px 20px; 
                border-radius: 8px; 
                color: #000000; 
                box-shadow: 0px 2px 5px rgba(0, 0, 0, 0.1);">
                <h5 style="margin: 0;"><b>GitHub</b></h5>
                <p style="margin: 5px 0 0 0;">
                    <a href="{SOCIAL_MEDIA['GitHub']}" target="_blank" style="color: #0000EE; text-decoration: none;">
                        {SOCIAL_MEDIA['GitHub']}
                    </a>
                </p>
            </div>
            ''',
            unsafe_allow_html=True
        )
