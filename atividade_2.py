import datetime
start_time = datetime.datetime.now()

arq=open('dataset-2-e.csv','r')
conteudo=arq.read()
arq.close()
dados = conteudo.split('\n')

maior = 0
for x in dados:
    if int(x) > int(maior):
        maior = x

arq2=open('resposta-dataset-2-e.txt','w')
arq2.write(maior+'\n')

end_time = datetime.datetime.now()
time_diff = (end_time - start_time)
execution_time = time_diff.total_seconds() * 1000

arq2.write(str(execution_time)+'\n')
arq2.close()
