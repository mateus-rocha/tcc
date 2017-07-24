import socket
import sys

file = "2016-08-01_2016-08-31_ip1.csv"
host = "172.16.20.39"
port = 4242
refreshRate = 1000
metric = "ip.1"

def calculaLinhas (arquivo):
	with open(arquivo) as f:
		for i, l in enumerate(f):
			pass
	return i+1
	
def update_progress(count, total, suffix='Enviando arquivos para openTSDB...'):
    bar_len = 100
    filled_len = int(round(bar_len * count / float(total)))

    percents = round(100.0 * count / float(total), 1)
    bar = '=' * filled_len + '-' * (bar_len - filled_len)

    sys.stdout.write('[%s] %s%s %s\r' % (bar, percents, '%', suffix))
    sys.stdout.flush()
	
try:
	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
except socket.error, msg:
	print 'Failed to create socket. Error code: ' + str(msg[0]) + ', Error message: ' + msg[1]
	sys.exit();

print 'Criando um novo socket.'

s.connect((host, port))

print 'Socket conectado a 172.16.20.39, na porta ' + str(port)

totalLinhas = calculaLinhas (file)
linhaAtual = 1.0
progresso = 0

print 'Abrindo arquivo ' + file
print 'Iniciando envio ao banco de dados'

with open(file) as arquivo:

	filtros = arquivo.readline().split(";")
	for linha in arquivo:
	
		valores = linha.rstrip('\n').split(";")
		comandoTSDB = 'put ' + metric + ' ' + valores[0].split(".")[0] + ' 1'
		
		for filtro, valor in zip(filtros, valores):
		
				if valor and "," not in valor and ":" not in valor and "frame.time_epoch" not in filtro:
					comandoTSDB = comandoTSDB + ' ' + filtro.strip('\n').strip('\r') + '=' + valor.strip('\n').strip('\r')
					
		try:
			print comandoTSDB
			s.sendall(comandoTSDB + "\n")
			if ((linhaAtual%refreshRate) == 0):
				update_progress(linhaAtual, totalLinhas)
				
		except socket.error:
			print 'Send failed'
			sys.exit()
			
		linhaAtual+=1

print 'Pronto!'