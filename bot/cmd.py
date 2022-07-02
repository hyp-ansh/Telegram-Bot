from telegram import BotCommand as bot
# pip install -U python-telegram-bot
class _BotCommands:
    def __init__(self):
        self.owner = "owner"
        self.start = "start"
        self.gandu = "gandu"
        self.slap = "slap"
        self.poke = "poke"


info = _BotCommands()


botcmds = [
    bot(f"{info.owner}", "To get owner id"),
    bot(f"{info.start}", "Introduction of the bot"),
    bot(f"{info.gandu}", "Gali sunne ke liye"),
    bot(f"{info.slap}", "Slaps you with random objects"),
    bot(f"{info.poke}", "Gives you detail about a pokemon")
]
