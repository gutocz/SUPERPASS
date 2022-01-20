from tkinter.constants import CENTER
import PySimpleGUI as sg
from PySimpleGUI.PySimpleGUI import TEXT_LOCATION_CENTER
import pyperclip
import os
import pathlib

sg.theme('DarkPurple4')

layout = [[sg.Text('SUPERPASS')],
		[sg.Button('Adicionar nova conta', size=(25, 0))],
		[sg.Button('Verificar conta existente', size=(25, 0))],
		[sg.Button('Apagar conta existente', size=(25, 0))],
		[sg.Button('Sair', size=(25, 0))]
		]

window = sg.Window('SUPERPASS', layout, size= (250, 500), element_justification='c', font='CaviarDreams')

while True:
	event, values = window.read()
	
	if event in (None, 'Sair'):
		break
	
	if event == 'Adicionar nova conta':
		layout = [
			[sg.Text('Plataforma que deseja adicionar a conta:'),
			sg.Input(key='plataforma')],
			[sg.Text('Email/User:'),
			sg.Input(key='user')],
			[sg.Text('Senha:'),
			sg.Input(key='senha')],
			[sg.Button('Confirmar' ,key='confirmar'), sg.Button('Cancelar', key='cancelar')]
		]
		window2 = sg.Window('SUPERPASS', layout)

		while True:
			event, values = window2.read()

			if event in (None, 'cancelar'):
				break

			if event == 'confirmar':
					plataformam = values['plataforma'].upper()
					nomearquivo = plataformam + ".txt"
					arquivo = open(nomearquivo,'w')
					arquivo.write("Plataforma: " + values['plataforma'] + "  ")
					arquivo.write("User ou Email: " + values['user'] + "  ")
					arquivo.write("Senha: " + values['senha'] + "  ")
					arquivo.close()
					[sg.popup('Conta cadastrada com sucesso!')]

					window2.close()
		window2.close()

	if event == 'Apagar conta existente':
		layout = [
			[sg.Text('Plataforma que deseja apagar a conta'),
			sg.Input(key='plataforma')],
			[sg.Button('Confirmar', key='confirmar'), sg.Button('Cancelar', key='cancelar')]
		]
		window4 = sg.Window('SUPERPASS', layout)

		while True:
			event, values = window4.read()

			if event in (None, 'cancelar'):
				break

			if event == 'confirmar':
				plataformam = values['plataforma'].upper()
				arquivo = plataformam + ".txt"
				diretorio = pathlib.Path(os.path.dirname(os.path.realpath(__file__)))
				arquivos = diretorio.glob(arquivo)
				for arquivo in arquivos:
					os.remove(arquivo)
					[sg.popup('Conta deletada com sucesso!')]
				else:
					[sg.popup('Não existe uma conta com esse nome aqui')]

		window4.close()
	
	if event == 'Verificar conta existente':
		layout = [
			[sg.Text('Plataforma que deseja verificar seus dados:'),
			sg.Input(key='plataforma')],
			[sg.Button('Confirmar' ,key='confirmar'), sg.Button('Cancelar', key='cancelar')]
		]
		window3 = sg.Window('SUPERPASS', layout)

		while True:
			event, values = window3.read()

			if event in (None, 'cancelar'):
				break

			if event == 'confirmar':
					plataformam = values['plataforma'].upper()
					nomearquivo = plataformam + ".txt"
					arquivo = open(nomearquivo,'r')
					for linha in arquivo:
						linha = linha.rstrip()
						pyperclip.copy(linha)
						[sg.popup(linha)]
						[sg.popup('Dados copiados para a área de transferência!')]
						#print (linha)
						
					arquivo.close()

					window3.close()
		window3.close()


window.close()