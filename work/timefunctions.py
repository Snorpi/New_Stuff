import datetime


# offsetting because I want to list everything in my csv in mt
def generateCourseTimes(st):
    pt_offset = datetime.timedelta(hours=-1)
    mt_offset = datetime.timedelta(hours=0)
    ct_offset = datetime.timedelta(hours=+1)
    et_offset = datetime.timedelta(hours=+2)
    sevenhr_offset = datetime.timedelta(hours=+1)

    try:
        start_time_str = st.strip()
        st = datetime.datetime.strptime(start_time_str, '%H:%M').time()

        start_datetime = datetime.datetime.combine(datetime.date.today(), st)

        pacific_time = (start_datetime + pt_offset).strftime('%I:%M %p').lstrip('0')
        mountain_time = (start_datetime + mt_offset).strftime('%I:%M %p').lstrip('0')
        central_time = (start_datetime + ct_offset).strftime('%I:%M %p').lstrip('0')
        eastern_time = (start_datetime + et_offset).strftime('%I:%M %p').lstrip('0')
        sevenhr_offset = (start_datetime + sevenhr_offset).strftime('%I:%M %p').lstrip('0')
        sevenpt = (pacific_time + sevenhr_offset).strftime('%I:%M %p').lstrip('0')
        sevenmt = (mountain_time + sevenhr_offset).strftime('%I:%M %p').lstrip('0')
        sevenct = (central_time + sevenhr_offset).strftime('%I:%M %p').lstrip('0')
        sevenet = (eastern_time + sevenhr_offset).strftime('%I:%M %p').lstrip('0')


        elective_timezones = f"""
        <p style="text-align: center;"><span style="font-size: 10pt;">
        ({pacific_time} PT / {mountain_time} MT / {central_time} CT / {eastern_time} ET)
        </span></p>
        """

        sevenhr_timezones = f"""
        <p style="text-align: center;"><span style="font-size:10pt;>
        ({sevenpt} PT / {sevenmt} MT / {sevenct} CT / {sevenet} ET)
        </span></p>
        """

    except ValueError as e:
        print(f"You broke eomething in TIME functions: {e}")

    return elective_timezones and sevenhr_timezones


# Takes 9:00
# Returns (8:00 AM PT / 9:00 AM MT / 10:00 AM CT / 11:00 AM ET)

