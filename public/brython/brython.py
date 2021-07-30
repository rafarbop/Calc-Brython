from browser import document, html, bind, alert


display = document["display"]
history = document["display_history"]

text_display = []
display_history = []
result_in_display = False


def atualizar_display(list_text):
    global result_in_display
    text_concatenado = ""
    for item in list_text:
        text_concatenado += item
    display.value = text_concatenado
    print(result_in_display)


def refresh_history(list_history):
    history.text = ""
    while len(list_history) > 5:
        list_history.pop(0)
    for group_item in list_history:
        history_in_text = "".join(group_item)
        history <= html.P(f"{history_in_text}", Class="box")


@bind(document["1"], "click")
@bind(document["2"], "click")
@bind(document["3"], "click")
@bind(document["4"], "click")
@bind(document["5"], "click")
@bind(document["6"], "click")
@bind(document["7"], "click")
@bind(document["8"], "click")
@bind(document["9"], "click")
@bind(document["0"], "click")
@bind(document["+"], "click")
@bind(document["-"], "click")
@bind(document["*"], "click")
@bind(document["/"], "click")
def get_inputs(ev):
    global result_in_display
    global text_display
    if (not result_in_display):
        text_display.append(ev.target.text)
        atualizar_display(text_display)
    elif ev.target.text in [
        '+',
        '-',
        '*',
        '/',
    ]:
        result_in_display = False
        text_display.append(ev.target.text)
        atualizar_display(text_display)
    else:
        text_display = []
        result_in_display = False
        text_display.append(ev.target.text)
        atualizar_display(text_display)



@bind(document["CE"], "click")
def clean_display(ev):
    global text_display
    global display_history
    text_display = []
    atualizar_display(text_display)


@bind(document["="], "click")
def operation_sum(ev):
    global text_display
    global display_history
    global result_in_display
    isValid = True
    operetion_text = ''.join(text_display)
    operators = []
    operators.append(operetion_text.count('+'))
    operators.append(operetion_text.count('-'))
    operators.append(operetion_text.count('*'))
    operators.append(operetion_text.count('/'))
    if sum(operators) > 1:
        text_display = []
        atualizar_display(text_display)
        alert('Operação inválida!')
        return
    if '+' in text_display:
        n1_list = text_display[:text_display.index('+')]
        n2_list = text_display[text_display.index('+')+1:]
        n1_str = ""
        n2_str = ""
        for item1 in n1_list:
            n1_str += item1
        for item2 in n2_list:
            n2_str += item2
        display_history.append(text_display)
        refresh_history(display_history)
        text_display = [str(float(n1_str)+float(n2_str))]
        result_in_display = True
        atualizar_display(text_display)
        print("Cálculo Realizado+")
        return
    if '-' in text_display:
        n1_list = text_display[:text_display.index('-')]
        n2_list = text_display[text_display.index('-')+1:]
        n1_str = ""
        n2_str = ""
        for item1 in n1_list:
            n1_str += item1
        for item2 in n2_list:
            n2_str += item2
        display_history.append(text_display)
        refresh_history(display_history)
        text_display = [str(float(n1_str)-float(n2_str))]
        result_in_display = True
        atualizar_display(text_display)
        print("Cálculo Realizado-")
        return
    if '*' in text_display:
        n1_list = text_display[:text_display.index('*')]
        n2_list = text_display[text_display.index('*')+1:]
        n1_str = ""
        n2_str = ""
        for item1 in n1_list:
            n1_str += item1
        for item2 in n2_list:
            n2_str += item2
        display_history.append(text_display)
        refresh_history(display_history)
        text_display = [str(float(n1_str)*float(n2_str))]
        result_in_display = True
        atualizar_display(text_display)
        print("Cálculo Realizado*")
        return
    if '/' in text_display:
        n1_list = text_display[:text_display.index('/')]
        n2_list = text_display[text_display.index('/')+1:]
        n1_str = ""
        n2_str = ""
        for item1 in n1_list:
            n1_str += item1
        for item2 in n2_list:
            n2_str += item2
        display_history.append(text_display)
        refresh_history(display_history)
        text_display = [str(float(n1_str)/float(n2_str))]
        result_in_display = True
        atualizar_display(text_display)
        print("Cálculo Realizado/")
        return
