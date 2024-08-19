import csv
import json


def load_elective_data(file_path):
    with open(file_path, 'r') as f:
        elective_data = json.load(f)
    return elective_data


def load_instructor_data(file_path):
    with open(file_path, 'r') as p:
        instructor_data = json.load(p)
    return instructor_data


def generate_course_html(csv_file, elective_file, instructor_file):
    elective_data = load_elective_data(elective_file)
    instructor_data = load_instructor_data(instructor_file)
    with open(csv_file, 'r') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            try:
                elective = row['elective']
                elective_info = elective_data.get(elective, {})
                elective_duration = elective_info.get('elective_duration', 0)
                elective_name = elective_info.get('elective_name')
                instructor = row['instructor']
                instructor_info = instructor_data.get(instructor, {})
                instructor_image = instructor_info.get('lmslink')
                instructor_fullname = f"{instructor_info.get('fname')} {instructor_info.get('lname')}"
                tz = row['timezone']
                st = row['start_time']
                course_number = elective_info.get('course_number')
                html_content = f"""
                <p><img style="display: block; margin-left: auto; margin-right: auto;" src="https://mortgageeducators.com/{instructor_image}" alt="" /></p>
                <p style="text-align: center;"><span style="font-size: 24pt;"><strong><a title="Click to learn more about {instructor_info.get('fname')}!" href="https://mortgageeducators.com/instructors{instructor_info.get('pageanchor')}" target="_blank" rel="noopener noreferrer">{instructor_fullname}</a></strong></span></p>
                <p> </p>
                <p style="text-align: center;"><span style="font-size: 14pt;"><strong>{elective_duration} Hour {elective_name} Elective</strong></span></p>
                <p style="text-align: center;"><span style="font-size: 12pt;"><strong>{st} - {row['end_time']} {tz} Time</strong></span></p>
                <p style="text-align: center;"><span style="font-size: 10pt;">({row['PT']} PT / {row['MT']} MT / {row['CT']} CT / {row['ET']} ET)</span></p>
                <p> </p>
                <p style="text-align: center;"><img src="https://mortgageeducators.com/images/webinar/Webcam_Required_Banner.png" alt="" /></p>
                <p style="text-align: center;"><strong><span style="font-size: 10pt;">This course has been approved by the NMLS to fulfill the {elective_duration} hour of Continuing Education requirement for {elective_name} outlined in the SAFE Act for mortgage loan originators and brokers. </span>
                <span style="font-size: 10pt;">Per NMLS requirements, all webinar attendees are required to have a webcam enabled for the entire duration of all webinars for NMLS credit.</span></strong></p>
                <p style="text-align: center;">  <strong>NMLS Course #15889<br /></strong><strong>NMLS Provider # 1400062 </strong>  </p>
                <!-- Webinar {elective_duration} Hour {elective_name} Elective CE {course_number} {row['course_date']}, 2024 {st} {tz} -->
                """

                filename = f"lms-{row['elective']}-{row['course_date']}.html"

                with open(filename, 'a', encoding='utf-8') as output_file:
                    output_file.write(html_content)
            except Exception as e:
                print(f"{row['course_date']}-{elective_name}: Problem - {e}")


csv_file = "tristan.csv"
elective_file = "elective_data.json"
instructor_file = "instructors.json"

generate_course_html(csv_file, elective_file, instructor_file)
