#!/usr/bin/env python
# pylint: disable=C0116,W0613
# This program is dedicated to the public domain under the CC0 license.

"""
Simple Bot to reply to Telegram messages.

First, a few handler functions are defined. Then, those functions are passed to
the Dispatcher and registered at their respective places.
Then, the bot is started and runs until we press Ctrl-C on the command line.

Usage:
Basic Echobot example, repeats messages.
Press Ctrl-C on the command line or send a signal to the process to stop the
bot.
"""
from fileinput import filename
from telegram import ChatAction
import os
from socket import timeout
from datetime import datetime
import random
from time import sleep
from tqdm import tqdm

lista_num=[]
numeros=[]
abre=('BEGIN:VCARD')
cierra=('END:VCARD')
now = datetime.now()
horas = now.time()
horas = str(horas)
horass = replaced_text = horas.replace(':', '')
nombre_file_vcf=(str(horass)+' numeros.vcf')
limite=100000
filename=0

import logging

import telegram
from telegram import InlineKeyboardMarkup, InlineKeyboardButton, Update, ForceReply, ChatAction
from telegram import Update, ForceReply
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext

# Enable logging
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO
)

logger = logging.getLogger(__name__)


# Define a few command handlers. These usually take the two arguments update and
# context.

def porcentaje(Porcentaje, update, context):
    chat = update.message.chat
    chat.send_action(
        
        action=ChatAction.TYPING,
        timeout=None
    )
    print(Porcentaje, "%" )
    
    
def send_txt(filename, chat):
    
    chat.send_document(
                
                document= open (filename,'rb')
            )


def generador(update, context):
        
    i = 1
    while i <= limite:
      
        num= random.randint(900000000, 999999999)
        medio=("TEL;CELL:"+str(num))
        lista_num=(abre,medio,cierra)
        numeros=(str(num))
        with open(nombre_file_vcf, 'a') as temp_file:
         for item in lista_num:
            temp_file.write("%s\n" % item)
        f = open ('todos.txt','a')
        f.write(str(numeros + '\n'))
        f.close()
        i = i + 1
        Porcentaje= i/1000
        if Porcentaje == 5 or Porcentaje ==10 or Porcentaje == 15 or Porcentaje == 20 or Porcentaje == 25 or Porcentaje == 30 or Porcentaje ==35 or Porcentaje == 40 or Porcentaje ==45 or Porcentaje == 50 or Porcentaje == 55 or Porcentaje == 60 or Porcentaje ==65 or Porcentaje == 70 or Porcentaje ==75 or Porcentaje == 80 or Porcentaje == 85 or Porcentaje ==90 or Porcentaje == 95:
           
           porcentaje(Porcentaje, update, context)
           
        elif Porcentaje == 100:
           
            print ('Terminado')
            
            chat = update.message.chat
            chat.send_action(
        
            action=ChatAction.UPLOAD_DOCUMENT,
            timeout=None
        )
        
            filename= 'todos.txt'
            send_txt(filename, chat)
            
            os.unlink(filename)
            
            filename= nombre_file_vcf
            send_txt(filename, chat)
            
            os.unlink(filename)
            

        
            
        else:
         
            Porcentaje= i/1000 
         
    



def start(update: Update, context: CallbackContext) -> None:
    """Send a message when the command /start is issued."""
    user = update.effective_user
    update.message.reply_markdown_v2(
        fr'Hi {user.mention_markdown_v2()}\!',
        reply_markup=ForceReply(selective=True),
    )


def help_command(update: Update, context: CallbackContext) -> None:
    """Send a message when the command /help is issued."""
    update.message.reply_text('Help!')


def echo(update: Update, context: CallbackContext) -> None:
    """Echo the user message."""
    update.message.reply_text(update.message.text)


def main() -> None:
    """Start the bot."""
    # Create the Updater and pass it your bot's token.
    updater = Updater("5169103798:AAF2AZtUq9LOncmgU3FfY2XyHlbHfkQRGcg")

    # Get the dispatcher to register handlers
    dispatcher = updater.dispatcher

    # on different commands - answer in Telegram
    dispatcher.add_handler(CommandHandler("start", start))
    dispatcher.add_handler(CommandHandler("help", help_command))

    # on non command i.e message - echo the message on Telegram
    dispatcher.add_handler(MessageHandler(Filters.text & ~Filters.command, generador))

    # Start the Bot
    updater.start_polling()

    # Run the bot until you press Ctrl-C or the process receives SIGINT,
    # SIGTERM or SIGABRT. This should be used most of the time, since
    # start_polling() is non-blocking and will stop the bot gracefully.
    updater.idle()


if __name__ == '__main__':
    main()
