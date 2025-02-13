import customtkinter as ctk

c0 = "#2c3c67"
c1 = "#8894c6"
c2 = "#5a6897"
c3 = "#717eae"
c4 = "#43527f"
c5 = "#6a6a6a"


janela = ctk.CTk()
janela.title("Calculadora IMC")
janela.geometry('440x520')
janela.configure(bg=c3)

quadro_superior = ctk.CTkFrame(janela, width=400, height=90, corner_radius=15)
quadro_superior.grid(row=0, column=0, sticky='nsew', padx=20, pady=20)

quadro_inferior = ctk.CTkFrame(janela, width=400, height=400, corner_radius=15)
quadro_inferior.grid(row=0, column=0, sticky='nsew', padx=20, pady=20)

nome_app = ctk.CTkLabel(quadro_superior, text='Calculadora de IMC',text_color=c4, anchor='center', font=('Helvetica', 30, 'bold'))
nome_app.place(x=0, y=25, relwidth=1)

def calcular():
    try:
        peso = float(e_peso.get())
        altura = float(e_altura.get())

        # Verificar se a altura e peso são válidos
        if peso <= 0 or altura <= 0:
            l_texto_resultado.configure(text='Erro: Peso e altura devem ser positivos!')
            return

        # Verificar se a altura foi inserida em metros ou centímetros (se for > 3 metros, considerar como centímetros)
        if altura > 3:
            altura = altura / 100  # Converter para metros

        resultado = peso / (altura ** 2)

        if resultado < 18.5:
            l_texto_resultado.configure(text='Seu IMC é: Abaixo do peso.')
        elif resultado < 24.9:
            l_texto_resultado.configure(text='Seu IMC é: Normal')
        elif resultado < 29.9:
            l_texto_resultado.configure(text='Seu IMC é: Sobrepeso')
        else:
            l_texto_resultado.configure(text='Seu IMC é: Obesidade')

        l_resultado.configure(text=f"{resultado:.2f}")
    except ValueError:
        l_texto_resultado.configure(text='Erro: Insira valores numéricos válidos!')

# Criar os labels para os campos de entrada
l_peso = ctk.CTkLabel(quadro_inferior, text='Digite seu peso(Kg)', text_color=c0, font=('Helvetica', 14))
l_peso.grid(row=0, column=0, sticky='nw', padx=15, pady=15)

# Criar as entradas corretas e armazená-las em variáveis distintas
e_peso = ctk.CTkEntry(quadro_inferior, width=180, font=('Helvetica', 16), justify='center', corner_radius=12)
e_peso.grid(row=0, column=1, sticky='nsew', padx=15, pady=15)

l_altura = ctk.CTkLabel(quadro_inferior, text='Digite sua altura(M)', text_color=c0, font=('Helvetica', 14))
l_altura.grid(row=1, column=0, sticky='nw', padx=15, pady=15)

e_altura = ctk.CTkEntry(quadro_inferior, width=180, font=('Helvetica', 16), justify='center', corner_radius=12)
e_altura.grid(row=1, column=1, sticky='nsew', padx=15, pady=15)


l_resultado = ctk.CTkLabel(quadro_inferior, text='---',width=5, height=1,text_color=c0, font=('Helvetica', 32, 'bold'), anchor='center', corner_radius=12)
l_resultado.grid(row=2, column=0, columnspan=2, padx=15, pady=30)

l_texto_resultado = ctk.CTkLabel(quadro_inferior, text='', text_color=c0, font=('Helvetica', 16), anchor='center')
l_texto_resultado.grid(row=3, column=0, columnspan=2, padx=15, pady=15)

b_calcular = ctk.CTkButton(quadro_inferior, text='Calcular', width=180, height=50, font=('Helvetica', 16, 'bold'),fg_color=c2, hover_color="#78eff2", corner_radius=12, command=calcular)
b_calcular.grid(row=4, column=0, columnspan=2, padx=15, pady=25)



janela.mainloop()