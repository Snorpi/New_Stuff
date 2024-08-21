import json


# loads elective json
def load_elective_data(file_path):
    with open(file_path, 'r') as f:
        elective_data = json.load(f)
    return elective_data


# loads instructor json
def load_instructor_data(file_path):
    with open(file_path, 'r') as p:
        instructor_data = json.load(p)
    return instructor_data


# gets chapter titles for product description
def generate_chapter_html(chapters):
    chapter_html = ""
    for i, chapter in enumerate(chapters, start=1):
        chapter_html += f"<p><span style='font-size: 12pt;'>Chapter {i}: {chapter}</span></p>"
    return chapter_html


# generates html for 7hr core
def generate_7hr_html():
    core_html = f"""
                <p><span style="text-decoration: underline; font-size: 12pt;"><strong>7 Hour SAFE CORE Continuing Education Course: NMLS #15898</strong></span></p>
                <p><span style="font-size: 12pt;">Chapter 1: Top 10 Violations</span></p>
                <p><span style="font-size: 12pt;">Chapter 2: Unfair, Deceptive, Abusive Acts and Practices (UDAAP)</span></p>
                <p><span style="font-size: 12pt;">Chapter 3: Loan Originator Compensation (LO Comp)</span></p>
                <p><span style="font-size: 12pt;">Chapter 4: Mortgage Fraud &amp; Money Laundering</span></p>
                <p><span style="font-size: 12pt;">Chapter 5: Fair Lending</span></p>
                <p><span style="font-size: 12pt;">Chapter 6: Renovation/Rehabilitation Mortgages: FHA 203(k)</span></p>
                <p><span style="font-size: 12pt;">Chapter 7: Non-Qualified Mortgages: How-To</span></p>
                <p style="margin-top: 9px; margin-bottom: 9px; border-width: initial; border-style: none; line-height: 17px; font-size: 15px; text-align: left;"> </p>
                <p style="margin-top: 9px; margin-bottom: 9px; border-width: initial; border-style: none; line-height: 17px; font-size: 15px; text-align: left;"><span style="font-size: 16px;">End of course group assessment</span></p>
        """
    return core_html

