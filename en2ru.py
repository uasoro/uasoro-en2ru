import keyboard
import pyperclip
from tkinter.messagebox import showinfo

### en2ru v.1.0

def stop():
    showinfo(title="en2ru v.1.0", message="Программа en2ru была выключена.\nНажмите OK чтобы закрыть окно.")
    exit(0)

def mainen():
    txt = pyperclip.paste()
    x = txt
    ru2en =  {'а':'f', 'б':',', 'в':'d', 'г':'u', 'д':'l', 'е':'t', 'ё':'`', 'ж':';', 'з':'p', 'и':'b', 'й':'q', 
             'к':'r', 'л':'k', 'м':'v', 'н':'y', 'о':'j', 'п':'g', 'р':'h', 'с':'c', 'т':'n', 'у':'e', 'ф':'a',
             'х':'[', 'ц':'w', 'ч':'x', 'ш':'i', 'щ':'o', 'ъ':']', 'ы':'s', 'ь':'m', 'ю':'.', 'я':'z', 'А':'F', 
             'Б':'<', 'В':'D', 'Г':'U', 'Д':'L', 'Е':'T', 'Ё':'~', 'Ж':':', 'З':'P', 'И':'B', 'Й':'Q', 'К':'R', 
             'Л':'K', 'М':'V', 'Н':'Y', 'О':'J', 'П':'G', 'Р':'H', 'С':'C', 'Т':'N', 'У':'E', 'Ф':'A', 'Х':'{',
             'Ц':'W', 'Ч':'X', 'Ш':'I', 'Щ':'O', 'Ъ':'}', 'Ы':'S', 'Ь':'M', 'Э':'"', 'Ю':'>', 'Я':'Z', 'э':"'"}
    for i in x:
        try:
            x = x.replace(i, ru2en.get(i))
        except:
            pass

    pyperclip.copy(x)

def main():
    txt = pyperclip.paste()
    x = txt
    en2ru = {'f':'а', ',':'б', 'd':'в', 'u':'г', 'l':'д', 't':'е', '`':'ё', ';':'ж', 'p':'з', 'b':'и', 'q':'й', 
             'r':'к', 'k':'л', 'v':'м', 'y':'н', 'j':'о', 'g':'п', 'h':'р', 'c':'с', 'n':'т', 'e':'у', 'a':'ф', 
             '[':'х', 'w':'ц', 'x':'ч', 'i':'ш', 'o':'щ', ']':'ъ', 's':'ы', 'm':'ь', "'":'э', '.':'ю', 'z':'я', 
             'F':'А', '<':'Б', 'D':'В', 'U':'Г', 'L':'Д', 'T':'Е', '~':'Ё', ':':'Ж', 'P':'З', 'B':'И', 'Q':'Й', 
             'R':'К', 'K':'Л', 'V':'М', 'Y':'Н', 'J':'О', 'G':'П', 'H':'Р', 'C':'С', 'N':'Т', 'E':'У', 'A':'Ф', 
             '{':'Х', 'W':'Ц', 'X':'Ч', 'I':'Ш', 'O':'Щ', '}':'Ъ', 'S':'Ы', 'M':'Ь', '"':'Э', '>':'Ю', 'Z':'Я'}
    for i in x:
        try:
            x = x.replace(i, en2ru.get(i))
        except:
            pass
        
    if x == txt: mainen()
    else: pyperclip.copy(x)

while True:
    keyboard.add_hotkey('insert', main)
    keyboard.add_hotkey('ctrl+insert', stop)
    keyboard.wait('insert')
    keyboard.wait('ctrl+insert')

### en2ru v.1.0