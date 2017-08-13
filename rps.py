import random
from sopel.module import rule

@rule(r'(RPS|rps) $nickname[ ]?[\?]?[ \t]*$')
def rps(bot, trigger):
    choice = random.choice(('ROCK', 'PAPER', 'SCISSORS'))
    punctuation = random.choice(('', '!'))
    bot.say(choice + ' ' + trigger.nick + punctuation)
