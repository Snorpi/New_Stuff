import timefunctions as tf


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


def generateFinalText(elective_duration, course_number, elective_name):
    core_html = f"""
        <p> </p>
        <p style="text-align: center;"><img src="https://mortgageeducators.com/images/webinar/Webcam_Required_Banner.png" alt="" /></p>
        <p style="text-align: center;"><strong><span style="font-size: 10pt;">This course has been approved by the NMLS to fulfill the {elective_duration} hour of Continuing Education requirement for {elective_name} outlined in the SAFE Act for mortgage loan originators and brokers. </span>
        <span style="font-size: 10pt;">Per NMLS requirements, all webinar attendees are required to have a webcam enabled for the entire duration of all webinars for NMLS credit.</span></strong></p>
        <p style="text-align: center;">  <strong>NMLS Course {course_number}<br /></strong><strong>NMLS Provider # 1400062 </strong>  </p>
    """
    return core_html

# def generateInstructorInfo(instructor_image, instructor, pageanchor, instructor_fullname, errorinfo):
#    instructor_html = f""""""
#    try:
#        instructor_html += f"""
#        <p><img style="display: block; margin-left: auto; margin-right: auto;" src="https://mortgageeducators.com{instructor_image}" alt="" /></p>
#        <p style="text-align: center;">
#        <span style="font-size: 24pt;"><strong>
#        <a title="Click to learn more about {instructor}!" href="https://mortgageeducators.com/instructors{pageanchor}" target="_blank" rel="noopener noreferrer">{instructor_fullname}</a></strong></span></p>
#        <p> </p>"""
#    except Exception as e:
#        print(f"You broke the instructor HTML for the LMS LOL - {errorinfo} -- {e}")
#    return instructor_html


def generateTopInfo(elective_duration, elective_name, cd, fullstate, errorinfo):
    try:
        toptable = f""""""

        if fullstate == 'n':

            toptable += f"""
            <!-- Top Information -->
            <table width="80%" align="center">
            <tbody>
            <tr>
            <td>
            <h1 style="font-weight: 600; text-align: center;">2026 Live WEBINAR<br /> NMLS {elective_duration} Hour {elective_name} Continuing Education Course</h1>
            <h1 style="font-weight: 600; text-align: center;">{cd}, 2026</h1>
            </td>
            </tr>
            </tbody>
            </table>
            """

        if fullstate == 'y':
            toptable += f""" 
            <!-- Top Information -->
            <table width="80%" align="center">
            <tbody>
            <tr>
            <td>
            <h1 style="font-weight: 600; text-align: center;">2026 Live WEBINAR<br /> NMLS {elective_duration} Hour {elective_name} Continuing Education Course</h1>
            <h1 style="font-weight: 600; text-align: center;">{cd}, 2026</h1>
            </td>
            </tr>
            </tbody>
            </table>
            """
        return toptable
    except Exception as e:
        print(f"Somewhere in the LMS top table seems to have broken. -- {e}")

def generateBotInfo(elective_duration, elective_name, cd, fullstate, errorinfo, stet, timezonelist):
    try:
        bottomtable = f""""""

        if fullstate == 'n':

            bottomtable += f"""
            <p style="text-align: center;"><span style="font-size: 14pt;"><strong>{elective_duration} Hour {elective_name} Elective</strong></span></p>
            <p style="text-align: center;"><span style="font-size: 12pt;"><strong>{stet} Time</strong></span></p>
            <p style="text-align: center;"><span style="font-size: 10pt;">{timezonelist}</span></p>
            <p style="text-align: center;"> </p>
            """

        if fullstate == 'y':
            bottomtable += f""" 
            <p style="text-align: center;"><span style="font-size: 14pt;"><strong>{elective_duration} Hour {elective_name} Elective</strong></span></p>
            <p style="text-align: center;"><span style="font-size: 12pt;"><strong>{stet} Time</strong></span></p>
            <p style="text-align: center;"><span style="font-size: 10pt;">{timezonelist}</span></p>
            <p style="text-align: center;"> </p>
            <p style="text-align: center;"><span style="font-size: 14pt;"><strong>7 Hour CORE </strong></span></p>
            <p style="text-align: center;"><span style="font-size: 12pt;"><strong></strong></span></p>
            <p style="text-align: center;"><span style="font-size: 10pt;"></span></p>
            <p style="text-align: center;"> </p>
            """
        return bottomtable
    except Exception as e:
        print(f"Somewhere in the LMS bottom table seems to have broken. -- {errorinfo} {e}")

# generates lms description and whatnot
def generate_lms_description(course_title, elective_duration, elective_name, course_number, cd, 
                             stet, timezonelist, errorinfo, fullstate, st):
    try:
        lms_content = f"""
        <!-- Course Title -->
        <!-- {course_title} -->
        """

        lms_content += generateCertificateinfo(elective_duration, elective_name, course_number, cd)

        lms_content += generateTopInfo(elective_duration, cd, elective_name, fullstate, errorinfo)

        # lms_content += generateInstructorInfo(instructor_image, instructor, instructor_fullname, pageanchor)

        # lms_content +=

        lms_content += tf.generateCourseTimes(st)

        lms_content += generateFinalText(elective_duration, elective_name, course_number
                                         )
    except Exception as e:
        print(f"You broke the LMS HTML ------ {e}")
    return lms_content
