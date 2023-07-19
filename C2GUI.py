import PySimpleGUI as psg
workouts = ['30min','10km','5km','8km']
lst = psg.Combo(workouts, font=('Arial Bold', 14),  expand_x=True, enable_events=True,  readonly=True, key='-COMBO-')
layout = [[lst,
   psg.Button('View'),
   psg.Button('Exit')],
   [psg.Text("", key='-MSG-',
      font=('Arial Bold', 14),
      justification='center')]
   ]
window = psg.Window('Combobox Example', layout, size=(715, 200))
while True:
   event, values = window.read()
   print(event, values)
   if event in (psg.WIN_CLOSED, 'Exit'):
      break
   if event == 'View':
       chosen_workout = values['-COMBO-']
       print(chosen_workout)
#code to execute controller
#will need to modify controller such that it only deals with selected workout


window.close()