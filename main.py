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
# st.image("assets/profile.png", width = 160)
st.title(f'''***{WORK_NAME}***''')
st.markdown(f'''##### ***{TC_NAME}***''')
st.warning(DESCRIPTION_a, icon = "💡")
st.success(DESCRIPTION_b, icon = "⚡")

st.download_button(
    label = "  ⏬ **Download Resume** (*.pdf*)  ",
    data = PDFbyte,
    file_name = resume_file.name,
    mime = "application/octet-stream",
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
    st.image('assets/gmail.png', width = 60)
    st.info(f'''
    > {EMAIL}
    ''')
    
    st.image('assets/linkedin.png', width = 60)
    st.info(f'''
    > [{SOCIAL_MEDIA['LinkedIn']}]({SOCIAL_MEDIA['LinkedIn']})
    ''')

    st.image('assets/github.png', width = 60)
    st.markdown(f'''
    > [{SOCIAL_MEDIA['GitHub']}]({SOCIAL_MEDIA['GitHub']})
    ''')
