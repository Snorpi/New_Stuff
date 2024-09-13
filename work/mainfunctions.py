import csv
import functions as fc
import lmsfunctions as lms


# for standalone products
def generate_standalone_product(elective, elective_info, elective_duration,
                                elective_name, instructor, instructor_info, instructor_banner, stet, timezonelist,
                                course_number, course_url, cd, banking_fee, pageanchor, productsku, pagetitle,
                                errorinfo):
    try:
        standalone_content = f"""
        <p><a title="Click to learn more about {instructor}!" href="https://mortgageeducators.com/instructors" target="_blank" rel="noopener noreferrer"><img style="display: block; margin-left: auto; margin-right: auto;" src="https://mortgageeducators.com{instructor_banner}" alt="" /></a></p>
        <p> </p>
        <p style="text-align: center;"><span style="font-size: 18pt;"><strong>Date: </strong>{cd}, 2024</span></p>
        <p style="text-align: center;"><span style="font-size: 18pt;"><strong>Start Time: </strong>{stet} Time</span></p>
        <p style="text-align: center;"><span style="font-size: 18pt;">{timezonelist}</span></p>
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

        standalone_content += fc.generate_chapter_html(elective_info.get('chapters', []))

        standalone_content += f"""
        <p><span style="font-size: 12pt;"><strong>***This live webinar course includes only the {elective_duration} hour(s) of {elective_name} CE material. If you need additional state education, those can be found <a href="https://mortgageeducators.com/articles?id=751" target="_blank" rel="noopener noreferrer">HERE</a> in an online format***</strong></span></p>
        <p style="text-align: left;"><span style="font-size: 12pt;">Includes the ${banking_fee}0 NMLS banking fee. </span></p>
        <p style="text-align: left;"><span style="font-size: 12pt;">This course is in a live webinar format and requires the student to be active and pay attention the entire time. Control measures will be taken to ensure   
         participation. </span></p>
        <p style="text-align: left;"><span style="font-size: 12pt;">Questions: <a href="mailto:webinar@MortgageEducators.com">webinars@MortgageEducators.com</a></span></p>
        <p style="text-align: left;"><span style="font-size: 12pt;">NMLS Provider #1400062</span></p> 
        
        """
        return standalone_content
    except Exception as e:
        print(f"Problem generating a standalone product? {errorinfo} {e}")


# for 7+1 Products
def generate_7_1_html(elective, elective_info, elective_duration,
                      elective_name, instructor, instructor_info, instructor_banner, stet, timezonelist,
                      course_number, course_url, cd, banking_fee, pageanchor, productsku, pagetitle, errorinfo):
    try:
        fbankingfee = banking_fee + 10.50
        html_content = f"""
        <p><a title="Click to learn more about {instructor}!" href="https://mortgageeducators.com/instructors{pageanchor}" target="_blank" rel="noopener noreferrer"><img style="display: block; margin-left: auto; margin-right: auto;" src="https://mortgageeducators.com{instructor_banner}" alt="{instructor} Banner" /></a></p>
        <p> </p>
        <p style="text-align: center;"><span style="font-size: 18pt;"><strong>Date: </strong>{cd}, 2024</span></p>
        <p style="text-align: center;"><span style="font-size: 18pt;"><strong>Start Time: </strong>{stet} Time</span></p>
        <p style="text-align: center;"><span style="font-size: 18pt;">{timezonelist}</span></p>
        <p> </p>
        <p style="text-align: center;"><span style="text-decoration: underline; font-size: 24pt;"><strong>UWM - 2024 7 + {elective_duration} Hour {elective_name} CE Webinar</strong></span></p>
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
        <p><span style="font-size: 12pt;"><strong>***This live webinar course includes only the 7 + {elective_duration} hours of {elective_name} CE material. If you need additional state education, those can be found <a href="https://mortgageeducators.com/articles?id=751" target="_blank" rel="noopener noreferrer">HERE</a> in an online format***</strong></span></p>
        <p style="text-align: left;"><span style="font-size: 12pt;">Includes the ${fbankingfee}0 NMLS banking fee. </span></p>
        <p style="text-align: left;"><span style="font-size: 12pt;">This course is in a live webinar format and requires the student to be active and pay attention the entire time. Control measures will be taken to ensure   
         participation. </span></p>
        <p style="text-align: left;"><span style="font-size: 12pt;">Questions: <a href="mailto:webinar@MortgageEducators.com">webinars@MortgageEducators.com</a></span></p>
        <p style="text-align: left;"><span style="font-size: 12pt;">NMLS Provider #1400062</span></p> 
        """

        return html_content
    except Exception as e:
        print(f"You fked a 7+1 product up --  {errorinfo} {e}")


# this would be the main function i guess.
def productCreator(csv_file):
    elective_data = fc.load_elective_data(elective_file)
    instructor_data = fc.load_instructor_data(instructor_file)

    with (open(csv_file, 'r') as csvfile):
        reader = csv.DictReader(csvfile)
        for row in reader:
            # elective information
            elective = row['elective']
            elective_info = elective_data.get(elective, {})
            elective_duration = elective_info.get('elective_duration', 0)
            elective_name = elective_info.get('elective_name')

            # instructor data
            instructor = row['instructor']
            instructor_info = instructor_data.get(instructor, {})
            instructor_banner = instructor_info.get('bannerlink')
            instructor_fullname = f"{instructor_info.get('fname')} {instructor_info.get('lname')}"
            pageanchor = instructor_info.get('pageanchor')

            # course time information
            month = row['month']
            day = row['day']
            tz = row['timezone']
            st = row['start_time']
            et = row['end_time']
            stet = f"{st} - {et} {tz}"
            timezonelist = f"({row['PT']} PT / {row['MT']} MT / {row['CT']} CT / {row['ET']} ET)"


            # actual course info
            course_number = elective_info.get('course_number')
            course_url = f"{month}-{day}-24-{elective_duration}-{elective}-ceq"
            cd = row['course_date']
            banking_fee = int(elective_info.get('elective_duration')) * 1.50

            # "standalone backend type stuff"
            productsku = f"{month}.{day}.24 - {elective_duration} {elective} CEQ"
            pagetitle = f"{month}/{day} - {elective_duration} Hour {elective} CE Webinar"

            # "standalone backend type stuff"
            fproductsku = f"{month}.{day}.24 - 7 + {elective_duration} {elective} CEQ"
            fpagetitle = f"{month}/{day} - 7 + {elective_duration} Hour {elective} CE Webinar"

            # 'fullstate' is tbe column I'm using to determine if the product is a 7+1 or a standalone
            fullstate = row['full']
            lmsstate = row['lmsstate']
            errorinfo = f"{cd} {elective_name} -- "

            # LMS assignments
            course_title = f"Webinar {elective_duration} Hour {elective_name} Elective CE {course_number} {cd}, 2024 {st} {tz}"
            instructor_image = instructor_info.get('lmslink')

            try:

                if fullstate == 'y':
                    html_content = f""" """
                    html_content += fc.generateProductinfo_full(fullstate, elective, elective_duration, elective_name,
                                                                cd, st, tz, productsku, pagetitle, course_url,
                                                                errorinfo, fproductsku, fpagetitle)
                    html_content += generate_7_1_html(elective, elective_info, elective_duration,
                                                      elective_name, instructor, instructor_info, instructor_banner,
                                                      stet, timezonelist, course_number, course_url, cd, banking_fee,
                                                      pageanchor, productsku, pagetitle, errorinfo)

                    fc.outputProductDir(elective, fullstate, month, day, html_content)

                elif fullstate == 'n':
                    standalone_content = f""" """
                    standalone_content += fc.generateProductinfo_full(fullstate, elective, elective_duration,
                                                                      elective_name, cd, st, tz, productsku, pagetitle,
                                                                      course_url, errorinfo, fproductsku, fpagetitle)

                    standalone_content += generate_standalone_product(elective, elective_info, elective_duration,
                                                                      elective_name, instructor, instructor_info,
                                                                      instructor_banner, stet, timezonelist,
                                                                      course_number, course_url, cd, banking_fee,
                                                                      pageanchor,
                                                                      productsku, pagetitle, errorinfo)


                    fc.outputProductDir(elective, fullstate, month, day, standalone_content)
            finally:
                try:

                    if lmsstate == 'y':
                        # create the LMS course content
                        lms_content = f""" """
                        lms_content += lms.generate_lms_description(course_title, elective_duration, elective_name,
                                                                    course_number, cd,
                                                                    instructor_fullname, instructor_image, instructor,
                                                                    pageanchor, stet,
                                                                    timezonelist, st, errorinfo)

                        fc.outputLmsDir(cd, elective, lms_content)
                    elif lmsstate == 'n':
                        print("I think I need something to print here in order to keep the loop going. I'm not sure.")
                except Exception as e:
                    print(f"You broke the LMS part of productGenerator. Nice! -- {errorinfo} {e}")


# these should be changed, definitely csv_file. you know, why make test products just make real ones and fix them if they're wrong lol
csv_file = "csv/ohman.csv"
elective_file = "json/elective_data.json"
instructor_file = "json/instructors.json"

# this is calling the main to actually run
productCreator(csv_file)

# ################################################## old and unused these days because I'm a cool guy now
# Example Usage

# For LMS Title, Certificate Title, Certificate Info, Course Information Pages
# generate_lms_description(csv_file, elective_file, instructor_file)

# For Generating state elective product descriptions, title, alias, sku, page title, link
# generate_standalone_product(csv_file, elective_file, instructor_file)

# For generating 7+1 product descriptions, title, alias, sku, page title, link
# generate_7_1_html(csv_file, elective_file, instructor_file)
