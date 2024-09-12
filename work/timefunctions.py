import datetime
import csv

csv_file = "csv/oh.csv"

# Define time zone offsets as timedelta objects
pt_offset = datetime.timedelta(hours=-1)
mt_offset = datetime.timedelta(hours=0)
ct_offset = datetime.timedelta(hours=1)
et_offset = datetime.timedelta(hours=2)

with open(csv_file, 'r') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        try:
            # Parse the start time, handling potential exceptions
            start_time_str = row['start_time'].strip()  # Remove leading/trailing spaces
            start_time = datetime.datetime.strptime(start_time_str, '%H:%M').time()

            # Convert to datetime with a dummy date
            start_datetime = datetime.datetime.combine(datetime.date.today(), start_time)

            # Calculate time for each time zone using offsets
            pacific_time = (start_datetime + pt_offset).strftime('%I:%M %p')
            mountain_time = (start_datetime + mt_offset).strftime('%I:%M %p')
            central_time = (start_datetime + ct_offset).strftime('%I:%M %p')
            eastern_time = (start_datetime + et_offset).strftime('%I:%M %p')

            everything = f"{pacific_time} {mountain_time} {central_time} {eastern_time}"
            print(f'lol {everything}')
        except ValueError as e:
            print(f"Error parsing start time: {e}")
        except Exception as e:
            print(f"Unexpected error: {e}")