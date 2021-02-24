import os
import random
import discord
from dotenv import load_dotenv
from file import*
from translations import*
from conversationnel import*
from nltk.chat.util import Chat, reflections
import datetime
import pytz
import pymongo



client = pymongo.MongoClient("mongodb+srv://africa:africa2021@bot.cb1sv.mongodb.net/NougatBD2?retryWrites=true&w=majority")
mydb = client["NougatBD2"]

mycolFD_score = mydb["Feedbac_S"]
mycolFD_Improvement = mydb["Feedbac_I"]


load_dotenv(dotenv_path="config")
TOKEN = os.getenv("TOKEN")

client = discord.Client()
chat = Chat(pairs, reflections)


message_acceuil = ''' ```-------------------------- Englih ---------------------------
Hello, Im NougatBOT,  
I was created by AfrIcA agency to make a basic conversation with you,  
I can give you answers for your questions (Astronomy, Bioinformatic, Datascience) 

-------------------------- Francais ---------------------------
Bonjour, Je suis NougatBot,
Je suis crée par l'agence AfrIcA pour vous aider à trouver des réponses à vos questions dans les domaines de l'Astronomie, la Bioinformatique et la Science des données.
 
---------------------------  عربي -----------------------------
مرحبا ، إسمي نوڨابوت
.تمت برمجتي من قبل مؤسسة أفريكا لمساعدتكم على إيجاد إجابات  لأسئلتك في مجالات علم الفلك والمعلوماتية الحيوية وعلوم البيانات.
```  '''


#!sat  to enter your satisfaction_score
    #!imp  to give some improvement
    #!name
    #!date



dic={}
limit = 5


@client.event
async def on_ready():
   
    chanel = client.get_channel(809014144941817876)
    await chanel.send(message_acceuil)
    print(f'{client.user.name} has connected to Discord!')
    
  
@client.event
async def on_message(message):
    
    chanel = client.get_channel(809014144941817876)

    cmd = ''
    lang = 'en'

    if message.content == 'raise-exception':
        raise discord.DiscordException
    
    
    if message.author == client.user:
        return


    elif message.content.startswith('!'):
        cmd = message.content.split()[0]
        print('cmd = ', cmd)

        
    if cmd != '':
        
        def is_command (msg): # Checking if the message is a command call
            if len(msg.content.split()) < 2:
                return False
            else : 
                 
                key_ = msg.content.split()[0]    # key_ can be : '!score', '!improvement'..
                value = msg.content.replace(key_, '').strip()
                key= key_[1:]
                
                if(key != 'date'):
                    dic= { 'user' :message.author.name,
                           'date' : datetime.datetime.now(pytz.timezone('Europe/Paris')).strftime('%Y-%m-%d - %H:%M:%S '),
                           'langue' : lang,
                            key :value }
                    print(dic.items())
                    
                if(key == 'score'): mydb.mycolFD_score.insert(dic)
                if(key == 'improvement'): mydb.mycolFD_Improvement.insert(dic)

                return key

                # control user 
                # langue
                # automated_id
                # {association du score + msg_improvement
                # ajout de la date}


        key =  is_command(message)     
        if(key == False) : await chanel.send('sorry, it seems like you missed so ! !')
        if(key == 'score'):  await chanel.send('score well received, thanks !')
        if(key == 'improvement'): await chanel.send('improvement well received, thanks !')
        if(key == 'date') : 
            await chanel.send('the date&hour now are :')
            await chanel.send(datetime.datetime.now(pytz.timezone('Europe/Paris')).strftime('%Y-%m-%d - %H:%M:%S  '))
    else: 
        lang = language_detection(message.content)
        eng_msg = translate_input(message.content)
        rabbit = chat.respond(eng_msg.lower())
        
        if rabbit:
            if(rabbit == 'Hello' or  rabbit == 'Hey there'): 
                rabbit += ' ' + message.author.name
            await chanel.send(convert_to_detected_language(rabbit, lang))
        
        else: 
            #check if we have this question-response in our collections
            id,y_col = resarchQuestion(eng_msg)
            if (id):
                reponse = get_response(id,y_col)
                #print(reponse)
                if (len(reponse)>1500) :
                    reponse_f = reponse[0:1500]
                    reponse_f += '...'
                    
                else : reponse_f = reponse

                if (lang != 'en'): 
                    reponse_ff = convert_to_detected_language(reponse_f,lang)
                else : 
                    reponse_ff = reponse_f
                await chanel.send(reponse_ff)
                await chanel.send(reponse_ff)
            else: 
                txt = "please specify me your question "
                if (lang != 'en'):  
                    txt2 = convert_to_detected_language(txt,lang)
                else : txt2 = txt
                await chanel.send(txt2)

client.run(TOKEN)