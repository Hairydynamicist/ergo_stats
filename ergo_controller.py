# ------------------
# Brought into Pycharm from Jupyter July 2023, looking to play around and improve code quality
#as well as maybe even add some nice basic GUI
#original Jupyter comment below:
# header block: imports and that
# the intent of this notebook is to replicate the work in 'stats creation and storage' as a function driven architecture
# this way I can make it easy to run the plotting for different workouts

FILEPATH = r'C:\Users\johnb\Downloads\concept2-season-2014.csv'

# These are the columns from the CSV that I'm interested in
COLUMNS = ['Date','Description','Pace','Work Distance','Stroke Rate/Cadence',
                        'Work Time (Seconds)']
# import libraries
import pandas as pd
import functions

# read the csv file downloaded from C2 website
df = functions.read_csv(FILEPATH, 0, COLUMNS, ['Date'])
# get rid of all the noise in the logbook csv I import.  anything with a stroke rate < 0 does this
df = df.loc[(df['Stroke Rate/Cadence']>0)]
# convert to date time where necessary
df['Pace']=pd.to_datetime(df['Pace'],errors='coerce')
df['Work Time'] = pd.to_datetime(df['Work Time (Seconds)']*1000000000)
df['Work Time'] = df['Work Time'].dt.strftime('%M:%S.%f')

#check to see if there's a local CSV file that needs updating:


# Open the GUI
with open("C2GUI.py") as f:
    exec(f.read())

