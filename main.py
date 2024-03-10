import discord
import random
import yaml

intents = discord.Intents.all()
intents.message_content = True
client = discord.Client(intents=intents)

questions = []

with open('quests.yml', 'r', encoding='utf-8') as f:
    data = yaml.safe_load(f)
    for question in data:
        questions.append(question)

awaiting_answer = False
current_question = None

@client.event
async def on_message(message):
    global awaiting_answer
    global current_question

    if message.author == client.user:
        return

    if message.content.startswith('/start'):
        awaiting_answer = True
        current_question = random.choice(questions)
        await message.channel.send(current_question['text'])

    elif message.content.startswith('/answer'):
        if awaiting_answer:
            # Get user's answer
            answer = message.content.split(' ')[1]
            if answer.lower() == current_question['answer'].lower():
                await message.channel.send('Правильно!')
            else:
                await message.channel.send('Неправильно! Ответ: ' + current_question['answer'])
            awaiting_answer = False
            current_question = None

client.run('MTIwNTk3NTcyNjE1MTU2OTQzOQ.GnqXpX.wXPjCRrdbuw0SHC1Uc6j0tT8XCV6qO1AxPpgoE')
