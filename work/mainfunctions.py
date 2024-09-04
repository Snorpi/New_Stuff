import os
import csv
import functions as fc


def generate_lms_description(csv_file, elective_file, instructor_file):
    elective_data = fc.load_elective_data(elective_file)
    instructor_data = fc.load_instructor_data(instructor_file)
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
                et = row['end_time']
                timezonelist = f"({row['PT']} PT / {row['MT']} MT / {row['CT']} CT / {row['ET']} ET)"
                course_number = elective_info.get('course_number')
                course_date = row['course_date']
                html_content = f"""
                <!-- Course Title -->
                <!-- Webinar {elective_duration} Hour {elective_name} Elective CE {course_number} {course_date}, 2024 {st} {tz} -->
                
                <!-- Course Certificate Info -->
                <!-- {elective_duration} Hour {elective_name} {course_number} Certificate
                
                Is proud to announce that

                #name#
                
                with NMLS number #reg_answer# 
                
                has completed the requirements necessary for the
                
                {elective_duration} Hour {elective_name}
                Webinar Course (ID {course_number})
                
                completed on {course_date}, 2024. 
                -->
                
                <!-- Top Information -->
                <table width="80%" align="center">
                <tbody>
                <tr>
                <td>
                <h1 style="font-weight: 600; text-align: center;">2024 Live WEBINAR<br /> NMLS {elective_duration} Hour {elective_name} Continuing Education Course</h1>
                <h1 style="font-weight: 600; text-align: center;">{course_date}, 2024</h1>
                </td>
                </tr>
                </tbody>
                </table>
                
                <!-- Bottom Information -->
                <p><img style="display: block; margin-left: auto; margin-right: auto;" src="https://mortgageeducators.com{instructor_image}" alt="" /></p>
                <p style="text-align: center;">
                <span style="font-size: 24pt;"><strong>
                <a title="Click to learn more about {instructor}!" href="https://mortgageeducators.com/instructors{instructor_info.get('pageanchor')}" target="_blank" rel="noopener noreferrer">{instructor_fullname}</a></strong></span></p>
                <p> </p>
                <p style="text-align: center;"><span style="font-size: 14pt;"><strong>{elective_duration} Hour {elective_name} Elective</strong></span></p>
                <p style="text-align: center;"><span style="font-size: 12pt;"><strong>{st} - {et} {tz} Time</strong></span></p>
                <p style="text-align: center;"><span style="font-size: 10pt;">{timezonelist}</span></p>
                <p> </p>
                <p style="text-align: center;"><img src="https://mortgageeducators.com/images/webinar/Webcam_Required_Banner.png" alt="" /></p>
                <p style="text-align: center;"><strong><span style="font-size: 10pt;">This course has been approved by the NMLS to fulfill the {elective_duration} hour of Continuing Education requirement for {elective_name} outlined in the SAFE Act for mortgage loan originators and brokers. </span>
                <span style="font-size: 10pt;">Per NMLS requirements, all webinar attendees are required to have a webcam enabled for the entire duration of all webinars for NMLS credit.</span></strong></p>
                <p style="text-align: center;">  <strong>NMLS Course {course_number}<br /></strong><strong>NMLS Provider # 1400062 </strong>  </p>
                """

                output_dir = "C:\\Users\\tbone\\PycharmProjects\\MyNewMainStuff\\work\\lmsDescriptions"
                filename = os.path.join(output_dir, f"{course_date}-lms-{elective}.html")

                with open(filename, 'a', encoding='utf-8') as output_file:
                    output_file.write(html_content)
            except Exception as e:
                print(f"{row['course_date']}-{elective_name}: Problem - {e}")


def generate_standalone_product(csv_file, elective_file, instructor_file):
    elective_data = fc.load_elective_data(elective_file)
    instructor_data = fc.load_instructor_data(instructor_file)

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
                instructor_banner = instructor_info.get('bannerlink')
                tz = row['timezone']
                st = row['start_time']
                et = row['end_time']
                timezonelist = f"({row['PT']} PT / {row['MT']} MT / {row['CT']} CT / {row['ET']} ET)"
                course_number = elective_info.get('course_number')
                course_url = f"""{row['Month']}-{row['Day']}-24-{elective_duration}-{elective}-ceq"""
                cd = row['course_date']
                banking_fee = int(elective_info.get('elective_duration')) * 1.50
                html_content = f"""
                <p><a title="Click to learn more about {instructor}!" href="https://mortgageeducators.com/instructors" target="_blank" rel="noopener noreferrer"><img style="display: block; margin-left: auto; margin-right: auto;" src="https://mortgageeducators.com{instructor_banner}" alt="" /></a></p>
                <p> </p>
                <p style="text-align: center;"><span style="font-size: 18pt;"><strong>Date: </strong>{cd}, 2024</span></p>
                <p style="text-align: center;"><span style="font-size: 18pt;"><strong>Start Time: </strong>{st} - {et} {tz} Time</span></p>
                <p style="text-align: center;"><span style="font-size: 18pt;">{timezonelist} ET)</span></p>
                <p> </p>
                <p style="text-align: center;"><span style="text-decoration: underline; font-size: 24pt;"><strong>2024 {elective_duration} Hour {elective_name} CE Webinar</strong></span></p>
                <p> </p>
                <p style="text-align: center;"><span style="font-size: 14pt;">  This course fulfills the {elective_duration} Hour {elective_name} NMLS mortgage continuing education requirement for 2024 in a live webinar format. </span></p>
                <p> </p>
                <p><a title="NMLS Webcam Requirement" href="https://nationwidelicensingsystem.org/courseprovider/Course%Provider%Resources/Functional%Specification%for%All%NMLS%Approved%Courses.pdf#page=27" target="_blank" rel="noopener noreferrer"><img style="display: block; margin-left: auto; margin-right: auto;" title="NMLS Webcam Requirement" src="https://mortgageeducators.com/images/00TemplateImages/webcam4.png" alt="Webcam Required, Per NMLS as of June 6th, 2022." width="652" height="129" /></a></p>
                <p style="text-align: left;"><span style="text-decoration: underline; font-size: 14pt;"><strong>Course Content:</strong></span></p>
                <p><span style="font-size: 10pt;"><em><span style="color: #ff0000;">*Courses will be taught in the following order*</span></em></span></p>
                <p> </p>
                <p><span style="text-decoration: underline; font-size: 12pt;"><strong>{elective_duration} Hour {elective_name} Elective: NMLS {course_number}</strong></span></p>
                """

                html_content += fc.generate_chapter_html(elective_info.get('chapters', []))

                html_content += f"""
                <p><span style="font-size: 12pt;"><strong>***This live webinar course includes only the {elective_duration} hour(s) of {elective_name} CE material. If you need additional state education, those can be found <a href="https://mortgageeducators.com/articles?id=751" target="_blank" rel="noopener noreferrer">HERE</a> in an online format***</strong></span></p>
                <p style="text-align: left;"><span style="font-size: 12pt;">Includes the ${banking_fee}0 NMLS banking fee. </span></p>
                <p style="text-align: left;"><span style="font-size: 12pt;">This course is in a live webinar format and requires the student to be active and pay attention the entire time. Control measures will be taken to ensure   
                 participation. </span></p>
                <p style="text-align: left;"><span style="font-size: 12pt;">Questions: <a href="mailto:webinar@MortgageEducators.com">webinars@MortgageEducators.com</a></span></p>
                <p style="text-align: left;"><span style="font-size: 12pt;">NMLS Provider #1400062</span></p> 
                
                
                <!-- Product Information -->
                <!-- 2024 {elective_duration} Hour {elective_name} CE Webinar {cd}, 2024 {st} {tz} -->
                <!-- {row['Month']}.{row['Day']}.2024 {elective_duration}hr {elective} CEQ -->
                <!-- {course_url} -->
                <!-- {row['Month']}/{row['Day']} - {elective_duration} Hour {elective_name} CE Webinar -->
                <!-- asana info -->
                <!-- {elective_duration}Hr {elective} 
                <h2 style="text-align: center">
                <a
                title="{elective_duration} Hour {elective_name} CE Webinar - {cd}"
                href="https://mortgageeducators.com/component/virtuemart/{course_url}-detail"
                target="_blank"
                rel="noopener noreferrer"
                >{elective_duration} Hour {elective_name} CE Webinar - {cd}</a
                >
                </h2>
                """

                output_dir = "C:\\Users\\tbone\\PycharmProjects\\MyNewMainStuff\\work\\productDescriptions"
                filename = os.path.join(output_dir, f"{elective}-{instructor_info.get('fname')}-{cd}.html")

                with open(filename, 'a', encoding='utf-8') as output_file:
                    output_file.write(html_content)
            except Exception as e:
                print(f"{cd}-{elective_name}: Problem - {e}")



def generate_7_1_html(csv_file, elective_file, instructor_file):
    elective_data = fc.load_elective_data(elective_file)
    instructor_data = fc.load_instructor_data(instructor_file)

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
                instructor_banner = instructor_info.get('bannerlink')
                tz = row['timezone']
                st = row['start_time']
                et = row['end_time']
                timezonelist = f"({row['PT']} PT / {row['MT']} MT / {row['CT']} CT / {row['ET']} ET)"
                course_number = elective_info.get('course_number')
                cd = row['course_date']
                pageanchor = instructor_info.get('pageanchor')
                banking_fee = int(elective_info.get('elective_duration')) * 1.50 + 10.5
                course_url = f"""{row['Month']}-{row['Day']}-24-7-{elective_duration}-{elective}-ceq"""
                html_content = f"""
                <p><a title="Click to learn more about {instructor}!" href="https://mortgageeducators.com/instructors{pageanchor}" target="_blank" rel="noopener noreferrer"><img style="display: block; margin-left: auto; margin-right: auto;" src="https://mortgageeducators.com{instructor_banner}" alt="{instructor} Banner" /></a></p>
                <p> </p>
                <p style="text-align: center;"><span style="font-size: 18pt;"><strong>Date: </strong>{cd}, 2024</span></p>
                <p style="text-align: center;"><span style="font-size: 18pt;"><strong>Start Time: </strong>{st} - {et} {tz} Time</span></p>
                <p style="text-align: center;"><span style="font-size: 18pt;">{timezonelist}</span></p>
                <p> </p>
                <p style="text-align: center;"><span style="text-decoration: underline; font-size: 24pt;"><strong>2024 7 + {elective_duration} Hour {elective_name} CE Webinar</strong></span></p>
                <p> </p>
                <p style="text-align: center;"><span style="font-size: 14pt;">  This course fulfills the 7 + {elective_duration} Hour {elective_name} NMLS mortgage continuing education requirement for 2024 in a live webinar format. </span></p>
                <p> </p>
                <p><a title="NMLS Webcam Requirement" href="https://nationwidelicensingsystem.org/courseprovider/Course%Provider%Resources/Functional%Specification%for%All%NMLS%Approved%Courses.pdf#page=27" target="_blank" rel="noopener noreferrer"><img style="display: block; margin-left: auto; margin-right: auto;" title="NMLS Webcam Requirement" src="https://mortgageeducators.com/images/00TemplateImages/webcam4.png" alt="Webcam Required, Per NMLS as of June 6th, 2022." width="652" height="129" /></a></p>
                <p style="text-align: left;"><span style="text-decoration: underline; font-size: 14pt;"><strong>Course Content:</strong></span></p>
                <p><span style="font-size: 10pt;"><em><span style="color: #ff0000;">*Courses will be taught in the following order*</span></em></span></p>
                <p> </p>
                <p><span style="text-decoration: underline; font-size: 12pt;"><strong>{elective_duration} Hour {elective_name} Elective: NMLS {course_number}</strong></span></p>
                """

                html_content += fc.generate_chapter_html(elective_info.get('chapters', []))
                html_content += fc.generate_7hr_html()
                html_content += f"""
                <p style="text-align: left;"> </p>`
                <p><span style="font-size: 12pt;"><strong>***This live webinar course includes only the 7 + {elective_duration} hours of {elective_name} CE material. If you need additional state education, those can be found <a href="https://mortgageeducators.com/articles?id=751" target="_blank" rel="noopener noreferrer">HERE</a> in an online format***</strong></span></p>
                <p style="text-align: left;"><span style="font-size: 12pt;">Includes the ${banking_fee}0 NMLS banking fee. </span></p>
                <p style="text-align: left;"><span style="font-size: 12pt;">This course is in a live webinar format and requires the student to be active and pay attention the entire time. Control measures will be taken to ensure   
                 participation. </span></p>
                <p style="text-align: left;"><span style="font-size: 12pt;">Questions: <a href="mailto:webinar@MortgageEducators.com">webinars@MortgageEducators.com</a></span></p>
                <p style="text-align: left;"><span style="font-size: 12pt;">NMLS Provider #1400062</span></p> 
                <!-- 2024 7 + {elective_duration} Hour {elective_name} CE Webinar {cd}, 2024 {st} {tz} -->
                <!-- {row['Month']}.{row['Day']}.2024 - 7 + {elective_duration} {elective} CEQ -->
                <!-- {course_url} -->
                <!-- {row['Month']}/{row['Day']} - 7 + {elective_duration} Hour {elective} CE Webinar -->
                <!-- asana info -->
                <!-- {elective_duration}Hr {elective} 
                <h2 style="text-align: center">
                <a
                title="7 + {elective_duration} Hour {elective_name} CE Webinar - {cd}"
                href="https://mortgageeducators.com/component/virtuemart/{course_url}-detail"
                target="_blank"
                rel="noopener noreferrer"
                >7 + {elective_duration} Hour {elective_name} CE Webinar - {cd}</a
                >
                </h2>
                """

                output_dir = "C:\\Users\\tbone\\PycharmProjects\\MyNewMainStuff\\work\\productDescriptions"
                filename = os.path.join(output_dir, f"{elective}-{instructor}-{cd}.html")

                with open(filename, 'a', encoding='utf-8') as output_file:
                    output_file.write(html_content)
            except Exception as e:
                print(f"{cd}-{elective}: Problem - {e}")




csv_file = "csv/lms_desc.csv"
elective_file = "json/elective_data.json"
instructor_file = "json/instructors.json"


# Example Usage

# For LMS Title, Certificate Title, Certificate Info, Course Information Pages
generate_lms_description(csv_file, elective_file, instructor_file)

# For Generating state elective product descriptions, title, alias, sku, page title, link
# generate_standalone_product(csv_file, elective_file, instructor_file)

# For generating 7+1 product descriptions, title, alias, sku, page title, link
# generate_7_1_html(csv_file, elective_file, instructor_file)
