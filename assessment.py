import streamlit as st
import pandas as pd
import time  # Import time for delay

# Initialize session state for navigation
if "submitted" not in st.session_state:
    st.session_state.submitted = False
if "score" not in st.session_state:
    st.session_state.score = 0

# Define domain-specific questions (20 per domain, progressing from basic to advanced)
assessment_questions = {
    "Data Science": [
        {"question": "Which data structure is used to store labeled data in Pandas?", "options": ["Array", "DataFrame", "Tuple", "Dictionary"], "answer": "DataFrame"},
        {"question": "What is the primary library for numerical computing in Python?", "options": ["Pandas", "NumPy", "Scikit-learn", "Matplotlib"], "answer": "NumPy"},
        {"question": "What does CSV stand for?", "options": ["Comma Separated Values", "Common Storage View", "Compact Structured Variables", "Columnar Separated Values"], "answer": "Comma Separated Values"},
        {"question": "Which function is used to check missing values in Pandas?", "options": ["isnull()", "isna()", "dropna()", "fillna()"], "answer": "isnull()"},
        {"question": "Which library is used for data visualization?", "options": ["Matplotlib", "Scikit-learn", "TensorFlow", "OpenCV"], "answer": "Matplotlib"},
           # Intermediate
        {"question": "Which type of algorithm is K-Means?", "options": ["Supervised", "Unsupervised", "Reinforcement", "None"], "answer": "Unsupervised"},
        {"question": "Which metric evaluates regression models?", "options": ["Accuracy", "RMSE", "F1-score", "Recall"], "answer": "RMSE"},
        {"question": "Which deep learning framework is developed by Google?", "options": ["PyTorch", "Theano", "TensorFlow", "Keras"], "answer": "TensorFlow"},
        {"question": "What is overfitting in machine learning?", "options": ["Model performs well on training but poorly on test data", "Model performs equally on train & test data", "Model fails to capture patterns", "None"], "answer": "Model performs well on training but poorly on test data"},
        {"question": "What does CNN stand for in deep learning?", "options": ["Convolutional Neural Network", "Computational Neural Net", "Complex Neural Network", "None"], "answer": "Convolutional Neural Network"},

        # Advanced
        {"question": "Which technique is used to handle text data in ML?", "options": ["Bag of Words", "TF-IDF", "Word Embeddings", "Stopword Removal"], "answer": "Word Embeddings"},
        {"question": "Which optimization algorithm is commonly used in deep learning?", "options": ["Gradient Descent", "Adam", "SGD", "Momentum"], "answer": "Adam"},
        {"question": "Which method is used for dimensionality reduction?", "options": ["PCA", "SVM", "Decision Trees", "Random Forest"], "answer": "PCA"},
        {"question": "Which regularization technique prevents overfitting?", "options": ["L1 & L2 Regularization", "Feature selection", "Hyperparameter tuning", "Gradient clipping"], "answer": "L1 & L2 Regularization"},
        {"question": "Which cloud service is best for deploying ML models?", "options": ["AWS SageMaker", "Google Cloud ML", "Azure ML", "IBM Watson"], "answer": "AWS SageMaker"}
    ],
    "Web Development": [
        {"question": "Which HTML tag is used to define the main content of a webpage?", "options": ["<div>", "<main>", "<section>", "<article>"], "answer": "<main>"},
        {"question": "Which CSS property sets text color?", "options": ["color", "text-color", "font-color", "foreground"], "answer": "color"},
        {"question": "Which tag is used for creating hyperlinks?", "options": ["<a>", "<link>", "<href>", "<hyperlink>"], "answer": "<a>"},
        {"question": "Which CSS property controls layout responsiveness?", "options": ["media-query", "grid", "flexbox", "margin"], "answer": "media-query"},
        {"question": "Which programming language is widely used for web backend development?", "options": ["JavaScript", "Python", "PHP", "Ruby"], "answer": "Python"},
          # Intermediate
        {"question": "Which JavaScript function prints output to the console?", "options": ["print()", "console.log()", "write()", "log.print()"], "answer": "console.log()"},
        {"question": "Which framework is commonly used for frontend web development?", "options": ["React", "Django", "Flask", "Spring"], "answer": "React"},
        {"question": "Which Python framework is used for web development?", "options": ["Django", "Flask", "FastAPI", "Node.js"], "answer": "Django"},
        {"question": "Which HTTP method is used to send data to a server?", "options": ["GET", "POST", "PUT", "DELETE"], "answer": "POST"},
        {"question": "What does AJAX stand for?", "options": ["Asynchronous JavaScript and XML", "Advanced JavaScript and XML", "Automated JavaScript and XHTML", "None"], "answer": "Asynchronous JavaScript and XML"},

        # Advanced
        {"question": "Which API enables real-time web communication?", "options": ["REST API", "GraphQL", "WebSockets", "SOAP"], "answer": "WebSockets"},
        {"question": "Which tool is used for package management in JavaScript?", "options": ["NPM", "Yarn", "Bower", "Webpack"], "answer": "NPM"},
        {"question": "What is WebAssembly used for?", "options": ["Run compiled code in the browser", "Improve HTML rendering", "Enhance JavaScript performance", "None"], "answer": "Run compiled code in the browser"},
        {"question": "Which database is best suited for handling large-scale data in web applications?", "options": ["MySQL", "PostgreSQL", "MongoDB", "SQLite"], "answer": "MongoDB"},
        {"question": "Which technology is used for serverless computing?", "options": ["AWS Lambda", "Azure Functions", "Google Cloud Functions", "IBM Cloud Functions"], "answer": "AWS Lambda"}
    ]
}
# If the user has submitted, show success page
if st.session_state.submitted:
    st.markdown(
    """
    <style>
        .centered {
            text-align: center;
            background-color: #f4f4f4;
            padding: 20px;
            border-radius: 10px;
        }
        .big-check {
            font-size: 80px;
            color: green;
        }
        .success-message {
            font-size: 26px;
            font-weight: bold;
        }
        .sub-message {
            font-size: 18px;
            color: gray;
        }
         div.stButton > button:first-child {
            background-color: #70236A; /* Green */
            color: white;
            border-radius: 8px;
            padding: 10px 20px;
            font-size: 16px;
            font-weight: bold;
            border: none;
            cursor: pointer;
            transition: 0.3s;
        }
        div.stButton > button:first-child:hover {
            background-color: #d2b4de; /* Darker Green */
        }
    </style>
    <div class="centered">
        <div class="big-check">☑️</div>
        <p class="success-message">Submission Successful</p>
        <p class="sub-message">Thank you for completing the assessment.</p>
    </div>
    """,
    unsafe_allow_html=True
)
   


    
    # View Score Button
    if st.button("View Score"):
        st.markdown("### 📊 Your Assessment Score")
        st.write(f"**Score:** {st.session_state.score}%")

        # Skill level determination
        if st.session_state.score >= 80:
            st.success("Skill Level: **Advanced**")
        elif st.session_state.score >= 50:
            st.info(" Skill Level: **Intermediate**")
        else:
            st.warning(" Skill Level: **Beginner**")

    st.stop()  # Stop execution to show only the success page
    
# Streamlit UI for assessment
st.title("  Skill Assessment")

# Select Domain
domain = st.selectbox("Choose your preferred domain:", list(assessment_questions.keys()))

if domain:
    st.subheader(f" {domain} Assessment")

    correct_answers = 0
    total_questions = len(assessment_questions[domain])

    # Store user responses
    user_responses = {}

    for i, question_data in enumerate(assessment_questions[domain]):
        st.markdown(f"**Q{i+1}: {question_data['question']}**")  # Removes extra space between question and answers
        user_choice = st.radio("", question_data["options"], index=None, key=f"q{i}", label_visibility="collapsed")  # Removes label spacing

        # Store user response
        user_responses[f"q{i}"] = user_choice

        # Check if the selected answer is correct
        if user_choice and user_choice == question_data["answer"]:
            correct_answers += 1

    # Submit Button
    if st.button("Submit Assessment"):
        if None in user_responses.values():
            st.warning(" Please answer all questions before submitting.")
        else:
            # Calculate Score
            st.session_state.score = (correct_answers / total_questions) * 100
            st.session_state.submitted = True  # Set session state to navigate to success page
            st.rerun()  # Reload the page



import streamlit as st

# Custom CSS to style the button
st.markdown(
    """
    <style>
        div.stButton > button {
            background-color: #70236A !important; /* Dark Purple */
            color: white !important; /* White Text */
            font-size: 16px !important;
            font-weight: bold !important;
            padding: 10px 20px !important;
            border: none !important;
            border-radius: 8px !important;
            cursor: pointer !important;
            transition: 0.3s !important;
        }
        div.stButton > button:hover {
            background-color: #5a1b55 !important; /* Slightly darker purple on hover */
        }
    </style>
    """,
    unsafe_allow_html=True,
)
st.markdown(
    """
    <style>
        /* Full page background color */
        body {
            background-color: #D2B4DE !important;
        }
        [data-testid="stAppViewContainer"] {
            background-color: #D2B4DE;
        }
        [data-testid="stSidebar"] {
            background-color: #5a1b55;
        }

        /* Style for Question Box */
        .question-box {
            background-color: white;
            padding: 15px;
            border-radius: 10px;
            box-shadow: 0px 4px 6px rgba(0, 0, 0, 0.1);
            margin-bottom: 20px;
        }

        /* Customizing radio buttons */
        div[data-testid="stRadio"] {
            background-color: white;
            padding: 10px;
            border-radius: 10px;
        }

        /* Style Submit Button */
        div.stButton > button {
            background-color: #ffffff !important;
            color: #70236A !important;
            font-size: 16px !important;
            font-weight: bold !important;
            padding: 10px 20px !important;
            border: none !important;
            border-radius: 8px !important;
            cursor: pointer !important;
            transition: 0.3s !important;
        }
        div.stButton > button:hover {
            background-color: #e0d7e6 !important;
        }
    </style>
    """,
    unsafe_allow_html=True,
)

