import PySimpleGUI as sg

def janela_inicial():
    sg.theme('BrownBlue')
    linha = [
        [sg.Checkbox(''), sg.Input('')]
    ]
    layout = [
        [sg.Frame('Tarefas', layout=linha, key='container')],
        [sg.Button('Nova Tarefa'), sg.Button('Resetar')]
    ]

    return sg.Window('Lista de Tarefas', layout=layout, finalize=True)

janela = janela_inicial()

while True:
    event, values = janela.read()
    if event == sg.WIN_CLOSED:
        break
    elif event == 'Nova Tarefa':
        janela.extend_layout(janela['container'],  [[sg.Checkbox(''), sg.Input('')]])
    elif event == 'Resetar':
        janela.close()
        janela = janela_inicial()