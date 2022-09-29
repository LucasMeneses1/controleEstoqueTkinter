#!/usr/bin/env python
# coding: utf-8

# In[ ]:


from tkinter import *
from tkinter import ttk
import tkinter.messagebox
import pyodbc
import datetime

# Integração com o Banco de Dados
dados_conexao = ("Driver={SQL Server};"
                 "Server=ADMIN-PC;"
                 "Database=ProjetoCrud")
conexao = pyodbc.connect(dados_conexao)
cursor = conexao.cursor()

# Classe da janela
class app:
    def __init__(self, usuario):
        ############################ CONFIGURAÇÔES JANELA PRINCIPAL APP #############################
        
        self.usuario = usuario
        self.janela = Tk()
        self.janela.geometry("600x823")
        self.janela.configure(bg='#03989e')
        self.janela.title('Controle de Estoque')
        self.background_img = PhotoImage(file=r"background.png")
        self.canvas = Canvas(
            self.janela,
            bg="#ffffff",
            height=823,
            width=600,
            bd=0,
            highlightthickness=0,
            relief="ridge")
        self.canvas.place(x=0, y=0)
        self.background = self.canvas.create_image(
            300.0, 169.0,
            image=self.background_img)
        self.create()
        self.read()
        self.update()
        self.delete()
        self.editar()
        self.treeview_main()
        
        self.janela.resizable(False, False)
        self.janela.mainloop()
    
        ################################ WIDGETS DO MENU PRINCIPAL ##################################

    # 1- Btn Criar novo item
    def create(self):
        self.img0 = PhotoImage(file=f"img0.png")
        self.b0 = Button(
            image=self.img0,
            borderwidth=0,
            highlightthickness=0,
            command=self.btn_criar_novo_item,
            relief="flat")

        self.b0.place(
            x=34, y=228,
            width=255,
            height=34)
        
    # 2- Btn Procurar Item
    def read(self):
        self.img1 = PhotoImage(file=f"img1.png")
        self.b1 = Button(
            image=self.img1,
            borderwidth=0,
            highlightthickness=0,
            command=self.btn_procurar_item,
            relief="flat")

        self.b1.place(
            x=308, y=228,
            width=255,
            height=34)
        
    # 3- Btn Editar quantidade do item
    def update(self):
        self.img3 = PhotoImage(file=f"img3.png")
        self.b3 = Button(
            image=self.img3,
            borderwidth=0,
            highlightthickness=0,
            command=self.btn_editar_qtd,
            relief="flat")

        self.b3.place(
            x=34, y=271,
            width=255,
            height=34)
        
    # 4- Btn Excluir item
    def delete(self):
        self.img2 = PhotoImage(file=f"img2.png")
        self.b2 = Button(
            image=self.img2,
            borderwidth=0,
            highlightthickness=0,
            command=self.btn_deletar_item,
            relief="flat")

        self.b2.place(
            x=308, y=271,
            width=255,
            height=34)
    
    # 5- Botão de edição
    def editar(self):
        self.be = Button(
            text='Editar item',
            font="Inter 10 bold",
            bg = '#000000',
            fg = 'white',
            borderwidth=0,
            highlightthickness=0,
            command=self.btn_editar_item,
        )
        
        self.be.place(
            x=262, y=794,
            width=75,
            height=27
        )

    # 6- TreeView Principal
    def treeview_main(self):
        self.tv = ttk.Treeview(columns=('id','cod','nome','lote','qtd'), show='headings')
        
        scrlbar = ttk.Scrollbar(self.janela,  
                           orient ="vertical",  
                           command = self.tv.yview)
        scrlbar.place(
            x = 573, y = 644,
            height = 147
            )
        self.tv.configure(yscrollcommand = scrlbar.set)

        self.tv.column('id', minwidth=116 , width=116, anchor = N)
        self.tv.column('cod', minwidth=116 , width=116, anchor = N)
        self.tv.column('nome', minwidth=116 , width=116, anchor = N)
        self.tv.column('lote', minwidth=116 , width=116, anchor = N)
        self.tv.column('qtd', minwidth=116 , width=116, anchor = N)

        self.tv.heading('id', text='ID_ITEM')
        self.tv.heading('cod', text='CÓDIGO_ITEM')
        self.tv.heading('nome', text='NOME_ITEM')
        self.tv.heading('lote', text='LOTE_ITEM')
        self.tv.heading('qtd', text='QUANTIDADE_ITEM')

        comando = f"""SELECT * FROM Itens
                    """
        cursor.execute(comando)

        for item in cursor.fetchall():
            i,j,k,l,m = item
            self.tv.insert('', 'end', values=(i,j,k,l,m))

        self.tv.place(
            x=10, y=620,
            width=580,
            height=170)
        
    ################################ treeview secundária ###################################
        
    # Exibe o resultado da pesquisa
    def treeview_sec(self):
        self.tv2 = ttk.Treeview(columns=('id','cod','nome','lote','qtd'),show='headings')
        
        self.scrlbar = ttk.Scrollbar(self.janela,  
                           orient ="vertical",  
                           command = self.tv2.yview)
        self.scrlbar.place(
            x = 573, y = 444,
            height = 116
            )
        self.tv2.configure(yscrollcommand = self.scrlbar.set)
        
        self.tv2.column('id', minwidth=116 , width=116, anchor = N)
        self.tv2.column('cod', minwidth=116 , width=116, anchor = N)
        self.tv2.column('nome', minwidth=116 , width=116, anchor = N)
        self.tv2.column('lote', minwidth=116 , width=116, anchor = N)
        self.tv2.column('qtd', minwidth=116 , width=116, anchor = N)

        self.tv2.heading('id', text='ID_ITEM')
        self.tv2.heading('cod', text='CÓDIGO_ITEM')
        self.tv2.heading('nome', text='NOME_ITEM')
        self.tv2.heading('lote', text='LOTE_ITEM')
        self.tv2.heading('qtd', text='QUANTIDADE_ITEM')

        for item in self.itens_procurados:
            #print(self.itens_procurados)
            i,j,k,l,m = item
            self.tv2.insert('', 'end', values=(i,j,k,l,m))

        self.tv2.place(
            x=10, y=420,
            width=580,
            height=140)
        
    ################################### INPUTS DO USUÁRIO #########################################

    # 1- Caixa de entrada do código do item    
    def cod(self, i = 0):
        if i == 0:
            self.ci = Label(
                text='CÓDIGO:',
                font="Inter 10 bold",
                bg='#ffffff'
            )

            self.entry0 = Entry(
                bd=0,
                bg="#ffffff",
                highlightthickness=1)

            self.ci.place(
                x=24, y=383,
                width=150,
                height=20)

            self.entry0.place(
                x=185, y=378,
                width=388,
                height=28)
        else:
            try:
                self.ci.destroy()
                self.entry0.destroy()
            except:
                pass

    # 2- Caixa de entrada do nome do item
    def nome(self, i = 0):
        if i == 0:
            self.ni = Label(
                text='NOME:',
                font="Inter 10 bold",
                bg='#ffffff'
            )

            self.ni.place(
                x=24, y=433,
                width=155,
                height=20
                )

            self.entry1 = Entry(
                bd=0,
                bg="#ffffff",
                highlightthickness=1)

            self.entry1.place(
                x=185, y=428,
                width=388,
                height=28
                )
        else:
            try:
                self.ni.destroy()
                self.entry1.destroy()
            except:
                pass

    # 3- Caixa de entrada do lote do item        
    def lote(self, i = 0):
        if i == 0:
            self.li = Label(
                text='LOTE:',
                font="Inter 10 bold",
                bg='#ffffff'
            )

            self.li.place(
                x=24, y=483,
                width=155,
                height=20
                )

            self.entry2 = Entry(
                bd=0,
                bg="#ffffff",
                highlightthickness=1)

            self.entry2.place(
                x=185, y=478,
                width=388,
                height=28
                )
        else:
            try:
                self.li.destroy()
                self.entry2.destroy()
            except:
                pass

    # 4- Caixa de entrada da quantidade do item
    def qtd(self, i = 0):
        if i == 0:
            self.qi = Label(
                text='QUANTIDADE:',
                font="Inter 10 bold",
                bg='#ffffff'
            )

            self.qi.place(
                x=24, y=533,
                width=155,
                height=20
                )

            self.entry3 = Entry(
                bd=0,
                bg="#ffffff",
                highlightthickness=1)

            self.entry3.place(
                x=185, y=528,
                width=388,
                height=28
                )
        else:
            try:
                self.qi.destroy()
                self.entry3.destroy()
            except:
                pass
            
    ############################ CRIAÇÃO DOS BOTÕES DE ACÃO DO USUÁRIO #############################
    
    # 1- Botão de adicionar a quantidade do item
    def adc(self, i = 0):
        if i == 0:
            self.b5 = Button(
                text='ADICIONAR',
                foreground='#ffffff',
                font=('inter', 10, 'bold'),
                bg='#03989e',
                borderwidth=0,
                highlightthickness=0,
                command=self.btn_adc,
                relief="flat")

            self.b5.place(
                x=150, y=576,
                width=120,
                height=30)
        else:
            try:
                self.b5.destroy()
            except:
                pass

    # 2- Botão de diminuir a quantidade do item        
    def rem(self, i = 0):
        if i == 0:
            self.b6 = Button(
                text='REMOVER',
                foreground='#ffffff',
                font=('inter', 10, 'bold'),
                bg='#03989e',
                borderwidth=0,
                highlightthickness=0,
                command=self.btn_rem,
                relief="flat")

            self.b6.place(
                x=322, y=576,
                width=120,
                height=30)
        else:
            try:
                self.b6.destroy()
            except:
                pass
            
    # 3- Botão de confirmar a ação
    def confirmar(self, i = 0):
        if i == 0:
            self.b4 = Button(
                text='CONFIRMAR',
                foreground='#ffffff',
                font=('inter', 10, 'bold'),
                bg='#03989e',
                borderwidth=0,
                highlightthickness=0,
                command=self.btn_confirmar,
                relief="flat")

            self.b4.place(
                x=241, y=576,
                width=120,
                height=30)
        else:
            try:
                self.b4.destroy()
            except:
                pass
    
    # 4- Botão de retornar para a tela inicial            
    def reset(self, i = 0):
        if i == 0:
            self.br = Button(
                text='MENU',
                foreground='#ffffff',
                font=('inter', 10, 'bold'),
                bg='black',
                borderwidth=0,
                highlightthickness=0,
                command=self.btn_reset,
                relief="flat")

            self.br.place(
                x=256, y=335,
                width=90,
                height=25)
        else:
            try:
                self.b4.destroy()
            except:
                pass
        
    # 5- Histórico de edição do item
    def historico(self, i = 0):
        if i == 0:
            self.bh = Button(
                text='HISTÓRICO',
                foreground='#ffffff',
                font=('inter', 10, 'bold'),
                bg='black',
                borderwidth=0,
                highlightthickness=0,
                command=self.btn_hist,
                relief="flat")

            self.bh.place(
                x=400, y=576,
                width=120,
                height=30)
        else:
            try:
                self.bh.destroy()
            except:
                pass
    ############################## MÉTODOS AUXILIARES ##################################
    
    # Função de limpar os widgets de interação
    def limpar_tela(self):
        self.cod(1)
        self.nome(1)
        self.lote(1)
        self.qtd(1)
        self.adc(1)
        self.rem(1)
        self.confirmar(1)
        try:
            self.br.destroy()
        except:
            pass
        try:
            self.bh.destroy()
        except:
            pass
        try:
            self.tv2.destroy()
            self.scrlbar.destroy()
            self.tv.selection_set()
        except:
            pass
    
    # Função de exibir popups
    def popup(self, titulo, mensagem):
        tkinter.messagebox.showinfo(title=titulo, message=mensagem)
        
    # Função de Validação das entradas do usuário
    def validacoes(self, a, cod, lote):
        if a == 0:
            comando1 = f"""SELECT * FROM Itens
                    WHERE cod_item = '{cod}' AND lote_item = '{lote}';
                    """
            cursor.execute(comando1)
            j = len(cursor.fetchall())
            return j
        if a == 1:
            comando2 = f"""SELECT * FROM Itens
                    WHERE cod_item = '{cod}';
                    """
            cursor.execute(comando2)
            j = len(cursor.fetchall())
            return j
        
    # Função de atualizar a treeview principal
    def atualizar_tv(self):
        self.tv.delete(*self.tv.get_children())
        comando = f"""SELECT * FROM Itens
                """
        cursor.execute(comando)
        
        for item in cursor.fetchall():
            i,j,k,l,m = item
            self.tv.insert('', 'end', values=(i,j,k,l,m))
            
            
    ########################## MÉTODOS DE SALVAR O HISTÓRICO DE EDIÇÕES ############################
    
    # Salvar historico de criação de itens
    def salvar_hist_criacao(self, cod, nome, lote, qtd):
        agora = datetime.datetime.now()
        data = agora.date()
        hora = agora.time().strftime("%H:%M:%S")
        usuario = self.usuario
        acao = 'Criação do item'
        
        comando = f'''select id_item from Itens
            where cod_item = '{cod}' and lote_item = '{lote}' '''            
        cursor.execute(comando)
        
        fk = cursor.fetchall()[0][0]
    
        comando = f'''INSERT INTO Historico 
                        Values(
                        '{data}', 
                        '{hora}', 
                        '{usuario}', 
                        '{acao}',
                        '{fk}', 
                        '-',
                        '{cod}',
                        '-',
                        '{nome}',
                        '-',
                        '{lote}',
                        '',  
                        '{qtd}' )        
                        
                        '''            
        cursor.execute(comando)
        cursor.commit()
    
    # Salvar historico de exclusão de itens
    def salvar_hist_delete(self, cod, lote):
        agora = datetime.datetime.now()
        data = agora.date()
        hora = agora.time().strftime("%H:%M:%S")
        usuario = self.usuario
        acao = 'deletar'
        
        comando = f'''select id_item, nome_item, quantidade_item from Itens
            where cod_item = '{cod}' and lote_item = '{lote}' '''            
        cursor.execute(comando)
        
        lista_aux = cursor.fetchall()
        fk = lista_aux[0][0]
        nome = lista_aux[0][1]
        qtd = lista_aux[0][2]

        comando = f'''INSERT INTO Historico 
                        Values(
                        '{data}', 
                        '{hora}', 
                        '{usuario}', 
                        '{acao}',
                        '{fk}', 
                        '{cod}',
                        '-',
                        '{nome}',
                        '-',
                        '{lote}',
                        '-',
                        '{qtd}',
                        '0')        
                        
                        ''' 
        
        cursor.execute(comando)
        cursor.commit()
    
    # Salvar historico de modificação de quantidade de itens
    def salvar_hist_qtd(self, cod, lote, qtda, i):
        if i == 0:
            agora = datetime.datetime.now()
            data = agora.date()
            hora = agora.time().strftime("%H:%M:%S")
            usuario = self.usuario
            acao = 'adicionar qtd'
            
            comando = f'''select id_item, nome_item, quantidade_item from Itens
            where cod_item = '{cod}' and lote_item = '{lote}' '''            
            cursor.execute(comando)
            
            lista_aux = cursor.fetchall()
            
            fk = lista_aux[0][0]
            nome = lista_aux[0][1]
            qtd = lista_aux[0][2]
            qtda = int(qtda)
            qtda += int(qtd)
            
            comando = f'''INSERT INTO Historico 
                        Values(
                        '{data}', 
                        '{hora}', 
                        '{usuario}', 
                        '{acao}',
                        '{fk}', 
                        '{cod}',
                        '-',
                        '{nome}',
                        '-',
                        '{lote}', 
                        '-',
                        '{qtd}', 
                        '{qtda}')        
                        
                        ''' 
            cursor.execute(comando)
            cursor.commit()
            
        if i == 1:
            agora = datetime.datetime.now()
            data = agora.date()
            hora = agora.time().strftime("%H:%M:%S")
            usuario = self.usuario
            acao = 'remover qtd'
            
            comando = f'''select id_item, nome_item, quantidade_item from Itens
            where cod_item = '{cod}' and lote_item = '{lote}' '''            
            cursor.execute(comando)

            lista_aux = cursor.fetchall()
            
            fk = lista_aux[0][0]
            nome = lista_aux[0][1]
            qtd = lista_aux[0][2]
            qtda = int(qtda)
            qtda -= int(qtd)
            
            comando = f'''INSERT INTO Historico 
                        Values(
                        '{data}', 
                        '{hora}', 
                        '{usuario}', 
                        '{acao}',
                        '{fk}', 
                        '{cod}',
                        '-',
                        '{nome}',
                        '-',
                        '{lote}', 
                        '-',
                        '{qtd}', 
                        '{qtda}')        
                        
                        ''' 
            cursor.execute(comando)
            cursor.commit()
    
    # Salvar historico de edição de itens pelo botão de edição
    def salvar_hist_ed(self, fk, cod, nome, lote, qtd, acao):
        agora = datetime.datetime.now()
        data = agora.date()
        hora = agora.time().strftime("%H:%M:%S")
        usuario = self.usuario
        if acao == 'cod':
            
            comando = f'''select cod_item from Itens
            where id_item = '{fk}' '''            
            cursor.execute(comando)
            cod_n = cursor.fetchall()[0][0]
            
            comando = f'''INSERT INTO Historico 
                            Values(
                            '{data}', 
                            '{hora}', 
                            '{usuario}', 
                            '{acao}',
                            '{fk}', 
                            '{cod}', 
                            '{cod_n}',
                            '{nome}', 
                            '-',
                            '{lote}', 
                            '-',
                            '{qtd}',
                            '')        

                            ''' 
            cursor.execute(comando)
            cursor.commit()
            
        if acao == 'nome':
                
            comando = f'''select nome_item from Itens
            where id_item = '{fk}' '''            
            cursor.execute(comando)
            nome_n = cursor.fetchall()[0][0]
            
            comando = f'''INSERT INTO Historico 
                            Values(
                            '{data}', 
                            '{hora}', 
                            '{usuario}', 
                            '{acao}',
                            '{fk}', 
                            '{cod}',
                            '-',
                            '{nome}',
                            '{nome_n}',
                            '{lote}',
                            '-',
                            '{qtd}',
                            '')        

                            ''' 
            cursor.execute(comando)
            cursor.commit()
                
        if acao == 'lote':
            
            comando = f'''select lote_item from Itens
            where id_item = '{fk}' '''            
            cursor.execute(comando)
            lote_n = cursor.fetchall()[0][0]
            
            comando = f'''INSERT INTO Historico 
                            Values(
                            '{data}', 
                            '{hora}', 
                            '{usuario}', 
                            '{acao}',
                            '{fk}', 
                            '{cod}',
                            '-',
                            '{nome}',
                            '-',
                            '{lote}',
                            '{lote_n}',
                            '{qtd}',
                            '')        

                            ''' 
            cursor.execute(comando)
            cursor.commit()
            
      ####################### DEFININDO OS MÉTODOS EXECUTADOS PELOS BOTÕES DO MENU ############################
    
    # Função do Botão Criar novo item
    def btn_criar_novo_item(self):
        self.j = 1
        self.limpar_tela()
        self.b1.destroy()
        self.b2.destroy()
        self.b3.destroy()
        self.cod()
        self.nome()
        self.lote()
        self.qtd()
        self.confirmar()
        self.reset()
        
    # Função do Botão Procurar item    
    def btn_procurar_item(self):
        self.j = 3
        self.limpar_tela()
        self.b0.destroy()
        self.b2.destroy()
        self.b3.destroy()
        self.cod()
        self.confirmar()
        self.reset()
        
        
    # Função do Botão Editar qtd item   
    def btn_editar_qtd(self):
        self.limpar_tela()
        self.b0.destroy()
        self.b1.destroy()
        self.b2.destroy()
        self.cod()
        self.lote()
        self.qtd()
        self.adc()
        self.rem()
        self.reset()
        
    # Função do Botão Deletar item
    def btn_deletar_item(self):
        self.j = 2
        self.limpar_tela()
        self.b0.destroy()
        self.b1.destroy()
        self.b3.destroy()
        self.cod()
        self.lote()
        self.confirmar()
        self.reset()
        
    #################################### COMANDOS DOS BOTÕES ######################################
    
    # Função do Botão Editar item
    def btn_editar_item(self):
        selecionado = self.tv.focus()
        
        if selecionado:
            item = self.tv.item(selecionado,'values')
            lista = []
            
            for dado in item:
                lista.append(dado)
                
            janela_sec = Toplevel(self.janela)
            janela_sec.transient(self.janela)#
            janela_sec.focus_force()#
            janela_sec.grab_set()#
            pk = Label(janela_sec, text = "Id:")
            cod = Label(janela_sec, text = "Código:")
            nome = Label(janela_sec, text = "Nome:")
            lote = Label(janela_sec, text = "Lote:")
            qtd = Label(janela_sec, text = "Quantidade:")

            pk.grid(row=1, column=0)
            cod.grid(row=2, column=0)
            nome.grid(row=3, column=0)
            lote.grid(row=4, column=0)
            qtd.grid(row=5, column=0)

            tpk = Entry(janela_sec, width=30, highlightthickness=1)
            tpk.insert(0, item[0])
            tcod = Entry(janela_sec, width=30, highlightthickness=1)
            tcod.insert(0, item[1])
            tnome = Entry(janela_sec, width=30, highlightthickness=1)
            tnome.insert(0, item[2])
            tlote = Entry(janela_sec, width=30, highlightthickness=1)
            tlote.insert(0, item[3])
            tqtd = Entry(janela_sec, width=30, highlightthickness=1)
            tqtd.insert(0, item[4])
            tqtd.configure(state='disabled')
            tpk.configure(state='disabled')            

            tpk.grid(row=1, column=1)
            tcod.grid(row=2, column=1)
            tnome.grid(row=3, column=1)
            tlote.grid(row=4, column=1)
            tqtd.grid(row=5, column=1)

            def salvar_edicao():
                if tcod.get() != lista[1]:
                    comando = f"""UPDATE Itens
                    SET cod_item = '{tcod.get()}'
                    WHERE cod_item = '{lista[1]}' AND id_item = '{lista[0]}';
                    """
                    cursor.execute(comando)
                    cursor.commit()
                    self.atualizar_tv()
                    self.salvar_hist_ed(lista[0], lista[1], lista[2], lista[3], lista[4], 'cod')
                    lista[1] = tcod.get() 
                    
                    
                if tnome.get() != lista[2]:
                    comando = f"""UPDATE Itens
                    SET nome_item = '{tnome.get()}'
                    WHERE nome_item = '{lista[2]}' AND id_item = '{lista[0]}';
                    """
                    cursor.execute(comando)
                    cursor.commit()
                    self.atualizar_tv()
                    self.salvar_hist_ed(lista[0], lista[1], lista[2], lista[3], lista[4], 'nome')
                    lista[2] = tnome.get()
                    
                    
                if tlote.get() != lista[3]:
                    comando = f"""UPDATE Itens
                    SET lote_item = '{tlote.get()}'
                    WHERE lote_item = '{lista[3]}' AND id_item = '{lista[0]}';
                    """
                    cursor.execute(comando)
                    cursor.commit()
                    self.atualizar_tv()
                    self.salvar_hist_ed(lista[0], lista[1], lista[2], lista[3], lista[4], 'lote')
                    lista[3] = tlote.get()
                    
                
            def sair():
                janela_sec.destroy()
            
            salvar = Button(janela_sec, text='Salvar Alterações', command=salvar_edicao)
            salvar.grid(row=6, column=0, columnspan=2)
            
            fechar = Button(janela_sec, text='Fechar', command=sair)
            fechar.grid(row=7, column=0, columnspan=2)
            
            
        else:
            self.popup('AVISO','Nenhum Item Selecionado!')
            
    # Função do Botão histórico
    def btn_hist(self):
        selecionado = self.tv2.focus()
        
        if selecionado:
            item = self.tv2.item(selecionado,'values')
            janela_sec = Toplevel(self.janela)
            janela_sec.geometry("1000x400")
            janela_sec.transient(self.janela)#
            janela_sec.focus_force()#
            janela_sec.grab_set()#
            
            tvh = ttk.Treeview(janela_sec, columns=(
                'id_registro',
                'data',
                'hora',
                'usuario',
                'acao',
                'id_item',
                'cod',
                'cod_mod',
                'nome',
                'nome_mod',
                'lote',
                'lote_mod',
                'qtd',
                'qtd_mod'
                ),show='headings')
            cod = Label(janela_sec, text=f'HISTÓRICO DE EDIÇÕES - {item[1]}', font = 'Inter 14 bold', fg='#000000')
            cod.place(x=320, y=5, width=360)
            scrlbarx = ttk.Scrollbar(janela_sec,  
                               orient ="vertical",  
                               command = tvh.yview)
            
            scrlbary = ttk.Scrollbar(janela_sec,  
                               orient ="horizontal",  
                               command = tvh.xview)
            scrlbarx.place(x=983, y=64, height=318)
            scrlbary.place(x=0, y=383, width=1000)
            
            tvh.configure(yscrollcommand = scrlbarx.set, xscrollcommand = scrlbary.set)

            tvh.column('id_registro', minwidth=116 , width=116, anchor = N)
            tvh.column('data', minwidth=116 , width=116, anchor = N)
            tvh.column('hora', minwidth=116 , width=116, anchor = N)
            tvh.column('usuario', minwidth=116 , width=116, anchor = N)
            tvh.column('acao', minwidth=116 , width=116, anchor = N)
            tvh.column('id_item', minwidth=116 , width=116, anchor = N)
            tvh.column('cod', minwidth=116 , width=116, anchor = N)
            tvh.column('cod_mod', minwidth=116 , width=116, anchor = N)
            tvh.column('nome', minwidth=116 , width=116, anchor = N)
            tvh.column('nome_mod', minwidth=116 , width=116, anchor = N)
            tvh.column('lote', minwidth=116 , width=116, anchor = N)
            tvh.column('lote_mod', minwidth=116 , width=116, anchor = N)
            tvh.column('qtd', minwidth=116 , width=116, anchor = N)
            tvh.column('qtd_mod', minwidth=116 , width=116, anchor = N)

            tvh.heading('id_registro', text='ID_REG')
            tvh.heading('data', text='DATA_REG')
            tvh.heading('hora', text='HORA_REG')
            tvh.heading('usuario', text='USUARIO')
            tvh.heading('acao', text='AÇÃO')
            tvh.heading('id_item', text='ID_ITEM')
            tvh.heading('cod', text='CÓDIGO')
            tvh.heading('cod_mod', text='CÓD. MODIFICADO')
            tvh.heading('nome', text='NOME')
            tvh.heading('nome_mod', text='NOME MODIFICADO')
            tvh.heading('lote', text='LOTE')
            tvh.heading('lote_mod', text='LOTE MODIFICADO')
            tvh.heading('qtd', text='QTD')
            tvh.heading('qtd_mod', text='QTD MODIFICADO')

            comando = f'''select * from Historico
                where id_item = '{item[0]}' '''            
            cursor.execute(comando)
            
            for item in cursor.fetchall():
                #print(self.itens_procurados)
                a,b,c,d,e,f,g,h,i,j,k,l,m,n = item
                tvh.insert('', 'end', values=(a,b,c,d,e,f,g,h,i,j,k,l,m,n))
                
            tvh.place(x=0, y=40, width=1000, height=360)
        else:
            self.popup('AVISO','Nenhum Item Selecionado!')
        
    # Função do Botão Confirmar
    def btn_confirmar(self):
        try:
            cod = self.entry0.get()
        except:
            pass
        try:
            nome = self.entry1.get()
        except:
            pass
        try:
            lote = self.entry2.get()
        except:
            pass
        try:
            qtd = self.entry3.get()
        except:
            pass
        
        # Ação do botão Criar Novo Item
        if self.j == 1:
            if cod and nome and lote and qtd:
                if qtd.isnumeric():
                    j = self.validacoes(0, cod, lote)
                    if j == 0:
                        comando = f'''INSERT INTO Itens 
                        Values('{cod}', '{nome}', '{lote}', '{qtd}')'''
                        cursor.execute(comando)
                        cursor.commit()
                        self.atualizar_tv()
                        self.entry0.delete(0, END)
                        self.entry1.delete(0, END)
                        self.entry2.delete(0, END)
                        self.entry3.delete(0, END)
                        self.salvar_hist_criacao(cod, nome, lote, qtd)
                        self.popup('AVISO', 'PRODUTO ADICIONADO COM SUCESSO!')
                    else:
                        self.popup('AVISO','O item fornecido já está cadastrado no sistema! Se quiser alterar a quantidade deste item no estoque, utilize a opção EDITAR QUANTIDADE DO ITEM.')                    
                else:
                    self.popup('AVISO','DIGITE UM NÚMERO NA QUANTIDADE FORNECIDA!')
            else:
                self.popup('AVISO','Preencha todos os campos')

        
        # Ação do botão Deletar Item
        if self.j == 2:
            if cod and lote:
                j = self.validacoes(0, cod, lote)
                if j > 0:
                    self.salvar_hist_delete(cod, lote)
                    comando2 = f"""DELETE from Itens
                    WHERE cod_item = '{cod}' and lote_item = '{lote}';
                    """
                    cursor.execute(comando2)
                    cursor.commit()
                    self.atualizar_tv()
                    self.entry0.delete(0, END)
                    self.entry2.delete(0, END)
                    self.popup('AVISO', 'PRODUTO DELETADO COM SUCESSO!')
                else:
                    self.popup('AVISO','Produto Não Encontrado! Confira os Dados Fornecidos.')
            else:
                self.popup('AVISO','Preencha todos os campos')
        
        # Ação do botão Procurar Item
        if self.j == 3:
            if cod:
                try:
                    self.tv2.destroy()
                    self.scrlbar.destroy()
                except:
                    pass
                j = self.validacoes(1, cod, 0)
                if j > 0:
                    self.itens_procurados = []
                    selecao = []
                    for item in self.tv.get_children():
                        if cod in self.tv.item(item)['values']:
                            self.itens_procurados.append(self.tv.item(item)['values'])
                            selecao.append(item)
                    self.tv.selection_set(selecao)
                    self.treeview_sec()
                    self.entry0.delete(0, END)
                    self.historico()
                else:
                    self.popup('AVISO','Nenhum resultado encontrado!')
            else:
                self.popup('AVISO','Preencha todos os campos')
    
    # Ação do Botão Adicionar
    def btn_adc(self):
        cod = self.entry0.get()
        lote = self.entry2.get()
        qtd = self.entry3.get()
        if cod and lote and qtd:
            if qtd.isnumeric():
                j = self.validacoes(0, cod, lote)
                if j > 0:
                    self.salvar_hist_qtd(cod, lote, qtd, 0)
                    comando2 = f"""UPDATE Itens
                    SET quantidade_item = quantidade_item + {qtd}
                    WHERE cod_item = '{cod}' AND lote_item = '{lote}';
                    """
                    cursor.execute(comando2)
                    cursor.commit()
                    self.atualizar_tv()
                    self.entry0.delete(0, END)
                    self.entry2.delete(0, END)
                    self.entry3.delete(0, END)
                    
                    self.popup('AVISO', 'QUANTIDADE ADICIONADA COM SUCESSO!')
                else:
                    self.popup('AVISO','Produto Não Encontrado! Confira os Dados Fornecidos.')
            else:
                self.popup('AVISO','DIGITE UM NÚMERO NA QUANTIDADE FORNECIDA!')
        else:
            self.popup('AVISO','Preencha todos os campos')
            
    
    def qtd_est(self, cod, lote):
        comando = f"""SELECT quantidade_item FROM Itens
                    WHERE cod_item = '{cod}' AND lote_item = '{lote}';
                    """
        cursor.execute(comando)
        return int(cursor.fetchall()[0][0])
    
    # Ação do Botão Remover
    def btn_rem(self):
        cod = self.entry0.get()
        lote = self.entry2.get()
        qtd = self.entry3.get()
        if cod and lote and qtd:
            if qtd.isnumeric():
                j = self.validacoes(0, cod, lote)
                if j > 0:
                    if int(qtd) <= self.qtd_est(cod, lote):
                        self.salvar_hist_qtd(cod, lote, qtd, 1)
                        comando2 = f"""UPDATE Itens
                        SET quantidade_item = quantidade_item - {qtd}
                        WHERE cod_item = '{cod}' AND lote_item = '{lote}';
                        """
                        cursor.execute(comando2)
                        cursor.commit()
                        self.atualizar_tv()
                        self.entry0.delete(0, END)
                        self.entry2.delete(0, END)
                        self.entry3.delete(0, END)
                        self.popup('AVISO', 'QUANTIDADE REMOVIDA COM SUCESSO!')
                    else:
                        self.popup('AVISO', 'Você está tentando remover uma quantidade maior do que a presente no estoque!')
                    
                else:
                    self.popup('AVISO','Produto Não Encontrado! Confira os Dados Fornecidos.')
            else:
                self.popup('AVISO','DIGITE UM NÚMERO NA QUANTIDADE!')
        else:
            self.popup('AVISO','Preencha todos os campos')

    # Função do botão reset
    def btn_reset(self):
        self.limpar_tela()
        self.b0.destroy()
        self.b1.destroy()
        self.b2.destroy()
        self.b3.destroy()
        self.create()
        self.read()
        self.update()
        self.delete()
        self.atualizar_tv()

###################################################################################################
###################################################################################################
###################################################################################################
###################################################################################################
###################################################################################################

# JANELA DE LOGIN
janela = Tk()

# Configurações da janela de login
janela.geometry("500x400")
janela.title('Controle de Estoque - LOGIN')
background_img = PhotoImage(file=r"se_logo-1.png")
canvas = Canvas(
    janela,
    bg="#ffffff",
    height=400,
    width=500,
    bd=0,
    highlightthickness=0,
    relief="ridge")
canvas.place(x=0, y=0)
background = canvas.create_image(
    250, 100,
    image=background_img)

ce = Label(text='Login - Controle de Estoque', 
           font = 'Inter 12 bold', 
           bg='#ffffff', 
           fg='#03989e', 
           relief='flat')
ce.place(x=150, y=190, width=220)

# Widgets da janela de login
login = Label(text='Login:', font = 'Inter 10 bold', bg = '#ffffff', fg='#03989e')
login_ent = Entry(width=30, highlightthickness=1, borderwidth=2)
senha = Label(text='Senha:', font = 'Inter 10 bold', bg = '#ffffff', fg='#03989e')
senha_ent = Entry(width=30, highlightthickness=1, borderwidth=2, show='*')

login.place(x=113, y=232, width=70)
login_ent.place(x=188, y=232, width=200)
senha.place(x=113, y=262, width=70)
senha_ent.place(x=188, y=262, width=200)

# Acão do botão de login
def logar():
    if login_ent.get() and senha_ent.get():
        lg = login_ent.get()
        pw = senha_ent.get()
        
        comando = f"""SELECT * FROM Usuarios
                    WHERE login_usuario = '{lg}';
                    """
        cursor.execute(comando)
        if len(cursor.fetchall()) > 0:
            comando = f"""SELECT senha_usuario FROM Usuarios
                    WHERE login_usuario = '{lg}';
                    """
            cursor.execute(comando)
            if cursor.fetchall()[0][0] == pw:
                lg = login_ent.get()
                janela.destroy()
                app(lg)
                
            else:
                tkinter.messagebox.showinfo(title='Aviso', message='Dados Inválidos')
        else:
            tkinter.messagebox.showinfo(title='Aviso', message='Usuário não encontrado.')
    else:
        tkinter.messagebox.showinfo(title='Aviso', message='Preencha os campos!')

# Botão de login        
entrar = Button(text='Entrar', 
                font = 'Inter 10 bold', 
                bg='#03989e', 
                fg='#ffffff', 
                relief='flat', 
                command=logar) 
entrar.place(x=225, y=295, width=70)

janela.mainloop()

