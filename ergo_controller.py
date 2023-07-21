# ------------------
# Brought into Pycharm from Jupyter July 2023, looking to play around and improve code quality
#as well as maybe even add some nice basic GUI
#original Jupyter comment below:
# header block: imports and that
# the intent of this notebook is to replicate the work in 'stats creation and storage' as a function driven architecture
# this way I can make it easy to run the plotting for different workouts

FILEPATH = r'C:\Users\johnb\My Drive\Colab Notebooks\Total_log.csv'
# These are the columns from the CSV that I'm interested in
COLUMNS = ['Date','Description','Pace','Work Distance','Stroke Rate/Cadence',
                        'Work Time (Seconds)']
# import libraries
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import functions
from C2GUI import chosen_workout

# read the csv file
df = functions.read_csv(FILEPATH, 0, COLUMNS, ['Date'])
# get rid of all the noise in the logbook csv I import.  anything with a stroke rate < 0 does this
df = df.loc[(df['Stroke Rate/Cadence']>0)]
# convert to date time where necessary
df['Pace']=pd.to_datetime(df['Pace'],errors='coerce')
df['Work Time'] = pd.to_datetime(df['Work Time (Seconds)']*1000000000)
df['Work Time'] = df['Work Time'].dt.strftime('%M:%S.%f')

#sorting out the different categories of workout: timed and distance
#create a dictionary containing the different session names
all_workouts = {
  "30min": "30:00 row",
  "10km": "10000m row",
  "5km": "5000m row",
  "8km": "8000m row"
}
# distance_workouts=('10000m row','5000m row', '8000m row')
# timed_workouts=("30:00 row",)
# all_workouts = timed_workouts+distance_workouts

#print some basic stats to the screen

#Call a function that returns all the basic stats for distance workouts
#initial version I'm going to do each type seperately
#filter the overall df down to those with just single distance workouts
#10km
workout=all_workouts[chosen_workout]
distanceResults=functions.workout_filter(df, workout)
#and get some basic stats for that distance
fastest, median, mean =functions.distance_stats(distanceResults,workout)
#print to screen NEED TO ADAPT TO PRINT TO GUI
functions.printStatsDist(fastest,median, mean, workout)
#get a scatter plot for the chosen workout
#first get the data ready -> convert time from float to time
time_array=functions.prepDataPlt(distanceResults['Work Time (Seconds)'])
#now plot it
functions.scatterPlt(distanceResults['Date'],time_array)
#need to make this a function, but will do fixed time workouts and histograms first
df3=df.loc[df['Description']==workout]
workout_description = df3['Description']
# df2['Work Time (Seconds)']=df2['Work Time (Seconds)'].apply(pd.to_datetime,unit = 's')
work_time = df3['Work Time (Seconds)'].apply(pd.to_datetime,unit = 's')
#print(work_time)
# plot box plots
functions.plot_boxplots(work_time)


#create a scatter plot for 30min workouts
#create the right data array
#df4=df.loc[df['Description'].isin(timed_workouts)]
#now plot it
#functions.scatterPlt(df4['Date'],df4['Work Distance'])
#now get the box plot for fixed time.  Again, should be a function, but for now...
#y=df4['Work Distance']
#f, ax = plt.subplots()
#ax.yaxis.update_units(y)
#sns.boxplot(y=ax.yaxis.convert_units(y))
#get a histogram of timed + distance workouts over all time
#this line creates a df containing only the lines I'm interested in
#df5=df.loc[df['Description'].isin(all_workouts)]
#create new column which extracts the year from the date column
#df5['Year'] = df5['Date'].dt.strftime('%Y')
#print(df4['Year'].value_counts(sort=False, ascending=True))
#playing around now, extract only the workouts for a given year (2021 as orig written)
#df5=df4.loc[df4['Year']=='2021']
#df6= df5.groupby(['Year','Description'])['Description'].count()
