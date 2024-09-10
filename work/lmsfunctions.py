
# generates lms course certificate information
def generateCertificateinfo(elective_duration, elective_name, course_number, course_date):
    cert_html = f"""<!-- Course Certificate Info -->
        <!-- {elective_duration} Hour {elective_name} {course_number} Certificate

        Is proud to announce that

        #name#

        with NMLS number #reg_answer# 

        has completed the requirements necessary for the

        {elective_duration} Hour {elective_name}
        Webinar Course (ID {course_number})

        completed on {course_date}, 2024. 
        -->"""
    return cert_html

# generates lms description and whatnot
def generate_lms_description(course_title, elective_duration, elective_name, course_number, cd,
                             instructor_fullname, instructor_image, instructor, pageanchor, st, et, tz, timezonelist):
    try:
        lms_content = f"""
        <!-- Course Title -->
        <!-- {course_title} -->
        """

        lms_content += generateCertificateinfo(elective_duration, elective_name, course_number, cd)

        lms_content += f"""<!-- Top Information -->
        <table width="80%" align="center">
        <tbody>
        <tr>
        <td>
        <h1 style="font-weight: 600; text-align: center;">2024 Live WEBINAR<br /> NMLS {elective_duration} Hour {elective_name} Continuing Education Course</h1>
        <h1 style="font-weight: 600; text-align: center;">{cd}, 2024</h1>
        </td>
        </tr>
        </tbody>
        </table>

        <!-- Bottom Information -->
        <p><img style="display: block; margin-left: auto; margin-right: auto;" src="https://mortgageeducators.com{instructor_image}" alt="" /></p>
        <p style="text-align: center;">
        <span style="font-size: 24pt;"><strong>
        <a title="Click to learn more about {instructor}!" href="https://mortgageeducators.com/instructors{pageanchor}" target="_blank" rel="noopener noreferrer">{instructor_fullname}</a></strong></span></p>
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
    except Exception as e:
        print(f"lmsa-{cd}-{elective_name}: Problem - {e}")
    return lms_content
