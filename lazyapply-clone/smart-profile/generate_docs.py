import os
import json
from docx import Document
from datetime import datetime
import re

def generate_resume(profile_data, job_keywords):
    if not os.path.exists("resume_template.docx"):
        raise FileNotFoundError("resume_template.docx not found.")
    doc = Document("resume_template.docx")
    for p in doc.paragraphs:
        if "[SKILLS_MATCHED]" in p.text:
            matched = [k for domain in job_keywords for k in job_keywords[domain] if k.lower() in profile_data["skills"]]
            p.text = p.text.replace("[SKILLS_MATCHED]", ", ".join(set(matched)))
    doc.save(f"resume_{datetime.now().date()}.docx")

def generate_cover_letter(company, role):
    if not os.path.exists("cover_letter_template.txt"):
        raise FileNotFoundError("cover_letter_template.txt not found.")
    with open("cover_letter_template.txt") as f:
        letter = f.read()
    letter = letter.replace("[COMPANY_NAME]", company)
    letter = letter.replace("[ROLE_TITLE]", role)
    safe_company = re.sub(r'[\\/*?:"<>|]', "", company)
    if not safe_company:
        safe_company = "company"
    with open(f"cover_{safe_company}_{datetime.now().date()}.txt", "w") as f:
        f.write(letter)