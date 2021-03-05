from tkinter import *
from math import sqrt

def calc_main():
    class Calculadora():
        def __init__(self, master):
            # Instanciando Frames e Botões

            frm_resultado = Frame(master)
            frm_botoes = Frame(master)

            ''' As A seguir todos os botões utilizados no aplicativo serão instanciados e depois exibidos em GRID'''

            self.entry_resultado = Entry(frm_resultado, width=13, bg='#fff', font=('helvetica', 32))

            # Instanciando Botões
            btn_raiz = Button(frm_botoes, text=u'\u221A', bg='#2a2a2a', fg='#fff', width=10, pady=10, command=lambda: self.click('sqrt'))
            btn_exp = Button(frm_botoes, text=u'x\u00B2', bg='#2a2a2a', fg='#fff', width=10, pady=10, command=lambda: self.click('^'))
            btn_C = Button(frm_botoes, text='C', width=10, bg='#2a2a2a', fg='#fff', pady=10, command=self.clear)
            btn_back = Button(frm_botoes, text=u'\u232B', bg='#2a2a2a', fg='#fff', width=10, pady=10, command=self.clear_end)

            btn_div = Button(frm_botoes, text='/', width=10, bg='#2a2a2a', fg='#fff', pady=10, command=lambda: self.click('/'))
            btn_7 = Button(frm_botoes, text='7', bg='#6f6f6f', fg='#fff', width=10, pady=10, command=lambda: self.click('7'))
            btn_8 = Button(frm_botoes, text='8', bg='#6f6f6f', fg='#fff', width=10, pady=10, command=lambda: self.click('8'))
            btn_9 = Button(frm_botoes, text='9', bg='#6f6f6f', fg='#fff', width=10, pady=10, command=lambda: self.click('9'))

            btn_mult = Button(frm_botoes, text='x', bg='#2a2a2a', fg='#fff', width=10, pady=10, command=lambda: self.click('x'))
            btn_4 = Button(frm_botoes, text='4', bg='#6f6f6f', fg='#fff', width=10, pady=10, command=lambda: self.click('4'))
            btn_5 = Button(frm_botoes, text='5', bg='#6f6f6f', fg='#fff', width=10, pady=10, command=lambda: self.click('5'))
            btn_6 = Button(frm_botoes, text='6', bg='#6f6f6f', fg='#fff', width=10, pady=10, command=lambda: self.click('6'))

            btn_sub = Button(frm_botoes, text='-', bg='#2a2a2a', fg='#fff', width=10, pady=10, command=lambda: self.click('-'))
            btn_1 = Button(frm_botoes, text='1', bg='#6f6f6f', fg='#fff', width=10, pady=10, command=lambda: self.click('1'))
            btn_2 = Button(frm_botoes, text='2', bg='#6f6f6f', fg='#fff', width=10, pady=10, command=lambda: self.click('2'))
            btn_3 = Button(frm_botoes, text='3', bg='#6f6f6f', fg='#fff', width=10, pady=10, command=lambda: self.click('3'))

            btn_soma = Button(frm_botoes, text='+', bg='#2a2a2a', fg='#fff', width=10, pady=10, command=lambda: self.click('+'))
            btn_inverte_sinal = Button(frm_botoes, bg='#6f6f6f', fg='#fff', text=u'\u00B1', width=10, pady=10)
            btn_0 = Button(frm_botoes, text='0', bg='#6f6f6f', fg='#fff', width=10, pady=10, command=lambda: self.click('0'))
            btn_ponto = Button(frm_botoes, text=',', bg='#6f6f6f', fg='#fff', width=10, pady=10, command=lambda: self.click('.'))

            btn_iqual = Button(frm_botoes, text='=', bg='#6f6f6f', fg='#fff', width=45, pady=10, command=self.igual)


            # Exibindo widgets de Frames Botões na tela
            frm_resultado.pack()
            frm_botoes.pack()
            self.entry_resultado.pack(padx=10, pady=10)

            btn_raiz.grid(row=0, column=0)
            btn_exp.grid(row=0, column=1)
            btn_C.grid(row=0, column=2)
            btn_back.grid(row=0, column=3)

            btn_7.grid(row=1, column=0)
            btn_8.grid(row=1, column=1)
            btn_9.grid(row=1, column=2)
            btn_div.grid(row=1, column=3)

            btn_4.grid(row=2, column=0)
            btn_5.grid(row=2, column=1)
            btn_6.grid(row=2, column=2)
            btn_mult.grid(row=2, column=3)

            btn_1.grid(row=3, column=0)
            btn_2.grid(row=3, column=1)
            btn_3.grid(row=3, column=2)
            btn_sub.grid(row=3, column=3)

            btn_inverte_sinal.grid(row=4, column=0)
            btn_0.grid(row=4, column=1)
            btn_ponto.grid(row=4, column=2)
            btn_soma.grid(row=4, column=3)

            btn_iqual.grid(row=5, column=0, columnspan=4)


        # Funções do aplicativo
        def click(self, txt):
            """ -> Função click
            Recebe a equação a ser resolvida e imprime no campo resultado.
            param: txt: valor recebido ao pressionar o botão correspondente.
            """
            equacao = self.entry_resultado.get()
            self.entry_resultado.delete(0, END)
            self.entry_resultado.insert(0, equacao + txt)

        def igual(self):
            """ -> Função de resolução da equação
            Esta função verifica qual será a equação a resolver"""
            equacao = self.entry_resultado.get()
            if '+' in equacao:  # Adição
                self.soma(equacao)
            elif '-' in equacao:  # Subtração
                self.subtracao(equacao)
            elif 'x' in equacao:  # Multiplicação
                self.multiplicacao(equacao)
            elif '/' in equacao:  # Divisão
                self.divisao(equacao)
            elif '^' in equacao:  # Exponenciação
                self.exponencial(equacao)

        def soma(self, vlrs):
            vlrs = vlrs.split('+')
            result = float(vlrs[0]) + float(vlrs[1])
            self.entry_resultado.delete(0, END)
            self.entry_resultado.insert(0, str(result))

        def subtracao(self, vlrs):
            vlrs = vlrs.split('-')
            result = float(vlrs[0]) - float(vlrs[1])
            self.entry_resultado.delete(0, END)
            self.entry_resultado.insert(0, str(result))

        def multiplicacao(self, vlrs):
            vlrs = vlrs.split('x')
            result = float(vlrs[0]) * float(vlrs[1])
            self.entry_resultado.delete(0, END)
            self.entry_resultado.insert(0, str(result))

        def divisao(self, vlrs):
            vlrs = vlrs.split('/')
            result = float(vlrs[0]) / float(vlrs[1])
            self.entry_resultado.delete(0, END)
            self.entry_resultado.insert(0, str(result))

        def exponencial(self, vlrs):
            vlrs = vlrs.split('^')
            result = float(vlrs[0]) ** float(vlrs[1])
            self.entry_resultado.delete(0, END)
            self.entry_resultado.insert(0, str(result))

        def clear(self):
            self.entry_resultado.delete(0, END)

        def clear_end(self):
            equacao = self.entry_resultado.get()
            equacao = equacao[:len(equacao)-1]
            self.entry_resultado.delete(0, END)
            self.entry_resultado.insert(0, equacao)


    root = Tk()
    root.title('Calculadora')
    root.iconbitmap('favicon.ico')
    root.resizable(False, False)
    my_gui = Calculadora(root)
    root.mainloop()

calc_main()