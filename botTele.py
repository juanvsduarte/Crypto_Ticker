from cProfile import run
from turtle import clear
from pandas import ExcelFile
import telebot
from readcrypto import btc , eth



CHAVE_API = "5593131632:AAEW0OJ93-u2ucGyP48x-geySzuL977xM10"

bot = telebot.TeleBot(CHAVE_API)


@bot.message_handler(commands=["opcao1"])
def opcao1(mensagem):
    bot.send_message(mensagem.chat.id, btc)

@bot.message_handler(commands=["opcao2"])
def opcao2(mensagem):
    bot.send_message(mensagem.chat.id, eth)

@bot.message_handler(commands=["opcao3"])
def opcao3(mensagem):
    bot.reply_to(mensagem, "Email enviado")

def verificar(mensagem):
    return True

@bot.message_handler(func=verificar)
def responder(mensagem):
    texto = """
    Escolha uma opção para continuar (Clique no item):
     /opcao1 Bitcoin
     /opcao2 Ethereum
     /opcao3 Enviar preço por email
Responder qualquer outra coisa não vai funcionar, clique em uma das opções"""
    bot.reply_to(mensagem, texto)

bot.polling()