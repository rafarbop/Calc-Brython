from browser import document, bind, alert


display = document["display"]

text_display = []

def atualizar_display(list_text):
    text_concatenado = ""
    for item in list_text:
        text_concatenado += item
    display.value = text_concatenado

@bind(document["1"],"click")
def number_1(ev):
    global text_display
    text_display.append(ev.target.text)
    atualizar_display(text_display)

@bind(document["2"],"click")
def number_1(ev):
    global text_display
    text_display.append(ev.target.text)
    atualizar_display(text_display)

@bind(document["3"],"click")
def number_1(ev):
    global text_display
    text_display.append(ev.target.text)
    atualizar_display(text_display)

@bind(document["4"],"click")
def number_1(ev):
    global text_display
    text_display.append(ev.target.text)
    atualizar_display(text_display)

@bind(document["5"],"click")
def number_1(ev):
    global text_display
    text_display.append(ev.target.text)
    atualizar_display(text_display)

@bind(document["6"],"click")
def number_1(ev):
    global text_display
    text_display.append(ev.target.text)
    atualizar_display(text_display)

@bind(document["7"],"click")
def number_1(ev):
    global text_display
    text_display.append(ev.target.text)
    atualizar_display(text_display)

@bind(document["8"],"click")
def number_1(ev):
    global text_display
    text_display.append(ev.target.text)
    atualizar_display(text_display)

@bind(document["9"],"click")
def number_1(ev):
    global text_display
    text_display.append(ev.target.text)
    atualizar_display(text_display)

@bind(document["0"],"click")
def number_1(ev):
    global text_display
    text_display.append(ev.target.text)
    atualizar_display(text_display)

@bind(document["+"],"click")
def number_1(ev):
    global text_display
    text_display.append(ev.target.text)
    atualizar_display(text_display)

@bind(document["-"],"click")
def number_1(ev):
    global text_display
    text_display.append(ev.target.text)
    atualizar_display(text_display)

@bind(document["*"],"click")
def number_1(ev):
    global text_display
    text_display.append(ev.target.text)
    atualizar_display(text_display)

@bind(document["/"],"click")
def number_1(ev):
    global text_display
    text_display.append(ev.target.text)
    atualizar_display(text_display)

@bind(document["CE"],"click")
def number_1(ev):
    global text_display
    text_display = []
    atualizar_display(text_display)

@bind(document["="],"click")
def number_1(ev):
    global text_display
    if '+' in text_display:
        if text_display.count('+') > 1:
            atualizar_display([])
            alert('Operação inválida!')
            return
        elif text_display.count('+') == 0:
            return
        else:
            n1_list = text_display[:text_display.index('+')]
            n2_list = text_display[text_display.index('+')+1:]
            n1_str = ""
            n2_str = ""
            for item1 in n1_list:
                n1_str += item1
            for item2 in n2_list:
                n2_str += item2
            text_display = [str(int(n1_str)+int(n2_str))]
            atualizar_display(text_display)
            print("Fim do Cálculo")
            return

