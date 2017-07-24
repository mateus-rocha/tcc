#!/bin/bash

#DECLARACAO DE FUNCOES

morra () 
{ 
	echo $0: $1
	exit 1
}

#VALIDACAO DE ARGUMENTOS

while getopts a:p: opcao 
do
	case "${opcao}" in
		a) ARQUIVO=${OPTARG};;
		p) PROTOCOLO=${OPTARG};;
	esac
done

if [ ! -f $ARQUIVO ];
then
	morra "Arquivo $ARQUIVO nao encontrado"
fi

case $PROTOCOLO in
	"tcp") :;;
	"udp") :;;
	 "ip") :;;
	    *) morra "Protocolo $PROTOCOLO nao suportado ou nao reconhecido"
esac

#PADRONIZACAO DE ARQUIVO

dos2unix $ARQUIVO

if [ $? -ne 0 ]; 
then
	morra "O comando dos2unix falhou em converter o arquivo $ARQUIVO."
fi

#PROCESSAMENTO DO ARQUIVO

IFS=';' read -a filtros <<< $(head -n 1 $ARQUIVO)

sed 1d $ARQUIVO | while IFS='' read -a linha || [[ -n "$linha" ]]; 
do

	IFS=';' read -a valores <<< $linha

	comandoTSDB="$(echo ${valores[0]} | cut -d'.' -f 1)"
        comandoTSDB="put ip $comandoTSDB 1"
	
	for index in "${!valores[@]}"; 
	do	
		if [ ! -z ${valores[$index]} ] && [[ ${valores[$index]} != *","* ]]; 
		then
			comandoTSDB="$comandoTSDB ${filtros[$index]}=${valores[$index]}"
		fi 
	done
	
	echo $comandoTSDB
done	
