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


def generate_7hrlms_description(csv_file, elective_file, instructor_file):
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
                <!-- Webinar 7 Hour CORE SAFE CE #15898 {course_date}, 2024 {st} {tz} -->

                <!-- Course Certificate Info -->
                <!-- 7 Hour {elective_name} {course_number} Certificate

               Is proud to announce that

#name#

with NMLS number #reg_answer# 

has completed the requirements necessary for the

7 Hour Continuing Education SAFE Core
Webinar Course (ID #15898)

completed on October 3rd, 2024.
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
                <p style="text-align: center;"> </p>
                <p style="text-align: center;"><span style="font-size: 14pt;"><strong>7 Hour CORE </strong></span></p>
                <p style="text-align: center;"><span style="font-size: 12pt;"><strong>{st7} - {et7} {tz} Time</strong></span></p>
                <p style="text-align: center;"><span style="font-size: 10pt;">{timezonelist7}</span></p>
                <p style="text-align: center;"><img src="https://mortgageeducators.com/images/webinar/Webcam_Required_Banner.png" alt="" /></p>
                <p style="text-align: center;"><strong><span style="font-size: 10pt;">This course has been approved by the NMLS to fulfill the 7 hours of Continuing Education requirement for general hours outlined in the SAFE Act for mortgage loan originators and brokers. </span>
                <span style="font-size: 10pt;">Per NMLS requirements, all webinar attendees are required to have a webcam enabled for the entire duration of all webinars for NMLS credit.</span></strong></p>
                <p style="text-align: center;">  <strong>NMLS Course #15898<br /></strong><strong>NMLS Provider # 1400062 </strong>  </p>
                """

                output_dir = "C:\\Users\\tbone\\PycharmProjects\\MyNewMainStuff\\work\\lmsDescriptions"
                filename = os.path.join(output_dir, f"{course_date}-lms-{elective}.html")

                with open(filename, 'a', encoding='utf-8') as output_file:
                    output_file.write(html_content)
            except Exception as e:
                print(f"{row['course_date']}-{elective_name}: Problem - {e}")

