from argparse import Action
import os
from socket import timeout
import time
import requests
from bs4 import BeautifulSoup
from requests.structures import CaseInsensitiveDict
from colorama import Fore, init
from urllib3.exceptions import InsecureRequestWarning
from requests.packages.urllib3.exceptions import InsecureRequestWarning
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)
init()

import logging

from telegram import Update
from telegram.ext import CommandHandler
from telegram.ext import Updater
#from telegram.ext import CallbackContext
from telegram.ext import Filters
from telegram.ext import MessageHandler
from telegram.ext import ConversationHandler
from telegram import ForceReply
from telegram.ext import ChatAction



# Enable logging
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO
)

logger = logging.getLogger(__name__)

INPUT_NAME =0
nombre = []

# Define a few command handlers. These usually take the two arguments update and
# context.
def start(update, context) -> None:
    """Send a message when the command /start is issued."""
    user = update.effective_user
    update.message.reply_markdown_v2(
        fr'Hi {user.mention_markdown_v2()}\!',
        reply_markup=ForceReply(selective=True),
    )
    update.message.reply_text('Bienvenido!\n\nEnvíame /buscar para buscar el dni de una persona a partir de los nombres')



def help_command(update, context) -> None:
    """Send a message when the command /help is issued."""
    update.message.reply_text('Help!')

def buscar_dni(update, context):
    
    update.message.reply_text('Envíame el nombre completo')
    return INPUT_NAME
    
    

def consulta_por_nombres(update, context):
    chat = update.message.chat
    chat.send_action(
        
        action=ChatAction.TYPING,
        timeout=None
    )
    nombre = [update.message.text]
    nombrenew = (update.message.text.replace(' ', ','))
    largo_nom = (nombrenew.count(','))
    largo_nombre = len(nombrenew)
    indice_c = nombrenew.index(',')
    
    if largo_nom == 1: 
    
        nombre1 = nombrenew[0:indice_c]
        apellido1 = nombrenew[indice_c + 1:largo_nombre]
        nombre = nombre1
        name = (nombre)
        apellidop = apellido1
        apellidom = ' '
        url = "https://buscardni.xyz/buscador/ejemplo_ajax_proceso.php"
        headers = CaseInsensitiveDict()
        headers["Content-Type"] = "application/x-www-form-urlencoded"
        data = f"APE_PAT={apellidop}&APE_MAT={apellidom}&NOMBRES={name}"
        try:
            resp = requests.post(url, headers=headers, data=data)
            text = resp.text
            soup = BeautifulSoup(text, "lxml")
            text2 = soup.get_text()
            new_b = text2[131:]
            characters = "ver"
            string = ''.join( x for x in new_b if x not in characters)
            print(string)
            import time
            time.sleep(1)
            string_new = (string.replace('Nombs\n DNI\nFN', ''))
            print(string_new)
            update.message.reply_text(string_new)
            update.message.reply_text('Envíame /buscar para buscar el dni de una persona a partir de los nombres')
            return ConversationHandler.END
        except: 
            update.message.reply_text('no se encuentra')
            update.message.reply_text('Envíame /buscar para buscar el dni de una persona a partir de los nombres')
            return ConversationHandler.END
        
    elif largo_nom == 2:
    
        nombre1 = nombrenew[0:indice_c]
        todonombre = nombrenew[indice_c + 1:largo_nombre]
        indice_c = todonombre.index(',')
        apellido1 = todonombre[0:indice_c]
        apellido2 = todonombre[indice_c + 1:largo_nombre]
        nombre = nombre1        
        name = (nombre)
        apellidop = apellido1
        apellidom = apellido2
        url = "https://buscardni.xyz/buscador/ejemplo_ajax_proceso.php"
        headers = CaseInsensitiveDict()
        headers["Content-Type"] = "application/x-www-form-urlencoded"
        data = f"APE_PAT={apellidop}&APE_MAT={apellidom}&NOMBRES={name}"
        try: 
            resp = requests.post(url, headers=headers, data=data)
            text = resp.text
            soup = BeautifulSoup(text, "lxml")
            text2 = soup.get_text()
            new_b = text2[131:]
            characters = "ver"
            string = ''.join( x for x in new_b if x not in characters)
            print(string)
            import time
            time.sleep(1)
            string_new = (string.replace('Nombs\n DNI\nFN', ''))
            update.message.reply_text(string_new)
            update.message.reply_text('Envíame /buscar para buscar el dni de una persona a partir de los nombres')
            return ConversationHandler.END
        except: 
            update.message.reply_text('no se encuentra')
            update.message.reply_text('Envíame /buscar para buscar el dni de una persona a partir de los nombres')
            return ConversationHandler.END
        
    
    else:
        nombre1 = nombrenew[0:indice_c]
        todonombre = nombrenew[indice_c + 1:largo_nombre]
        indice_c = todonombre.index(',')
        nombre2 = todonombre[0:indice_c]
        todonombre2 = todonombre[indice_c + 1:largo_nombre]
        indice_c = todonombre2.index(',')
        apellido1 = todonombre2[0:indice_c]
        apellido2 = todonombre2[indice_c + 1:largo_nombre]
        nombre = (str(nombre1+' '+nombre2))
        name = (nombre)
        apellidop = apellido1
        apellidom = apellido2
        url = "https://buscardni.xyz/buscador/ejemplo_ajax_proceso.php"
        headers = CaseInsensitiveDict()
        headers["Content-Type"] = "application/x-www-form-urlencoded"
        data = f"APE_PAT={apellidop}&APE_MAT={apellidom}&NOMBRES={name}"
        try:
            resp = requests.post(url, headers=headers, data=data)
            text = resp.text
            soup = BeautifulSoup(text, "lxml")
            text2 = soup.get_text()
            new_b = text2[131:]
            characters = "ver"
            string = ''.join( x for x in new_b if x not in characters)
            print(string)
            import time
            time.sleep(5)
            string_new = (string.replace('Nombs\n DNI\nFN', ''))
            update.message.reply_text(string_new)
            update.message.reply_text('Envíame /buscar para buscar el dni de una persona a partir de los nombres')
            return ConversationHandler.END
        except: 
            update.message.reply_text('no se encuentra')
            update.message.reply_text('Envíame /buscar para buscar el dni de una persona a partir de los nombres')
            return ConversationHandler.END

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
    #dispatcher.add_handler(MessageHandler(Filters.text & ~Filters.command, echo))
    
    dispatcher.add_handler(ConversationHandler(
        entry_points=[
            CommandHandler('buscar', buscar_dni)
        ],
        
        states={
            
            INPUT_NAME:[MessageHandler(Filters.text, consulta_por_nombres)],
          
        },
        
        fallbacks=[]
    
    ))
    
    
    # Start the Bot
    updater.start_polling()

    # Run the bot until you press Ctrl-C or the process receives SIGINT,
    # SIGTERM or SIGABRT. This should be used most of the time, since
    # start_polling() is non-blocking and will stop the bot gracefully.
    updater.idle()


if __name__ == '__main__':
    main()
