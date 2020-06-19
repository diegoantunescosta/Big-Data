# coding: utf-8
#Programa: Comunicação MQTT com Python

#importando bibliotecas
import paho.mqtt.client as mqtt
import sys

#Definições
broker = "test.mosquitto.org"
portaBroker = 1883
keepAliveBroker = 60
topicoSubscribe = "topic"

#Função para conectar no broker
def on_connect(client, userdata, flags, rc):
    print("[STATUS] Conectado ao Broker. Resultado da conexão: "+str(rc))
    
    #Assinar tópico
    client.subscribe(topicoSubscribe)
    
def on_message(client, userdata, msg):
    mensagemRecebida = str(msg.payload)
    
    #Imprimir mensagem recebida
    print("[MENSAGEM] Tópico: "+msg.topic+" /Mensagem:"+mensagemRecebida)
    if(mensagemRecebida == 0 ):
      print('fodase')
    

try: 
    print("[STATUS] Inicializando o MQTT...")
    client = mqtt.Client()    
    client.on_connect = on_connect
    client.on_message = on_message
    
    client.connect(broker, portaBroker, keepAliveBroker)
    client.loop_forever()
except KeyboardInterrupt:
    print("\n ctrl+C pressionado, encerrando aplicação e saindo..")
    sys.exit(0)