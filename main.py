# ------------------
# Brought into Pycharm from Jupyter July 2023
# header block: imports and that
# the intent of this notebook is to replicate the work in 'stats creation and storage' as a function driven architecture
# this way I can make it easy to run the plotting for different workouts
# import libraries
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import functions
# read the csv file
df = functions.read_csv(r'C:\Users\johnb\My Drive\Colab Notebooks\Total_log.csv', 0,
               ['Date','Description','Pace','Work Distance','Stroke Rate/Cadence',
                        'Work Time (Seconds)'], ['Date'])
# get rid of all the noise in the logbook csv I import.  anything with a stroke rate < 0 does this
df = df.loc[(df['Stroke Rate/Cadence']>0)]
# convert to date time where necessary
df['Pace']=pd.to_datetime(df['Pace'],errors='coerce')
df['Work Time'] = pd.to_datetime(df['Work Time (Seconds)']*1000000000)
df['Work Time'] = df['Work Time'].dt.strftime('%M:%S.%f')

#sorting out the different categories of workout: timed and distance
#create a tuple containing the different session names
distance_workouts=('10000m row','5000m row', '8000m row')
timed_workouts=("30:00 row",)
all_workouts = timed_workouts+distance_workouts
#print some basic stats to the screen

#Call a function that returns all the basic stats for distance workouts
#initial version I'm going to do each type seperately
#filter the overall df down to those with just single distance workouts
#10km
workout=distance_workouts[1]
distanceResults=functions.workout_filter(df, workout)
#and get some basic stats for that distance
fastest, median, mean =functions.distance_stats(distanceResults,workout)
#print to screen
functions.printStatsDist(fastest,median, mean, workout)
#get a scatter plot for the chosen workout
#first get the data ready -> get time from float to time
time_array=functions.prepDataPlt(distanceResults['Work Time (Seconds)'])
#now plot it
functions.scatterPlt(distanceResults['Date'],time_array)
#need to make this a function, but will do fixed time workouts and histograms first
df2=df.loc[df['Description'].isin(distance_workouts)]
df2['Work Time (Seconds)']=df2['Work Time (Seconds)'].apply(pd.to_datetime,unit = 's')
x=df2['Description']
y=df2['Work Time (Seconds)']
f, ax = plt.subplots()
ax.yaxis.update_units(y)
sns.boxplot(x=df2['Description'],y=ax.yaxis.convert_units(y))
#create a scatter plot for 30min workouts
#create the right data array
df3=df.loc[df['Description'].isin(timed_workouts)]
#now plot it
functions.scatterPlt(df3['Date'],df3['Work Distance'])
#now get the box plot for fixed time.  Again, should be a function, but for now...
y=df3['Work Distance']
f, ax = plt.subplots()
ax.yaxis.update_units(y)
sns.boxplot(y=ax.yaxis.convert_units(y))
#get a histogram of timed + distance workouts over all time
#this line creates a df containing only the lines I'm interested in
df4=df.loc[df['Description'].isin(all_workouts)]
#create new column which extracts the year from the date column
df4['Year'] = df4['Date'].dt.strftime('%Y')
#print(df4['Year'].value_counts(sort=False, ascending=True))
#playing around now, extract only the workouts for a given year (2021 as orig written)
#df5=df4.loc[df4['Year']=='2021']
df5= df4.groupby(['Year','Description'])['Description'].count()
