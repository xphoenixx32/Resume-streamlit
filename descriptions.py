# --- Basics ---
WORK_NAME = "Lean Lin"
TC_NAME = "Ming Yan, Lin"
DESCRIPTION_a = """
Senior Data Analyst with 5+ years experience
"""
DESCRIPTION_b = """
Skilled in leveraging **ML models**, **EDA**, **creating impactful visualizations** to uncover actionable trends, extracting insights into strategic business decisions.
"""

# --- Contacts ---
EMAIL = "xphoenixx32@email.com"
SOCIAL_MEDIA = {
    "LinkedIn": "https://www.linkedin.com/in/leanlin/",
    "GitHub": "https://github.com/xphoenixx32",
}

# --- Information of About ---
EDU = {
    'degree': '#### **Master Degree**, *Public Administration & Policy*',
    'school': 'National Taipei University',
    'period': '2017 Sep ~ 2021 Jan',
    'info':'''
        ###### Thesis
        - **The Research on the Influence of Influencers’ Political Endorsement and Policy Marketing Effect:** *Using Internet Public Opinion Big Data to Analyze its Impact on Social Media* 
        - Thesis URL 🔗 : [Link](https://hdl.handle.net/11296/834k8b)
        ###### Grade
        - GPA : **3.8**
        ###### Honor
        - *Phi Tau Phi Honorary Membership*
        - *The C. C. Chang Scholarship of Administrative Science*
        - *The Rotary Foundation Scholarship*
    '''
}

CAREER = {
    'shopee':{
        'title': '#### **Data Analyst, Business Intelligence**',
        'corp_name': '*Shopee*',
        'period': '2024 Jan ~ Present',
        'info': '''
            - Identify `potential opportunities` and `plan actionable business improvement strategies` from existing sales data.
            - `Develop and maintain Data Dashboards or Trackers` for marketing analysis needs.
            - Assist in organizing and focusing on analysis requests from the MKT Campaign team, including but not limited to `consumer traffic`, `marketing campaign performance`, and `analysis on ordering incentives`.
        '''
    },
    'ailabs':{
        'title': '#### **Lead Data Analyst**',
        'corp_name': '*Taiwan AiLabs*',
        'period': '2023 Feb ~ 2023 Dec',
        'info': '''
            - `Lead 3 Data Analysts` and distribute the workload, organizing the needs from clients & senior management, and `meeting the overall goals` of the business unit's expectations.
            - `Utilizing community detection algorithms` to group atypical accounts, also `detecting atypical behavior patterns` on social media based on feature engineering & other ML methods. (2+ models for `YouTube` & `TikTok`)
            - Experienced in data visualization, `demonstrating evidence of coordinated inauthentic behaviors`, and `concluding with insights about how collaborative groups manipulated` specific information. (40+ reports)
        '''
    },
    'eland':{
        'title': '#### **Sr. Business Analyst**',
        'corp_name': '*eLand Information*',
        'period': '2019 Mar ~ 2023 Feb',
        'info': '''
            - `Providing conclusions and insights` among various realms based on data-driven evidence. (realms including `politics & policies`, `public relations`, `business analytics` and `marketing campaign`)
            - Involved in data-related tasks such as `Data Cleaning`, `Data Integration`, `Data Transformation` & `Data Visualization`, routinely delivering analytic reports. (100+ reports)
            - `Offering assistance and advice to clients` to help deal with system-operating or data-processing issues. (clients including business group, ad agency and public sector) 
            - `Occasionally serve as a lecturer` sharing thoughts or insights about Social Big Data and various quantitative methods. (25+ lectures or workshops)
        '''
    }
}

# --- Information of Skills ---
SKILLS = {
    'soft':'''
        #### Communication and Collaboration 🤝
        - *Clear Data Storytelling*
        - *Cross-Functional Collaboration*
        #### Critical Thinking and Problem-Solving 🧠
        - *Problem Decomposition*
        - *Logical Reasoning*
        - *Data-Driven Decision-Making*
        #### Adaptability and Growth Mindset 🌵
        - *Learning New Tools and Techniques*
        - *Adapting to Change*
    ''',
    'hard':'''
        #### Code & Data Tool 🐍
        - `Python`, `SQL`, `Streamlit`
        - `Looker Studio`, `Tableau`, `Power BI`
        - `Excel`, `Power Query`, `Power Pivot`
        #### Analytic Skills 🤖
        - `EDA` & `Data Mining`
        - `Data Visualization`
        - `Data Modeling`
        - `Machine Learning`
        - `Feature Engineering`
        - `ETL` & `Data Management`
        #### Certificate 🪪
        - *Google Business Intelligence Specialization*
    '''
}

# --- Information of Projects ---
PROJECTS = {
    'side':{
        'ml':{
            'name':'''
                #### *a Showcase Demo of ML Model & XAI (Web app)*
            ''',
            'info':'''
                - This Showcase Demo app helps user to better understand how a `Machine Learning Model` works, also realizing how variables interprete & predict `y` via `SHAP` Value.
                - I expected to `standerdize the process of understanding a ML Model` by building this app with meaningful metrics & visualization.
            ''',
            'access': '''
                - 🔗 [Access link](https://ml-xai-showcase-toolkit.streamlit.app/)
                - 👾 [GitHub Code Link](https://github.com/xphoenixx32/MLshowcase-streamlit/tree/main)
            '''
        },
        'app':{
            'name':'''
                #### *EDA Toolkit (Web app) - a Data Tool without any Coding*
            ''',
            'info':'''
                - The EDA Toolkit is a user-friendly web application built with Streamlit that assists data analysts and data scientists in `performing quick, interactive, and comprehensive EDA`.
                - I aimed to `simplify the process of understanding datasets` by providing tools for statistical insights and visualization.
            ''',
            'access': '''
                - 🔗 [Access link](https://data-eda-toolkit-by-leanlinmy.streamlit.app/)
                - 👾 [GitHub Code Link](https://github.com/xphoenixx32/EDA-streamlit/tree/main)
            '''
        },
        'wal':{
            'name':'''
                #### *Business Case Study - Walmart Sales Factors Analysis & Forcasting*
            ''',
            'info':'''
                - This case study aimed to realize `how factors affect 'Weekly_Sales' of Walmart` and `what's the intersection effect between factors` by Using `K-means Clustering`, `Random Forest Regressor` and `Partial Dependence Plot`.
                - Using `LSTM` to `Predict the future 'Weekly_Sales' by different shop clusters` to help optimize the stocking strategy.
            ''',
            'access': '''
                - 🔗 [Access link](https://walmart-casestudy-leanlinmy.my.canva.site/)
                - 👾 [GitHub Code Link](https://github.com/xphoenixx32/case_study/blob/e5288101aeb8f9292dc6b2e9433e3e53842e7d89/factor_analysis_on_walmart_sales_performance.ipynb)
            '''
        }
    },
    'work':{
        'ls':{
            'name':'''
                #### *Guidelines for Early-Life Live Stream Sellers*
            ''',
            'info':'''
                - Using `Random Forest Regressor` & `EDA` to assess the most influential key factors that drive live stream success.
                - Compiling the insights into an executive summary for the Live Streaming Team to `help build up Guidelines`.
            '''
        },
        'dws':{
            'name':'''
                #### *Build a Local Data Warehouse of Integrated Consumer Segmentations for Taiwan Business*
            ''',
            'info':'''
                - `Standardize consumer segmentation` by aligning different departments' goals and integrating them with existing academic frameworks. 
                - Over `60+` User Features retrievedd from `8` different tables has been built into a local data warehouse (ETL) for `Enhancing Marketing Efficiency` and to `Improve Analysis Quality`.
                - `Reduce computation time by 40%` and potentially `save an average of 6 hours per week` in manual data retrieval efforts. 
            '''
        },
        'rfm':{
            'name':'''
                #### *RFM Clustering for CLV Prediction* ***(on-going)***
            ''',
            'info':'''
                - Using RFM Features to `Classified Consumer into Meaningful Groups` to help seek high CLV Users to:
                    - Improving `Cost-Efficiency` (Target on Right Users)
                    - Prevent Potential Loss on A1 & Buyers (`Churn-Preventing` Strategy)
                - `Predict the future behavior patterns` on whether the User will:
                    - Login
                    - Purchase
                    - Create Incremental Orders
            ''',
            'access': '''
                🔗 [Access link](https://twilight-torta-0ee.notion.site/RFM-Clustering-for-CLV-Prediction-2ae71451866f431ebb3d156783c7ddea)
            '''
        }
    }
}
