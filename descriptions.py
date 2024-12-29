# --- Basics ---
WORK_NAME = "Lean Lin"
TC_NAME = "Ming Yan, Lin"
DESCRIPTION_a = """
_Senior Data Analyst with 5+ years experience_**
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
    'degree': '**Master Degree**, *Public Administration & Policy*',
    'school': 'National Taipei University',
    'period': '2017 Sep ~ 2021 Jan',
    'info':'''
        ##### _Thesis_**
        - **The Research on the Influence of Influencers’ Political Endorsement and Policy Marketing Effect:** *Using Internet Public Opinion Big Data to Analyze its Impact on Social Media* 
        - Thesis URL : 🔗 [Link](https://hdl.handle.net/11296/834k8b)
        ##### _Grade_**
        - GPA : _3.8_**  |  *4.0*
        ##### _Honor_**
        - *Phi Tau Phi Honorary Membership*
        - *The C. C. Chang Scholarship of Administrative Science*
        - *The Rotary Foundation Scholarship*
    '''
}

CAREER = {
    'shopee':{
        'title': '##### **Data Analyst, Business Intelligence**',
        'corp_name': '*Shopee*',
        'period': '2024 Jan ~ Present',
        'info': '''
            - Identify _potential opportunities_** and _plan actionable business improvement strategies_** from existing sales data.
            - _Develop and maintain Data Dashboards or Trackers_** for marketing analysis needs.
            - Assist in organizing and focusing on analysis requests from the MKT Campaign team, including but not limited to _consumer traffic, marketing campaign performance, and analysis on ordering incentives_**.
        '''
    },
    'ailabs':{
        'title': '##### **Lead Data Analyst**',
        'corp_name': '*Taiwan AiLabs*',
        'period': '2023 Feb ~ 2023 Dec',
        'info': '''
            - _Lead 3 Data Analysts_** and distribute the workload, organizing the needs from clients & senior management, and meeting the overall goals of the business unit's expectations.
            - _Utilizing community detection algorithms_** to group atypical accounts, also _detecting atypical behavior patterns_** on social media based on feature engineering & other ML methods. (2+ models for YouTube & TikTok)
            - Experienced in data visualization, _demonstrating evidence of coordinated inauthentic behaviors_**, and _concluding with insights about how collaborative groups manipulated_** specific information. (40+ reports)
        '''
    },
    'eland':{
        'title': '##### **Sr. Business Analyst**',
        'corp_name': '*eLand Information*',
        'period': '2019 Mar ~ 2023 Feb',
        'info': '''
            - _Providing conclusions and insights among various realms_** based on data-driven evidence. (realms including politics & policies, public relations, business analytics and marketing campaign)
            - Involved in data-related tasks such as _Data Cleaning, Data Integration, Data Transformation & Data Visualization_**, routinely delivering analytic reports. (100+ reports)
            - _Offering assistance and advice to clients_** to help deal with system-operating or data-processing issues. (clients including business group, ad agency and public sector) 
            - _Occasionally serve as a lecturer_** sharing thoughts or insights about Social Big Data and various quantitative methods. (25+ lectures or workshops)
        '''
    }
}

# --- Information of Skills ---
SKILLS = {
    'soft':'''
        ##### _Communication and Collaboration_** 🤝
        - *Clear Data Storytelling*
        - *Cross-Functional Collaboration*
        ##### _Critical Thinking and Problem-Solving_* 🧠
        - *Problem Decomposition*
        - *Logical Reasoning*
        - *Data-Driven Decision-Making*
        ##### _Adaptability and Growth Mindset_* 🌵
        - *Learning New Tools and Techniques*
        - *Adapting to Change*
    ''',
    'hard':'''
        ###### _Code & Data Tool_* 🐍
        - `Python`, `SQL`, `Streamlit`
        - `Looker Studio`, `Tableau`, `Power BI`
        - `Excel`, `Power Query`, `Power Pivot`
        ###### _Analytic Skills_* 🤖
        - `EDA` & `Data Mining`
        - `Data Visualization`
        - `Data Modeling`
        - `Machine Learning`
        - `Feature Engineering`
        - `ETL` & `Data Management`
        ###### _Certificate_** 🪪
        - *Google Business Intelligence Specialization*
    '''
}

# --- Information of Projects ---
PROJECTS = {
    'side':{
        'app':{
            'name':'''
                ##### *EDA Toolkit (Web app) - a Data Tool without any Coding*
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
                ##### *Business Case Study - Walmart Sales Factors Analysis & Forcasting*
            ''',
            'info':'''
                - This case study aimed to realize `how factors affect 'Weekly_Sales' of Walmart` and `what's the intersection effect between factors` by Using `K-means Clustering`, `RandomForrestRegressor` and `Partial Dependence Plot`.
                - Using `LSTM` to `Predict the future 'Weekly_Sales' by different shop clusters` to help optimize the stocking strategy.
            ''',
            'access': '''
                - 🔗 [access link](https://walmart-casestudy-leanlinmy.my.canva.site/)
                - 👾 [GitHub Code Link](https://github.com/xphoenixx32/case_study/blob/e5288101aeb8f9292dc6b2e9433e3e53842e7d89/factor_analysis_on_walmart_sales_performance.ipynb)
            '''
        }
    },
    'work':{
        'ls':{
            'name':'''
                ##### *Guidelines for Early-Life Live Stream Sellers*
            ''',
            'info':'''
                - Using `Random Forest Regressor` & `EDA` to assess the most influential key factors that drive live stream success.
                - Compiling the insights into an executive summary for the Live Streaming Team to `help build up Guidelines`.
            '''
        },
        'dws':{
            'name':'''
                ##### *Build a Local Data Warehouse of an Integrated Consumer Segmentation for Taiwan Business*
            ''',
            'info':'''
                - `Standardize consumer segmentation` by aligning different departments' goals and integrating them with existing academic frameworks. 
                - Over 60+ User Features be built into a local data warehouse (ETL) for `Enhancing Marketing Efficiency` and to `Improve Analysis Quality`.
                - `Reduce computation time by 40%` and potentially `save an average of 6 hours per week` in manual data retrieval efforts. 
            '''
        },
        'rfm':{
            'name':'''
                ##### *RFM Clustering for CLV Prediction* ***(on-going)***
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
                🔗 [access link](https://twilight-torta-0ee.notion.site/RFM-Clustering-for-CLV-Prediction-2ae71451866f431ebb3d156783c7ddea)
            '''
        }
    }
}
