# -*- coding: utf-8 -*-
from kafka import KafkaProducer
from kafka.errors import KafkaError
import datetime
import sys
import os

reload(sys)  
sys.setdefaultencoding('utf8')

file = "iptcphttp.csv"
servidor_kafka = 'vm-cdl-d-10:9092'
topico_kafka = 'ip-tcp-http'
port = 4242
refreshRate = 1000
separator = ";"
kafka_producer = KafkaProducer(bootstrap_servers=[servidor_kafka])

def calcula_data (timestamp, formato):
	data = datetime.datetime.fromtimestamp(timestamp).strftime(formato)
	return data
	
def calcula_posicao (filtros, campo):
	i = 0
	for filtro in filtros:
		if filtro == campo:
			return i
		i += 1

def calcula_linhas (arquivo):
	with open(arquivo) as f:
		for i, l in enumerate(f):
			pass
	return i+1
	
def update_progress(count, total, suffix='Enviando o CSV no topico...'):
    bar_len = 100
    filled_len = int(round(bar_len * count / float(total)))

    percents = round(100.0 * count / float(total), 1)
    bar = '=' * filled_len + '-' * (bar_len - filled_len)

    sys.stdout.write('[%s] %s%s %s\r' % (bar, percents, '%', suffix))
    sys.stdout.flush()
	
def descobre_protocolo(filtros):
	if "telnet" in filtros[-1]:
		return "telnet"
	elif "dns" in filtros[-1]:
		return "dns"
	elif "ssh" in filtros[-1]:
		return "ssh"
	elif "http" in filtros[-1]:
		return "http"
		
def main ():
	
	total_linhas = calcula_linhas(file)
	linha_atual = 1
	
	with open(file) as arquivo:
	
		filtros = arquivo.readline().split(separator)
		protocolo = descobre_protocolo(filtros)
		posicao_time_epoch = calcula_posicao(filtros,"frame.time_epoch")
		
		for linha in arquivo:
			try:
				timestamp = float(linha.split(separator)[posicao_time_epoch])
				mensagem = calcula_data(timestamp,'%Y-%m-%dT%H:%M:%S.%f') +\
						   separator +\
					       calcula_data(timestamp,'%Y-%m-%d') +\
					       separator +\
						   protocolo +\
						   separator
						   
				mensagem = mensagem + linha
			
				kafka_producer.send(topico_kafka, mensagem.encode('utf-8'))
				#print (mensagem)
				#break
			except:
				pass
				#print ("Encontrada linha sem estampa de tempo. Ignorando.")
				
			update_progress(linha_atual, total_linhas)
			linha_atual +=1
	
	print("\n")
	print ("Terminado.")
	
if __name__ == "__main__":
	main()