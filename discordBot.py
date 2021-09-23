from discord.ext import commands
from mymongo import MyMongo
from myartist import MyArtist

client = commands.Bot(command_prefix="/")
mymongo = MyMongo(client_string="")


def validate_input_for_addartist(i):
    if all([isinstance(word, str) for word in i.split(" ")]):
        return True
    return False


@client.command()
async def addartist(ctx, *, i):
    if not validate_input_for_addartist(i):
        await ctx.send("Input: {Artist Name}")
    elif mymongo.check_if_key_exists("genius", "lyricsByArtist", "artist", i):
        await ctx.send("Artist exists in DB")
    else:
        myartist = MyArtist(artist=i, max_songs=50)
        myartist.populate_lyrics_for_artist()
        mymongo.insert_values_under_key("genius", "lyricsByArtist", "lyric", myartist.lyrics_for_artist, "artist", i)
        await ctx.send("Here we go! " + str(i) + " Added!")


@client.command()
async def getlyric(ctx, *, i):
    l = mymongo.get_random_doc("genius", "lyricsByArtist", "artist", str(i),"lyric")
    if l:
        await ctx.send(str(l[0]))
    else:
        await ctx.send(str(i) + " not in DB! Use /addartist {Artist Name}")


@client.event
async def on_ready():
    print("Bot is ready")


client.run("")
