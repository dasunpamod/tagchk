import telebot
token = '1743761492:AAHLdJEFjEsWV5A_vOYKRwnUi6f3_6tv5cY'
bot = telebot.TeleBot(token)
def chk(f_name,l_name,message,chat_id,user_id):
    if '⫷[ʘϾḂ]⫸' in f_name:
          a=1
    elif '⫷[ʘϾḂ]⫸' in l_name:
           a=1
    elif 'Group' in f_name:
           a=1
    elif 'Malshi' in l_name:
           a=1
    else:
          a=0
          print (f_name,l_name)
    if a == 0 :
         bot.reply_to(message, mutetxt)
         bot.restrict_chat_member(chat_id,user_id)
         print (user_id,"Has Been Muted")

mutetxt = "You have been muted.Please Put the ⫷[ʘϾḂ]⫸ in your name,and contact a admin (https://t.me/c/1448155875/33) to unmute. see rules http://t.me/c/1448155875/1089"
strtp = "This can Only be used In OCB Groups / Solely Created By @Hankur"
# handle commands, /start
@bot.message_handler(commands=['start'])
def handle_command(message):
    bot.reply_to(message, "Hello, welcome to OCB TAG Detector Bot! By hankur")
    

@bot.message_handler(func=lambda message: True)
def handle_all_message(message):
    f_name = message.from_user.first_name
    l_name = str(message.from_user.last_name)
    user_id = message.from_user.id
    chat_id = message.chat.id
    print (f_name,"got",l_name,chat_id,user_id) # jst fr testi
    status = bot.get_chat_member(chat_id, user_id).status
    print (status)
    if message.chat.type == "private":
       bot.reply_to(message,strtp)
       if '⫷[ʘϾḂ]⫸' in f_name:
          a=1
         elif '⫷[ʘϾḂ]⫸' in l_name:
           a=1
      elif 'Group' in f_name:
           a=1
      elif 'Malshi' in l_name:
           a=1
      else:
          a=0
          print (f_name,l_name)
      if a == 0 :
         bot.reply_to(message, "Please add ⫷[ʘϾḂ]⫸ to ur user name in order to join ocb groups")
    else:
      if status=='member':
          chk(f_name,l_name,message,chat_id,user_id)
bot.polling()


#solely Created By Hankur

