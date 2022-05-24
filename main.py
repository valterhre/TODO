import PySimpleGUI as sg
import sqlite3
valuis = []
command = ['del', 'Edit']
layout =[[sg.Listbox(key='list', size=(50,20), values=valuis, select_mode='extend',right_click_menu=['&Right', command])],
         [sg.Input(key='input'),sg.Button(key='push')],
         [sg.Button('del'),sg.Button(key='update', button_text='update')]]
window = sg.Window('To Do',layout)
con = sqlite3.connect('todo.db')
cur = con.cursor()
try:
    cur.execute('''CREATE TABLE todo (todo text)        
    ''')
except:
    print('already exist')
while True:
    event, values=window.read()
    def df():
        for row in cur.execute('SELECT * FROM todo'):
            valuis.append(row[0])
        window['list'].update(valuis)
    if not bool(valuis):
        df()
    if event=='push':
        valuis.append(values['input'])
        window['list'].update(valuis)
        window['input'].update('')
        cur.execute("INSERT INTO todo VALUES ('{}')".format(values['input']))
    if event =='del':#remove from list
        valuis.remove(values['list'][0])
        window['list'].update(valuis)
        cur.execute(f"DELETE FROM todo WHERE todo ='{values['list'][0]}'")
    if event =='Edit':
        window['input'].update(values['list'][0])
        valuis.remove(values['list'][0])
        window['input'].update(values['list'][0])
        if event == 'push':
            window['list'].update(valuis)
            window['input'].update('')
    if event =='update':
        window['list'].update(valuis)
    con.commit()
con.close()
window.close()