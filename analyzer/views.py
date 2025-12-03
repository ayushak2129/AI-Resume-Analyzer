from django.shortcuts import render
from .ai.extractor import extract_resume_text  # import your extractor
from .ai.parser import extract_sections, parse_additional_details
from .ai.parser import extract_sections, parse_additional_details, extract_keywords_from_jd
from .ai.analyzer import compare_resume_with_jd 
# Create your views here.

def upload_resume(request):
    return render(request, 'analyzer/upload.html')

def upload_resume(request):
    return render(request, 'analyzer/upload.html')


def analyze_resume(request):
    if request.method == "POST":
        resume_file = request.FILES.get("resume_file")

        if resume_file:
            extracted_text = extract_resume_text(resume_file)
            return render(request, 'analyzer/result.html', {
                "extracted_text": extracted_text
            })

    return render(request, 'analyzer/upload.html')

def analyze_resume(request):
    if request.method == "POST":
        resume_file = request.FILES.get("resume_file")

        if resume_file:
            # Extract raw text
            extracted_text = extract_resume_text(resume_file)

            # Parse sections
            sections = extract_sections(extracted_text)

            # Additional details (years of exp, degrees, skills)
            extra = parse_additional_details(extracted_text)

            return render(request, 'analyzer/result.html', {
                "extracted_text": extracted_text,
                "sections": sections,
                "extra": extra,
            })

    return render(request, 'analyzer/upload.html')

def analyze_resume(request):
    if request.method == "POST":
        resume_file = request.FILES.get("resume_file")
        jd_text = request.POST.get("job_description", "")

        if resume_file:
            extracted_text = extract_resume_text(resume_file)
            sections = extract_sections(extracted_text)
            extra = parse_additional_details(extracted_text)

            # Resume skills come from extracted programming languages
            resume_skills = extra["programming_languages"]

            # Extract keywords from JD
            jd_keywords = extract_keywords_from_jd(jd_text)

            # Compare
            jd_match_percent, matched_keywords, missing_keywords = compare_resume_with_jd(
                resume_skills,
                jd_keywords
            )

            return render(request, 'analyzer/result.html', {
                "extracted_text": extracted_text,
                "sections": sections,
                "extra": extra,
                "jd_keywords": jd_keywords,
                "jd_match_percent": jd_match_percent,
                "matched_keywords": matched_keywords,
                "missing_keywords": missing_keywords,
            })

    return render(request, 'analyzer/upload.html')