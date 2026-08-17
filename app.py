"""
app.py
------
Personal portfolio dashboard built with Streamlit.

Run locally with:
    streamlit run app.py

Edit the CONTENT section below (or better yet, edit data.py once you split
it out) to update your own education, experience, projects, and contact info.
"""

import streamlit as st

st.set_page_config(
    page_title="Gelana Abdisa Gemechis | Portfolio",
    page_icon="🎓",
    layout="wide",
)

# ---------------------------------------------------------------------------
# CONTENT — edit this section to update your info
# ---------------------------------------------------------------------------

NAME = "Gelana Abdisa Gemechis"
TITLE = "Lecturer & Department Head, Computer Science — Jimma University, Agaro Campus"
LOCATION = "Agaro, Oromia Region, Ethiopia"
TAGLINE = (
    "Machine learning and Deep learning researcher and educator focused on NLP for low-resource "
    "languages, computer vision, medical image analysis, and network security."
)

# Optional contact links — fill these in with your own, or leave blank to hide.
EMAIL = "gelana.abdisa@ju.edu.et"            # e.g. "gelana@example.com"
LINKEDIN_URL = "https://www.linkedin.com/in/gelana"     # e.g. "https://linkedin.com/in/your-profile"
GITHUB_URL = "https://github.com/gelanabadisa"       # e.g. "https://github.com/gelanabadisa"
PHONE = "+251921833044"            # e.g. "+251 9xx xxx xxx"

ABOUT = """
I am a Lecturer and Department Head of Computer Science at Jimma University,
Agaro Campus, Ethiopia. I teach machine learning,Data structure and algorithm, computer vision and image processing,
 Webprogramming, Design and analysis of algorihm, Research methods in computer science, professional ethics, and
computer skills, and I am connected to the Cisco Networking Academy
initiative at the campus.

My research spans natural language processing for low-resource languages
(especially Afaan Oromo), computer vision, medical image analysis, and
network security. I enjoy building applied ML systems end-to-end — from
data collection and model training to deployment as usable tools.
"""

EDUCATION = [
    {
        "degree": "MSc in Artificial Intelligence",
        "institution": "Jimma University",
        "period": "2022 - 2024",
        "details": "Graduate research and coursework in artificial intelligence.",
    },
    {
        "degree": "BSc in Information Science",
        "institution": "Jimma University",
        "period": "2018 -2021",
        "details": "Undergraduate foundation in information technology.",
    },
]

EXPERIENCE = [
    {
        "role": "Lecturer & Department Head, Computer Science",
        "organization": "Jimma University, Agaro Campus",
        "period": "Current",
        "details": [
            "Lead the Computer Science department at the Agaro Campus.",
            "Teach courses including Machine Learning, Professional Ethics, and Computer Skills.",
            "Connected to the Cisco Networking Academy initiative at the campus.",
        ],
    },
]

SKILLS = {
    "Machine Learning": ["Random Forest", "XGBoost", "LSTM / BiLSTM / Attention", "TensorFlow / Keras", "scikit-learn"],
    "NLP": ["Low-resource language modeling", "Text classification", "Corpus building"],
    "Computer Vision": ["Image classification", "Medical image analysis", "MobileNetV2 / MobileNetV3", "TFLite deployment"],
    "Other": ["Network Security", "Android (Kotlin)", "Full-stack web development", "Data pipelines & deployment"],
}

# Projects — edit freely. `link` is optional (leave "" if not public yet).
PROJECTS = [
    {
        "title": "DDoS Attack Detection (Attention-BiLSTM)",
        "description": (
            "Thesis project detecting DDoS attacks on the CIC-DDoS2019 dataset, "
            "comparing Attention-BiLSTM against BiLSTM, CNN-BiLSTM, BiGRU, Random "
            "Forest, and XGBoost across nine evaluation metrics."
        ),
        "tags": ["Deep Learning", "Network Security", "BiLSTM"],
        "link": "",
    },
    {
        "title": "Malaria Blood Smear Classifier",
        "description": (
            "End-to-end malaria diagnosis pipeline classifying blood smear images "
            "as Healthy, P. falciparum, or P. vivax. Trained MobileNetV2 and "
            "MobileNetV3-Large in Google Colab, converted to TFLite, and deployed "
            "as a working Kotlin Android app tested on a real device."
        ),
        "tags": ["Computer Vision", "Medical Imaging", "Android", "TFLite"],
        "link": "",
    },
    {
        "title": "Afaan Oromo Vigilante & Incitement Speech Detection",
        "description": (
            "Research project detecting vigilante and incitement speech in Afaan "
            "Oromo comment threads, comparing RNN, LSTM, Attention-LSTM, Bi-LSTM, "
            "and Attention-BiLSTM architectures on a 5-class labeled dataset."
        ),
        "tags": ["NLP", "Low-Resource Languages", "Deep Learning"],
        "link": "",
    },
    {
        "title": "Afaan Oromo Next-Word Prediction Corpus",
        "description": (
            "Building a large-scale synthetic Afaan Oromo corpus (~1 million words) "
            "for next-word prediction, using a Python generation pipeline with "
            "vocabulary banks and sentence templates."
        ),
        "tags": ["NLP", "Low-Resource Languages", "Data Engineering"],
        "link": "",
    },
    {
        "title": "SuqPOS — Point of Sale & Inventory App",
        "description": (
            "An entrepreneurial side project: a point-of-sale and inventory "
            "management application localized for the Ethiopian market, with "
            "ETB pricing and Amharic branding."
        ),
        "tags": ["Full-Stack", "Entrepreneurship"],
        "link": "",
    },
    {
        "title": "Jimma Hotel Booking & Reservation Platform",
        "description": (
            "Full-stack hotel booking website for Jimma, Ethiopia, with customer "
            "and admin flows, room browsing/booking with receipt upload, and "
            "support for local payment methods (Telebirr, CBE, Chapa, SantimPay)."
        ),
        "tags": ["Full-Stack", "Web Development"],
        "link": "",
    },
    {
        "title": "Python for AI — 100-Day Course",
        "description": (
            "Designed and delivered a 100-day Python/ML curriculum for undergraduate "
            "students using TensorFlow/Keras, teaching neural networks, calculus for "
            "ML, and the full supervised learning pipeline through an analogy-driven "
            "approach, using the malaria and DDoS projects as live case studies."
        ),
        "tags": ["Teaching", "Curriculum Design"],
        "link": "",
    },
]

# ---------------------------------------------------------------------------
# LAYOUT
# ---------------------------------------------------------------------------

# --- Header ---
col1, col2 = st.columns([1, 4])
with col1:
    st.markdown(
        f"""
        <div style="
            width:120px;height:120px;border-radius:50%;
            background:linear-gradient(135deg,#4F46E5,#06B6D4);
            display:flex;align-items:center;justify-content:center;
            color:white;font-size:42px;font-weight:700;">
            {''.join([n[0] for n in NAME.split()[:2]])}
        </div>
        """,
        unsafe_allow_html=True,
    )
with col2:
    st.title(NAME)
    st.subheader(TITLE)
    st.caption(f"📍 {LOCATION}")
    st.write(TAGLINE)

    contact_bits = []
    if EMAIL:
        contact_bits.append(f"📧 [{EMAIL}](mailto:{EMAIL})")
    if PHONE:
        contact_bits.append(f"📞 {PHONE}")
    if LINKEDIN_URL:
        contact_bits.append(f"[LinkedIn]({LINKEDIN_URL})")
    if GITHUB_URL:
        contact_bits.append(f"[GitHub]({GITHUB_URL})")
    if contact_bits:
        st.markdown(" &nbsp;|&nbsp; ".join(contact_bits))

st.divider()

# --- Navigation tabs ---
tab_about, tab_education, tab_experience, tab_skills, tab_projects = st.tabs(
    ["About", "Education", "Experience", "Skills", "Projects"]
)

with tab_about:
    st.header("About Me")
    st.write(ABOUT)

with tab_education:
    st.header("Education")
    for edu in EDUCATION:
        with st.container(border=True):
            st.markdown(f"**{edu['degree']}**")
            st.write(f"{edu['institution']}" + (f" · {edu['period']}" if edu["period"] else ""))
            if edu.get("details"):
                st.caption(edu["details"])

with tab_experience:
    st.header("Experience")
    for exp in EXPERIENCE:
        with st.container(border=True):
            st.markdown(f"**{exp['role']}**")
            st.write(f"{exp['organization']} · {exp['period']}")
            for point in exp["details"]:
                st.markdown(f"- {point}")

with tab_skills:
    st.header("Skills")
    cols = st.columns(2)
    for i, (category, items) in enumerate(SKILLS.items()):
        with cols[i % 2]:
            st.markdown(f"**{category}**")
            st.write(" · ".join(items))
            st.write("")

with tab_projects:
    st.header("Projects")
    st.write("A selection of research and applied projects.")
    for project in PROJECTS:
        with st.container(border=True):
            st.markdown(f"### {project['title']}")
            st.write(project["description"])
            if project.get("tags"):
                st.markdown(" ".join([f"`{tag}`" for tag in project["tags"]]))
            if project.get("link"):
                st.markdown(f"[View project]({project['link']})")

st.divider()
st.caption(f"© {NAME} · Built with Streamlit")
