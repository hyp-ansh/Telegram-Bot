import os
import telegram
import random
from telegram import *
from telegram.ext import *
import random
import requests
import reply
import cmd
token = os.environ.get("TOKEN") or ""
bot = Bot(token)
pic = "https://telegra.ph/file/dab7aa0e02fe075f35dff.jpg"
updater = Updater(token, use_context=True)
dispatcher=updater.dispatcher
bot.set_my_commands(cmd.botcmds)
#===================/start======================
def start(update:Update,context:CallbackContext):
    chat_id = update.effective_chat.id
    message_id = update.message.message_id
    bot.sendPhoto(
        chat_id,
        pic,
        caption=f"Hi! My name is PyBot: A Python based bot.\nI was created by an accident by my master.",
        parse_mode=telegram.ParseMode.MARKDOWN,
        reply_to_message_id=message_id
    )
start_value = CommandHandler("start", start)
dispatcher.add_handler(start_value)
#===============================================

#===================/owner======================
def owner(update: Update, context: CallbackContext):
    message_id = update.message.message_id
    owner_id = "[Ø𝖘𝖍Ø](tg://user?id=1210937719)"
    bot.send_message(
        chat_id=update.effective_chat.id,
        text=f"I was made by my master **{owner_id}**",
        parse_mode=telegram.ParseMode.MARKDOWN,
        reply_to_message_id=message_id
    )
start_value = CommandHandler("owner", owner)
dispatcher.add_handler(start_value)
#================================================

#===================/gandu=======================
def gandu(update:Update,context:CallbackContext):
    message_id = update.message.message_id
    update.message.message_id
    bot.send_message(
        chat_id=update.effective_chat.id,
        text=f"`{random.choice(reply.ABUSES)}`",
        parse_mode=telegram.ParseMode.MARKDOWN,
        reply_to_message_id=message_id
    )
start_value = CommandHandler("gandu", gandu)
dispatcher.add_handler(start_value)
#================================================

#===================/slap========================
def slap(update: Update, context: CallbackContext):
    message_id = update.message.message_id
    def slapping(user_id, owner_id):
        owner_id = "[Ø𝖘𝖍Ø](tg://user?id=1210937719)"
        user = update.message.from_user
        user_id = user.id
        first_name = user.first_name
        slapped = f"[{first_name}](tg://user?id={user_id})"
        temp = random.choice(reply.SLAP)
        item = random.choice(reply.ITEMS)
        hit = random.choice(reply.HIT)
        throw = random.choice(reply.THROW)
        where = random.choice(reply.WHERE)
        return temp.format(
            user1=owner_id,
            victim=slapped,
            item=item,
            hits=hit,
            throws=throw,
            where=where,
        )
    owner_id = "[Ø𝖘𝖍Ø](tg://user?id=1210937719)"
    user = update.message.from_user
    user_id = user.id
    caption = slapping(user_id, owner_id)
    bot.send_message(
        chat_id=update.effective_chat.id,
        text=f"{caption}",
        parse_mode=telegram.ParseMode.MARKDOWN,
        reply_to_message_id=message_id
    )
start_value = CommandHandler("slap", slap)
dispatcher.add_handler(start_value)
#================================================

#=====================/beta======================
def beta(update: Update, context:CallbackContext):
    user = update.message.from_user
    chat_id=update.effective_chat.id,
    message_id = update.message.message_id
    if user.id == 1210937719:
        mention = f"[{user.first_name}](tg://user?id={user.id})"
        bot.send_message(
            chat_id,
            text=f"Hi! Master {mention}.\nThanks for making me.",
            parse_mode=telegram.ParseMode.MARKDOWN,
            reply_to_message_id=message_id,
        )
    elif user.id == 1173082794:
        mention = f"[Gandu Jeet](tg://user?id={user.id})"
        bot.send_message(
            chat_id,
            text=f"Hi beta {mention}\nGali gali me shor h jeet gandu chor h.",
            parse_mode=telegram.ParseMode.MARKDOWN,
            reply_to_message_id=message_id,
        )
    else:
        mention = f"[{user.first_name}](tg://user?id={user.id})"
        bot.send_message(
            chat_id,
            text=f"Hi! {mention}",
            parse_mode=telegram.ParseMode.MARKDOWN,
            reply_to_message_id=message_id,
        )
start_value=CommandHandler("beta", beta)
dispatcher.add_handler(start_value)
#================================================

#===================/poke========================
def poke(update:Update,context:CallbackContext):
    chat_id = update.effective_chat.id
    update.message.message_id
    message_id = update.message.message_id
    pokemon = update.message.text
    pokemon = pokemon.replace("/poke ", "")
    move = requests.get(f"https://pokeapi.co/api/v2/pokemon/{pokemon}")
    status = move.ok
    if status == True:
        rw = f"https://some-random-api.ml/pokedex?pokemon={pokemon}"
        img = requests.get(f"https://api.pokemontcg.io/v1/cards?name={pokemon}")
        lol = img.json()
        img_url = lol["cards"][0]["imageUrlHiRes"]
        r = requests.get(rw)
        a = r.json()
        name = a["name"].upper()
        typ = a["type"]
        species = a["species"]
        abilities = a["abilities"]
        height = a["height"]
        weight = a["weight"]
        esatge = r.json()["family"]["evolutionStage"]
        try:
            weaknesses = lol["cards"][0]["weaknesses"][0]["type"]
        except BaseException:
            weaknesses = None
        l = r.json()["family"]["evolutionLine"]
        # ambiguous variable name 'l' flake8(E741)
        if not l:
            line = "None"
        else:
            line = ", ".join(map(str, l))
        gen = a["generation"]
        try:
            move1 = move.json()["moves"][0]["move"]["name"]
        except IndexError:
            move1 = None
        try:
            move2 = move.json()["moves"][1]["move"]["name"]
        except IndexError:
            move2 = None
        try:
            move3 = move.json()["moves"][2]["move"]["name"]
        except IndexError:
            move3 = None
        try:
            move4 = move.json()["moves"][3]["move"]["name"]
        except IndexError:
            move4 = None
        try:
            move5 = move.json()["moves"][4]["move"]["name"]
        except IndexError:
            move5 = None
        try:
            move6 = move.json()["moves"][5]["move"]["name"]
        except IndexError:
            move6 = None
        try:
            move7 = move.json()["moves"][6]["move"]["name"]
        except IndexError:
            move7 = None
        description = a["description"]
        typ = ", ".join(map(str, typ))
        Stats = a["stats"]
        species = ", ".join(map(str, species))
        abilities = ", ".join(map(str, abilities))
        cap = f"""\n\n
**NAME** : `{name}`
**TYPE** : `{typ}`
**SPECIES** : `{species}`
**Evolution Line** : `{line}`
**Evolution Stage** : `{esatge}`
**Generation** : `{gen}`

**ABILITIES** : `{abilities}`
**WEAKNESSES** :`{weaknesses}`
**HEIGHT** : `{height}`
**WEIGHT** : `{weight}`

    **Stats**                               **Moves**
**Hp**      : `{Stats['hp']}`               `(1){move1}`
**Attack**  : `{Stats['attack']}`           `(2){move2}`
**Defense** : `{Stats['defense']}`          `(3){move3}`
**S. Att**  : `{Stats['sp_atk']}`           `(4){move4}`
**S. Def**  : `{Stats['sp_def']}`           `(5){move5}`
**Speed**   : `{Stats['speed']}`            `(6){move6}`
**Total**   : `{Stats['total']}`            `(7){move7}`

**DESCRIPTION** : `{description}`
"""
        bot.sendPhoto(
            chat_id,
            img_url,
            cap,
            parse_mode=telegram.ParseMode.MARKDOWN,
            reply_to_message_id=message_id,
        )
    
    else:
        bot.send_message(
            chat_id=chat_id,
            text="`Invalid Input`\nExample : `/poke pikachu`",
            parse_mode=telegram.ParseMode.MARKDOWN,
            reply_to_message_id=message_id,
        )
start_value = CommandHandler("poke", poke)
dispatcher.add_handler(start_value)
#===============================================

updater.start_polling()
updater.idle()

