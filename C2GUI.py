import PySimpleGUI as psg
import functions
#create a dictionary containing the different session names
all_workouts = {
  "30min": "30:00 row",
  "10km": "10000m row",
  "5km": "5000m row",
  "8km": "8000m row"
}

workouts = ['30min','10km','5km','8km']
lst = psg.Combo(workouts, font=('Arial Bold', 14),  expand_x=True, enable_events=True,  readonly=True, key='-COMBO-')
layout = [[lst,
   psg.Button('View'),
   psg.Button('Exit')],
   [psg.Text("", key='-MSG-',
      font=('Arial Bold', 14),
      justification='center')]
   ]
window = psg.Window('Plot Ergo Stats', layout, size=(715, 200))
while True:
   event, values = window.read()
   if event in (psg.WIN_CLOSED, 'Exit'):
      break
   if event == 'View':
       chosen_workout = values['-COMBO-']
       workout = all_workouts[chosen_workout]
       filteredResults = functions.workout_filter(df, workout)
       #Get and plot some stats
       #slightly different approach for timed and distance workouts
       if chosen_workout != "30min":
          fastest, median, mean = functions.distance_stats(filteredResults, workout)
          # write basic stats to GUI
          msg = f"Fastest time for {workout} is {fastest}\n" \
                f"Median time for {workout} is {median}\n" \
                f"Mean time for {workout} is {mean}"
          window['-MSG-'].update(msg)
          # get a scatter plot for the chosen workout
          # first get the data ready -> convert time from float to time
          time_array = functions.prepDataPlt(filteredResults['Work Time (Seconds)'])
          # now plot it
          functions.scatterPlt(filteredResults['Date'], time_array)
          # need to make this a function, but will do fixed time workouts and histograms first
          df3 = df.loc[df['Description'] == workout]
          workout_description = df3['Description']
          # df2['Work Time (Seconds)']=df2['Work Time (Seconds)'].apply(pd.to_datetime,unit = 's')
          work_time = df3['Work Time (Seconds)'].apply(pd.to_datetime, unit='s')
          # print(work_time)
          # plot box plots
          functions.plot_boxplots(work_time)
       else:
          #timed results scatter plot
          functions.scatterPlt(filteredResults['Date'], filteredResults['Work Distance'])
          #get box plots
          functions.plot_boxplots(filteredResults['Work Distance'])
       break


window.close()