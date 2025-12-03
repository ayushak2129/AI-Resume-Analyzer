def compare_resume_with_jd(resume_skills, jd_skills):
    resume_set = set([s.lower() for s in resume_skills])
    jd_set = set([s.lower() for s in jd_skills])

    matched = list(resume_set.intersection(jd_set))
    missing = list(jd_set - resume_set)

    if len(jd_set) == 0:
        match_percent = 0
    else:
        match_percent = round((len(matched) / len(jd_set)) * 100, 2)

    return match_percent, matched, missing
