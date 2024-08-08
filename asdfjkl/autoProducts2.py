### I ain't using this one just yet i fucked everything up



import csv
import json


def load_elective_data(file_path):
    with open(file_path, 'r') as f:
        elective_data = json.load(f)
    return elective_data


def generate_chapter_html(chapters):
    chapter_html = ""
    for i, chapter in enumerate(chapters, start=1):
        chapter_html += f"<p><span style='font-size: 12pt;'>Chapter {i}: {chapter}</span></p>"
    return chapter_html


def generate_7hr_html():
    sevenhr_html = """ <p style="text-align: left;"> </p>
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
            <p style="text-align: left;"> </p>
            """
    return sevenhr_html

def generate_final_html():
    final_html = f"""
        <p><span style="font-size: 12pt;"><strong>***This live webinar course includes only the {course_duration} hours of {elective_info.get('elective_name', '')} CE material. If you need additional state education, those can be found <a href="https://mortgageeducators.com/articles?id=751" target="_blank" rel="noopener noreferrer">HERE</a> in an online format***</strong></span></p>
        <p style="text-align: left;"><span style="font-size: 12pt;">Includes the ${banking_fee} NMLS banking fee. </span></p>
        <p style="text-align: left;"><span style="font-size: 12pt;">This course is in a live webinar format and requires the student to be active and pay attention the entire time. Control measures will be taken to ensure   
         participation. </span></p>
        <p style="text-align: left;"><span style="font-size: 12pt;">Questions: <a href="mailto:webinar@MortgageEducators.com">webinars@MortgageEducators.com</a></span></p>
        <p style="text-align: left;"><span style="font-size: 12pt;">NMLS Provider #1400062</span></p> 
        <!-- 2024 7 + 1 Hour {elective_info.get('elective_name', '')} CE Webinar {row['course_date']} {row['start_time']} {row['timezone']} -->
        """
    return final_html






def generate_course_html(csv_file, elective_file, elective_column="elective", is_7plus_column="is_7plus1", elective_duration_column="elective_duration"):
    elective_data = load_elective_data(elective_file)

    with open(csv_file, 'r') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            try:
                elective = row[elective_column]
                elective_info = elective_data.get(elective, {})
                elective_duration = elective_data.get('elective_duration', 0)
                course_duration = row[course_duration]
                html_content = f"""
                <p><a title="Click to learn more about {row['instructor_fname']}!" href="https://mortgageeducators.com/instructors" target="_blank" rel="noopener noreferrer"><img style="display: block; margin-left: auto; margin-right: auto;" src="https://mortgageeducators.com/images/00TemplateImages/Product_Banner/{row['instructor_fname']}_Banner.png" alt="" /></a></p>
                <p style="text-align: center;"> </p>
                <p style="text-align: center;"><span style="font-size: 18pt;"><strong>Date: </strong>{row['course_date']}</span></p>
                <p style="text-align: center;"><span style="font-size: 18pt;"><strong>Start Time: </strong>{row['start_time']} - {row['end_time']} {row['timezone']} Time</span></p>
                <p style="text-align: center;"><span style="font-size: 18pt;">(8:00 AM PT / 10:00 AM CT / 11:00 AM ET)</span></p>
                <p style="text-align: center;"> </p>
                <p style="text-align: center;"><span style="text-decoration: underline; font-size: 24pt;"><strong>2024 {course_duration} Hour {elective_info.get('elective_name', '')} CE Webinar</strong></span></p>
                <p style="text-align: center;"> </p>
                <p style="text-align: center;"><span style="font-size: 14pt;">  This course fulfills the {course_duration} Hour {elective_info.get('elective_name', '')} NMLS mortgage continuing education requirement for 2024 in a live webinar format. </span></p>
                <p style="text-align: center;"> </p>
                <p><a title="NMLS Webcam Requirement" href="https://nationwidelicensingsystem.org/courseprovider/Course%Provider%Resources/Functional%Specification%for%All%NMLS%Approved%Courses.pdf#page=27" target="_blank" rel="noopener noreferrer"><img style="display: block; margin-left: auto; margin-right: auto;" title="NMLS Webcam Requirement" src="https://mortgageeducators.com/images/00TemplateImages/webcam4.png" alt="Webcam Required, Per NMLS as of June 6th, 2022." width="652" height="129" /></a></p>
                <p style="text-align: left;"><span style="text-decoration: underline; font-size: 14pt;"><strong>Course Content:</strong></span></p>
                <p><span style="font-size: 10pt;"><em><span style="color: #ff0000;">*Courses will be taught in the following order*</span></em></span></p>
                <p> </p>
                <p><span style="text-decoration: underline; font-size: 12pt;"><strong>{elective_duration} Hour {elective_info.get('elective_name', '')} Elective: {elective_info.get('course_number', '')}</strong></span></p>
                """
                html_content += generate_chapter_html(elective_info.get('chapters', []))
                if row['is_7plus1'] == 'yes':
                      html_content += generate_7hr_html()

                html_content += generate_final_html()

                filename = f"{row['instructor_fname']}-{row['course_date']}.html"

                with open(filename, 'a', encoding='utf-8') as output_file:
                    output_file.write(html_content)
            except Exception as e:
                print({e})

csv_file = "test2.csv"
elective_file = "../work/elective_data.json"
generate_course_html(csv_file, elective_file, is_7plus_column="is_7plus1", elective_duration_column="elective_duration")
