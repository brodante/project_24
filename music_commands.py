import discord
from discord.ext import commands

bot=commands.Bot(command_prefix="!",intents=discord.Intents.all())
# Define a play function to encapsulate the play logic
async def play(ctx, source):
    """Plays audio from a source (a link or an upload)"""

    # Create an FFmpeg PCMAudio object from the source input
    ffmpeg_options = {'options': '-vn'}
    player = ctx.voice_client
    if not player:
        player = await ctx.author.voice.channel.connect()

    if type(source) is str:
        # If the user is giving an URL
        if "spotify" in source:
            # If the user is giving a spotify song/album/playlist link
            song = await player.create_ytdl_player(source, ytdl_options=ffmpeg_options, stream=True)
        else:
            # If the user is giving a youtube link
            song = await player.create_ytdl_player(source, stream=True, ytdl_options=ffmpeg_options)
    else:
        # If the user is uploading a file
        song = await player.create_ffmpeg_player(source, ffmpeg_options=ffmpeg_options)

    # Add the song to the queue
    player.queue.append(song)

    # If the player was not playing anything, start the song
    if not player.is_playing():
        await player.play()
@bot.command(name="play", aliases=["p"])
async def play_(ctx, *, source: str):
    """Plays audio from a source (a link or an upload)"""
    async def play(ctx, source):
        """Plays audio from a source (a link or an upload)"""

        # Create an FFmpeg PCMAudio object from the source input
        ffmpeg_options = {'options': '-vn'}
        player = ctx.voice_client
        if not player:
            player = await ctx.author.voice.channel.connect()

        if type(source) is str:
            # If the user is giving an URL
            if "spotify" in source:
                # If the user is giving a spotify song/album/playlist link
                song = await discord.FFmpegOpusAudio.from_probe(source, **ffmpeg_options, executable='ffmpeg')
            else:
                # If the user is giving a youtube link
                song = await discord.FFmpegOpusAudio.from_probe(source, **ffmpeg_options, executable='ffmpeg')
        else:
            # If the user is uploading a file
            song = await discord.FFmpegOpusAudio.from_probe(source, **ffmpeg_options, executable='ffmpeg')

        # Add the song to the queue
        player.queue.append(song)

        # If the player was not playing anything, start the song
        if not player.is_playing():
            await player.play()

    await play(ctx, source)


@bot.command(name="queue", aliases=["q"])
async def queue_(ctx):
    """Shows the player's queue"""
    player = ctx.voice_client
    if not player:
        return await ctx.send("The player is not connected to a voice channel.")

    # Embed the current song and the upcoming songs in a nice format
    embed = discord.Embed(title="Queue", color=discord.Color.green())
    if player.is_playing():
        embed.add_field(name="Currently playing", value=f"`{player.current.title}`", inline=False)
    else:
        embed.add_field(name="Currently playing", value="No music currently playing.", inline=False)

    embed.add_field(name="Upcoming songs", value="\n".join(f"`{song.title}`" for song in player.queue))

    # Send the embed
    await ctx.send(embed=embed)

@bot.command(name="skip", aliases=["s"])
async def skip_(ctx):
    """Skips the currently playing song"""
    player = ctx.voice_client
    if not player:
        return await ctx.send("The player is not connected to a voice channel.")

    player.stop()
    await ctx.send("Skipped the currently playing song.")

@bot.command(name="pause", aliases=["pa"])
async def pause_(ctx):
    """Pauses the currently playing song"""
    player = ctx.voice_client
    if not player:
        return await ctx.send("The player is not connected to a voice channel.")

    player.pause()
    await ctx.send("Paused the currently playing song.")

@bot.command(name="resume", aliases=["re"])
async def resume_(ctx):
    """Resumes the currently playing song"""
    player = ctx.voice_client
    if not player:
        return await ctx.send("The player is not connected to a voice channel.")

    player.resume()
    await ctx.send("Resumed the currently playing song.")

@bot.command(name="disconnect", aliases=["dc"])
async def disconnect_(ctx):
    """Disconnects the bot from the voice channel"""
    player = ctx.voice_client
    if not player:
        return await ctx.send("The player is not connected to a voice channel.")

    await player.disconnect()
    await ctx.send("Disconnected the bot from the voice channel.")
