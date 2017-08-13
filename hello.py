import sopel.module
from sopel.formatting import *

@sopel.module.commands('hello')
def helloworld(bot, trigger):
    bot.say(color("Greetings earthling!", colors.RED))
