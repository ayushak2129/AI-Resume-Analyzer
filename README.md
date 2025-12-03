# 🧠 AI Resume Analyzer (Django + NLP)

A Django-based AI Resume Analyzer that extracts text from PDF/DOCX resumes, parses key sections using rule-based NLP, and compares resume skills with Job Descriptions (JD) to generate a match percentage.  
Features an ATS-style dashboard with color-coded matched/missing skills and structured resume insights.

---

## 🚀 Features

### 📄 Resume Processing
- Upload resume in **PDF** or **DOCX** format  
- Extract raw text using **PyPDF2** and **python-docx**  
- Identify and parse key resume sections:
  - Education  
  - Experience  
  - Skills  
  - Projects  
  - Certifications  
  - Summary  

### 🧠 NLP-Based Information Extraction
- Extract **degrees** (B.Tech, B.Sc, MCA, etc.)  
- Extract **years of experience**  
- Detect **company names**  
- Detect **programming languages**  
- Structured resume analysis using rule-based NLP + regex  

### 🎯 Job Description (JD) Matching
- Paste any Job Description into the system  
- Extract JD skill keywords  
- Compare JD vs resume skills  
- Display:
  - Matched Skills (Green tags)  
  - Missing Skills (Red tags)  
  - JD Match Percentage  

### 🖥️ Clean ATS-Style Dashboard
- Modern card UI with color-coded badges  
- Clear separation of parsed sections  
- Professional result layout for recruiters  

---

AIResumeAnalyzer/
│
├── analyzer/
│ ├── ai/
│ │ ├── extractor.py # Extract PDF/DOCX text
│ │ ├── parser.py # NLP section parsing + skill extraction
│ │ └── analyzer.py # JD matching logic
│ ├── views.py # upload + analyze views
│ ├── urls.py
│ └── templates/analyzer/
│ ├── upload.html # Upload page
│ └── result.html # Dashboard view
│
├── resumeai/
│ ├── settings.py
│ └── urls.py
│
└── manage.py


---

## 🔧 Installation & Setup

### 1️⃣ Clone the repository
```bash
git clone https://github.com/YOUR_USERNAME/AIResumeAnalyzer.git
cd AIResumeAnalyzer

2️⃣ Create a virtual environment
python -m venv venv
venv\Scripts\activate    # Windows

3️⃣ Install dependencies
pip install -r requirements.txt

4️⃣ Run migrations
python manage.py makemigrations
python manage.py migrate

5️⃣ Start the Django server
python manage.py runserver

🛠️ Tech Stack

Python

Django

PyPDF2

python-docx

HTML5

CSS3

Regex / Rule-Based NLP

Git & GitHub

📊 How It Works (High Level)

User uploads a resume + optional Job Description

Text extracted using PDF/DOCX parsers

NLP parser identifies resume sections

Additional extractors derive:

Degrees

Experience

Company names

Programming languages

JD keywords extracted from provided Job Description

Logic compares JD skills with resume skills

Final ATS-style dashboard shows:

Parsed sections

Extracted details

Matched/missing skills

JD Match Percentage

📌 Future Enhancements (Optional)

Add ML-based semantic matching

Add resume scoring model

Add support for more resume layouts

Export results as PDF

🤝 Contributions

Pull requests are welcome.
If you’d like new features added, feel free to open an issue.

⭐ Show Support

If you found this useful, give the repository a star 🌟


---

# 🔥 Want a more advanced README with screenshots?
I can also generate a **README with images**, **badges**, **GIF demo**, or even a **logo header**.

Just say:  
👉 “Add screenshots & badges to my README.”

