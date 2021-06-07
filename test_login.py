from PySimpleGUI import PySimpleGUI as sg
# Criar as janelas e estilos(layout)

def janela_login():
	sg.theme('Reddit')
	layout = [
		[sg.Text('Nome')],
		[sg.Input()],
		[sg.Button('Continuar')]
	]
	return sg.Window('Login', Layout=layout, finalize=True)


def janela_pedido():
	sg.theme('Reddit')
	layout = [
		[sg.Text('Fazer Pedido')],
		[sg.Checkbox('Pizza Pepperoni', key='pizza1'), sg.Checkbox('Pizza Frango c/ Catupiry', key='pizza2')]
	]
	return sg.Window('Montar Pedido', Layout=layout, finalize=True)

# Criar as janelas iniciais
janela1, janela2 = janela_login(), None


# Criar um loop de leitura de eventos
while True:
	window, event, values = sg.read_all_windows()
	# Quando a janela for fechada
	if window == janela1 and event == sg.WIN_CLOSED:
		break
	# Quando queremos ir para próxima janela
	if window == janela1 and event == 'Continuar':
		janela2 = janela_pedido()
		janela1.hide()

# Lógica de o que deve acontecer ao clicar os botões

