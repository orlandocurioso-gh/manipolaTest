import os

def pulisciLaLista(lista):     
    for elemento in lista:
        posizione=lista.index(elemento)
        riga=elemento.split(';')
        if riga[0]=='N°':
            lista.pop(posizione)
    return lista

listaFile=os.listdir('.\\doc\\')
for fileSingolo in listaFile:
    if not os.path.isdir('.\\doc\\'+fileSingolo):
        nomeFile=fileSingolo.split('.')[0]
        with open ('.\\doc\\'+nomeFile+'.csv','r') as file:
            fileDomande=open('.\\out\\'+nomeFile+'_domande.csv','a')
            fileRisposte=open('.\\out\\'+nomeFile+'_risposte.csv','a')
            fileDomande.write('id_domanda;tipo;peso;Domanda;selezione;sort\n')
            fileRisposte.write('id_domanda;Risposta;corretta;id_risposta;sort\n')
            os.system('cls')
            quiz=file.readlines()
            quizPulito=pulisciLaLista(quiz)
            for elemento in quizPulito:
                riga=elemento.split(';')
                fileDomande.write(riga[0]+';1;1;'+riga[1]+';1;1\n')
                fileRisposte.write(riga[0]+';'+riga[2]+';1;1;1\n')
                fileRisposte.write(riga[0]+';'+riga[3]+';0;2;1\n')
                fileRisposte.write(riga[0]+';'+riga[4]+';0;3;1\n')
                fileRisposte.write(riga[0]+';'+riga[5][:-1]+';0;4;1\n')
                #print (riga)
fileDomande.close()
fileRisposte.close()