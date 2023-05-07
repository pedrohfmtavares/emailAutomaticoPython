import pyautogui,time
import win32com.client as win32


# ALERTA QUE A AUTOMAÇÃO COM O PYTHON VAI COMEÇAR E O USUÁRIO NÃO PODERÁ MEXER NO MOUSE E NEM NO TECLADO DURANTE ELA
pyautogui.alert("O seu computador vai ser controlado pelo Python em 5 segundos a partir da confirmação 'Ok',por favor não pressione nenhuma tecla do seu teclado nem do seu mouse após a confirmação!!!")

# APERTANDO A TECLA DO WINDOWS
time.sleep(5)
pyautogui.press('win')


# ABRINDO O NAVEGADOR
time.sleep(2)
pyautogui.write('Navegador Opera GX')


# CONFIRMANDO A AÇÃO DE ABRIR O NAVEGADOR
time.sleep(2)
pyautogui.press('enter')


# ENTRANDO NO GMAIL
time.sleep(3.5)
pyautogui.write('gmail.com')


# CONFIRMANDO A AÇÃO DE ENTRAR NO GMAIL
time.sleep(2)
pyautogui.press('enter')


# EVENTO DE CLICK (OS NÚMEROS SERÃO DIFERENTES DE ACORDO COM A RESOLUÇÃO ATUAL DO COMPUTADOR EM QUE O CÓDIGO ESTÁ SENDO RODADO,É APENAS UM EXEMPLO)
time.sleep(2)
pyautogui.click(131, 187)


# ESCREVENDO O EMAIL
time.sleep(2.5)
pyautogui.write('pedromotta01040104@gmail.com')


# CONFIRMANDO A AÇÃO DE ESCREVER O EMAIL
time.sleep(2)
pyautogui.press('enter')


# EVENTO DE CLICK (OS NÚMEROS SERÃO DIFERENTES DE ACORDO COM A RESOLUÇÃO ATUAL DO COMPUTADOR EM QUE O CÓDIGO ESTÁ SENDO RODADO,É APENAS UM EXEMPLO)
time.sleep(2.5)
pyautogui.click(840, 435)


# ESCREVENDO O ASSUNTO DO EMAIL COM A PALAVRA 'Teste',PORÉM,PODERIA SER QUALQUER ASSUNTO DO COTIDIANO
time.sleep(1.5)
pyautogui.write('Teste')


# EVENTO DE CLICK (OS NÚMEROS SERÃO DIFERENTES DE ACORDO COM A RESOLUÇÃO ATUAL DO COMPUTADOR EM QUE O CÓDIGO ESTÁ SENDO RODADO,É APENAS UM EXEMPLO) 
time.sleep(2.5)
pyautogui.click(848, 452)


# ESCREVENDO O TEXTO DO EMAIL COM A PALAVRA 'Teste',PORÉM,PODERIA SER QUALQUER TEXTO DO COTIDIANO
time.sleep(2.5)
pyautogui.write('Teste')


# EVENTO DE CLICK (OS NÚMEROS SERÃO DIFERENTES DE ACORDO COM A RESOLUÇÃO ATUAL DO COMPUTADOR EM QUE O CÓDIGO ESTÁ SENDO RODADO,É APENAS UM EXEMPLO)
time.sleep(2.5)
pyautogui.click(828, 822)


# FECHANDO AS ABAS ABERTAS,UTILIZANDO O ATALHO "ALT + F4" DO TECLADO
time.sleep(3.5)
pyautogui.hotkey('alt', 'f4')


# ALERTA DIZENDO QUE A AUTOMAÇÃO JÁ ACABOU E QUE O USUÁRIO PODE MEXER NO COMPUTADOR A VONTADE
time.sleep(1)
pyautogui.alert("A automação com Python já terminou,agora você pode usar seu computador normalmente,obrigado!")