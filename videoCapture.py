import ffmpeg
name = input("What is your video name?")
stream = ffmpeg.input(name)
stream = ffmpeg.hflip(stream)
stream = ffmpeg.output(stream, 'name.wav')
ffmpeg.run(stream)

