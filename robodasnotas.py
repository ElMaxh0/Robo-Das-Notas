#!/usr/bin/env python
# coding: utf-8
#Maded On Anaconda Notepad V3.0
# In[ ]:


import pyautogui
import time
import pandas as pd
import easygui
import plotly.express as px

#LOGA AUTOMATICAMENTE E SOLICITA O DOWNLOAD DO ARQUIVO COM TODAS AS NOTAS 
numerodamatricula = ""
datanascimento = ""
time.sleep(4)
pyautogui.PAUSE = 2
pyautogui.hotkey('ctrl', 't')
pyautogui.write('estudanteonline.sed.sc.gov.br')
pyautogui.press("enter")
pyautogui.click(1129, 405)
pyautogui.hotkey('ctrl', 'a')
pyautogui.press("del")
pyautogui.write(numerodamatricula)
pyautogui.press("tab")
pyautogui.write(datanascimento)
pyautogui.click(1031, 514)
pyautogui.click(1074, 597)
pyautogui.click(1195, 462)
pyautogui.click(1234, 508)
pyautogui.click(1195, 462)
pyautogui.click(1132, 490)
pyautogui.click(1052, 522)
pyautogui.click(607, 130)
pyautogui.click(238, 196)

#PEGA O ARQUIVO COM TODAS AS NOTAS BAIXADO DO SITE DO GOVERNO E O ANALISA 
arquivo_sys="C://Users/picin/Downloads/ConsultaAtividadeNotasExport-786.xlsx"

#Calcula A MAEDIA GERAL E DA UM AVISO QUE GEROU COM SUCESSO 
notas = pd.read_excel(arquivo_sys)
soma = notas['Nota'].sum()
totalnotas = notas['Nota'].count()
mediageral =soma/totalnotas
print("A Media de suas Notas É")
print(soma/totalnotas)
easygui.msgbox("NOTAS RECEBIDAS COM SUCESSO  " , title="Notas")
easygui.msgbox("Media Geral De Notas " , title="Notas")
easygui.msgbox(mediageral , title="Notas")

#FILTRA POR DISCIPLINA E COLOCA O RESULTADO EM UMA VARIAVEL 
notasFIS_mask=notas['Disciplina.1'] == "FIS"
filtered_notasFIS = notas[notasFIS_mask]

notashist_mask=notas['Disciplina.1'] == "HIS"
filtered_notashist = notas[notashist_mask]

notasGEO_mask=notas['Disciplina.1'] == "GEO"
filtered_notasGEO = notas[notasGEO_mask]

notasLPL_mask=notas['Disciplina.1'] == "LPL"
filtered_notasLPL = notas[notasLPL_mask]

notasSOC_mask=notas['Disciplina.1'] == "SOC"
filtered_notasSOC = notas[notasSOC_mask]

notasEFI_mask=notas['Disciplina.1'] == "EFI"
filtered_notasEFI = notas[notasEFI_mask]

notasLEI_mask=notas['Disciplina.1'] == "LEI"
filtered_notasLEI = notas[notasLEI_mask]

notasQUI_mask=notas['Disciplina.1'] == "QUI"
filtered_notasQUI = notas[notasQUI_mask]

#CALCULA A MEDIA DE CADA DISCIPLINA 
FISsoma= filtered_notasFIS['Nota'].sum()
FIStotal=filtered_notasFIS['Nota'].count()
QUIsoma= filtered_notasQUI['Nota'].sum()
QUItotal=filtered_notasQUI['Nota'].count()
SOCsoma= filtered_notasSOC['Nota'].sum()
SOCtotal=filtered_notasSOC['Nota'].count()
EFIsoma= filtered_notasEFI['Nota'].sum()
EFItotal=filtered_notasEFI['Nota'].count()
LPLsoma= filtered_notasLPL['Nota'].sum()
LPLtotal=filtered_notasLPL['Nota'].count()
LEIsoma= filtered_notasLEI['Nota'].sum()
LEItotal=filtered_notasLEI['Nota'].count()
GEOsoma= filtered_notasGEO['Nota'].sum()
GEOtotal=filtered_notasGEO['Nota'].count()
histsoma= filtered_notashist['Nota'].sum()
histtotal=filtered_notashist['Nota'].count()

print("SUAS MEDIAS ")
print ("FISICA")
print(FISsoma/FIStotal)

print ("QUIMICA")
print(QUIsoma/QUItotal)

print ("SOCIOLOGIA")
print(SOCsoma/SOCtotal)

print ("EFISICA")
print(EFIsoma/EFItotal)

print ("LINGUA PORTUGUESA E LITERATURA ")
print(LPLsoma/LPLtotal)

print ("LINGUA ESTRANGEIRA INGLES ")
print(LEIsoma/LEItotal)

print ("GEGRAFIA")
print(GEOsoma/GEOtotal)

print ("Historia ")
print(histsoma/histtotal)


print("GRAFICOS")
print("Desempenho em Sociologia ")
#GERA O GRAFICO
fig = px.histogram(filtered_notasSOC, x="Data", y="Nota", nbins= 30,)
fig.show()
#EXIBE AS NOTAS DA DISCIPLINA 
print("SUAS NOTAS DE SOCIOLOGIA ")
display(filtered_notasSOC)
#REPETE EM TODOS ABAIXO A MESMA SEQUENCIA 
print("Desempenho em QUIMICA ")
fig1 = px.histogram(filtered_notasQUI, x="Data", y="Nota", nbins= 30,)
fig1.show()
print("SUAS NOTAS DE QUIMICA ")
display(filtered_notasQUI)
print("Desempenho em FISICA ")
fig2 = px.histogram(filtered_notasFIS, x="Data", y="Nota", nbins= 30,)
fig2.show()
print("SUAS NOTAS DE FISICA ")
display(filtered_notasFIS)
print("Desempenho em LINGUA PORTUGUESA ")
fig3 = px.histogram(filtered_notasLPL, x="Data", y="Nota", nbins= 30,)
fig3.show()
print("SUAS NOTAS DE LINGUA PORTUGUESA E LITERATURA  ")
display(filtered_notasLPL)
print("Desempenho em LINGUA inglesa")
fig4 = px.histogram(filtered_notasLEI, x="Data", y="Nota", nbins= 30,)
fig4.show()
print("SUAS NOTAS DE LINGUA ESTRANGEIRA E LITERATURA ")
display(filtered_notasLEI)
print("Desempenho em GEOGRAFIA")
fig5 = px.histogram(filtered_notasGEO, x="Data", y="Nota", nbins= 30,)
fig5.show()
print("SUAS NOTAS DE GEOGRAFIA  ")
display(filtered_notasGEO)
print("Desempenho em Historia")
fig6 = px.histogram(filtered_notashist, x="Data", y="Nota", nbins= 30,)
fig6.show()
print("SUAS NOTAS DE HISTORIA  ")
display(filtered_notashist)
print("Desempenho em EFisica")
fig7 = px.histogram(filtered_notasEFI, x="Data", y="Nota", nbins= 30,)
fig7.show()
print("SUAS NOTAS DE EDUCAÇÃO FISICA ")
display(filtered_notasEFI)

#EXIBE TODAS AS NOTAS 
print("TODAS SUAS NOTAS ")
display (notas)



