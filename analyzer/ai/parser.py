# parser.py
# Extracts structured sections from resume text using rule-based parsing.

import re

# Section keywords used to detect headings
SECTION_HEADERS = {
    "education": ["education", "academics", "qualification"],
    "experience": ["experience", "work experience", "employment"],
    "projects": ["projects", "project work", "academic projects"],
    "skills": ["skills", "technical skills", "core skills"],
    "certifications": ["certifications", "courses", "training"],
    "summary": ["summary", "objective", "about me", "profile"],
}

def find_sections(text):
    """
    Identify all section headers and their positions using regex.
    Returns a dictionary with {section_name: index_position}
    """

    section_positions = {}

    for section, keywords in SECTION_HEADERS.items():
        for keyword in keywords:
            pattern = r"\b" + re.escape(keyword) + r"\b"
            match = re.search(pattern, text.lower())
            if match:
                section_positions[section] = match.start()

    return section_positions


def extract_sections(text):
    """
    Extracts content for each section by locating header positions 
    and slicing the text accordingly.
    Returns a dictionary: {section_name: section_text}
    """

    positions = find_sections(text)

    # Sort sections by position in resume
    ordered_sections = sorted(positions.items(), key=lambda x: x[1])

    result = {}

    for i, (section, start_pos) in enumerate(ordered_sections):
        # End at next section's start or end of text
        if i + 1 < len(ordered_sections):
            _, next_pos = ordered_sections[i + 1]
            section_text = text[start_pos:next_pos]
        else:
            section_text = text[start_pos:]

        result[section] = clean_section_text(section_text)

    return result


def clean_section_text(text):
    """
    Removes the section header line and trims whitespace.
    """

    lines = text.split("\n")
    if len(lines) > 1:
        cleaned = "\n".join(lines[1:]).strip()
    else:
        cleaned = text.strip()

    return cleaned


def extract_years_of_experience(text):
    """
    Extracts total years of experience from resume using regex patterns.
    Returns an integer or None.
    """

    patterns = [
        r"(\d+)\s*\+?\s*years",
        r"(\d+)\s*yrs",
        r"(\d+)\s*year experience",
        r"experience\s*[:\-]?\s*(\d+)",
    ]

    for pattern in patterns:
        match = re.search(pattern, text.lower())
        if match:
            return int(match.group(1))

    return None

DEGREE_KEYWORDS = [
    "b.tech", "btech",
    "b.e", "be",
    "b.sc", "bsc",
    "m.tech", "mtech",
    "m.e", "me",
    "m.sc", "msc",
    "diploma",
    "mba",
    "bca", "mca",
]

def extract_degrees(text):
    """
    Detects degree names in resume text.
    Returns a list of degrees found.
    """

    text_lower = text.lower()
    found = []

    for degree in DEGREE_KEYWORDS:
        if degree in text_lower:
            found.append(degree.upper())

    return found

def extract_company_names(text):
    """
    Extracts potential company names using simple regex patterns.
    """

    companies = set()

    # Pattern for names like 'Infosys', 'TCS', 'Google'
    simple_company_pattern = r"\b([A-Z][a-zA-Z0-9&.\- ]{2,})\b (?:Pvt|Ltd|Technologies|Systems|Labs)"

    # Pattern for 'Worked at XYZ'
    worked_at_pattern = r"worked at ([A-Z][a-zA-Z0-9&.\- ]+)"

    # Pattern for 'Company: XYZ'
    company_colon_pattern = r"company[:\-]?\s*([A-Z][a-zA-Z0-9&.\- ]+)"

    for pattern in [simple_company_pattern, worked_at_pattern, company_colon_pattern]:
        matches = re.findall(pattern, text)
        for m in matches:
            companies.add(m.strip())

    return list(companies)


PROGRAMMING_LANGS = [
    "python", "java", "c++", "c#", "javascript",
    "typescript", "ruby", "php", "scala", "go",
    "html", "css", "sql",
]

def extract_programming_languages(text):
    """
    Extracts programming languages from resume.
    """

    text_lower = text.lower()
    found = []

    for lang in PROGRAMMING_LANGS:
        if lang in text_lower:
            found.append(lang.upper())

    return found

def parse_additional_details(text):
    """
    Runs all rule-based extractors and returns a structured dictionary.
    """

    return {
        "years_of_experience": extract_years_of_experience(text),
        "degrees": extract_degrees(text),
        "company_names": extract_company_names(text),
        "programming_languages": extract_programming_languages(text),
    }

import re

SKILL_KEYWORDS = [
    # Programming
    "python", "java", "c++", "c#", "javascript", "go", "typescript",
    "html", "css", "sql", "bash", "shell",

    # Frameworks
    "django", "flask", "spring", "react", "angular", "node", "express",

    # Testing tools
    "selenium", "junit", "testng", "pytest", "postman",

    # Databases
    "mysql", "postgres", "oracle", "mongodb",

    # DevOps & tools
    "git", "docker", "kubernetes", "jenkins", "aws",

    # Concepts
    "sdlc", "stlc", "automation", "manual testing",
    "test cases", "test plans", "bug tracking",
]

def extract_keywords_from_jd(jd_text):
    """
    Extracts relevant skill keywords from the Job Description.
    Case-insensitive keyword search.
    """
    jd_text = jd_text.lower()
    found = []

    for skill in SKILL_KEYWORDS:
        if skill in jd_text:
            found.append(skill)

    return found
