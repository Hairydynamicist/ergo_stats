# a load of functions that I expect to reuse
import pandas as pd
import datetime as dt
import matplotlib.pyplot as plt
import seaborn as sns
# reading csv files
def read_csv(filepath, header, columns, dates):
    df_loc = pd.read_csv(filepath, header=(header),
               usecols = columns, parse_dates=dates)
    return df_loc


# function to pull distance workout records from the overall dataframe
# not sure I've got this right...as written it can only deal with one element from
# the tuple at a time
def workout_filter(df,workout):
  df.loc[(df['Description'] == workout) & (df['Stroke Rate/Cadence'] > 1), 'name_match'] = workout
  filteredList = df[df.name_match == workout]
  return(filteredList)


#function to calculate fastest, median and average times for single distance workouts
def distance_stats(distanceResults,result):
#fastest
  output = distanceResults['Work Time (Seconds)'].min()
  fastest = distanceResults.loc[distanceResults['Work Time (Seconds)'] == output, 'Work Time'].item().rstrip('0')
#median
  output = distanceResults['Work Time (Seconds)'].median()
  median = distanceResults.loc[distanceResults['Work Time (Seconds)'] == output, 'Work Time'].item().rstrip('0')
#mean
  output = distanceResults['Work Time (Seconds)'].mean()
  mean = dt.timedelta(seconds=output)
  return fastest, median, mean


#function for printing output to screen, at the moment only does 3 inputs
def printStatsDist(fastest,median, mean, workout):
  #print(f"{stat} time for {item} is {output}")
  print(f"fastest time for {workout} is {fastest}")
  print(f"median time for {workout} is {median}")
  print(f"mean time for {workout} is {mean}")
  return


#function for prepping data for plotting
def prepDataPlt(workTime):
  #need to get data into a numpy array for plotting
  workTime = pd.to_datetime(workTime, unit='s')
  # Example 1: Convert specific column use to_numpy()
  time_array = workTime
  return(time_array)


#function for creating scatter plots
def scatterPlt(x,y):
    #the following converts the timedelta into floats so that the regression line can be plotted.
    f, ax = plt.subplots()
    ax.xaxis.update_units(x)
    ax.yaxis.update_units(y)
    #plot the graph
    sns.regplot(x=ax.xaxis.convert_units(x), y=ax.yaxis.convert_units(y))
    plt.show()
    return

#plot boxplots
def plot_boxplots(y):
    f, ax = plt.subplots()
    ax.yaxis.update_units(y)
    sns.boxplot(y=ax.yaxis.convert_units(y))
    plt.show()
    return
