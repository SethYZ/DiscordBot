import discord


def read_token():
    with open("token.txt", "r") as file:
        lines = file.readlines()
        return lines[0].strip()


token = read_token()

client = discord.Client()
client.run(token)
