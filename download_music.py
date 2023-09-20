from sclib.asyncio import SoundcloudAPI, Track, Playlist


api = SoundcloudAPI()
playlist_names = ["jukebox-samples-coherence","jukebox-samples-novel-lyrics","jukebox-samples-musicality","timeline-january","jukebox-samples-novel-riffs","jukebox-samples-novel-lyrics","jukebox-samples-novel-styles", "jukebox-samples-novel-voice","jukebox-samples-full-tree","musenet","jukebox-samples-novel","jukebox-samples-re-renditions", "jukebox-selected-early","timeline","timeline-october","timeline-august","jukebox"]
for playlist_name in playlist_names:

  playlist = await api.resolve('https://soundcloud.com/openai_audio/sets/' + playlist_name )

  assert type(playlist) is Playlist

  for track in playlist.tracks:
      file_path = "/content/drive/MyDrive/AI_music/AI Music Data/"
      filename = f'{track.artist} - {track.title}.mp3'.replace('/','-')
      with open(file_path + filename, 'wb+') as file:
          await track.write_mp3_to(file)



api = SoundcloudAPI()
playlist = await api.resolve('https://soundcloud.com/user-133591428/sets/frank-sinatra')

assert type(playlist) is Playlist

for track in playlist.tracks:
    filename = f'./{track.artist} - {track.title}.mp3'
    with open(filename, 'wb+') as file:
      file_path = "/content/drive/MyDrive/AI_music/Real Music Data/"
      filename = f'{track.artist} - {track.title}.mp3'.replace('/','-')
      with open(file_path + filename, 'wb+') as file:
          await track.write_mp3_to(file)

playlist = await api.resolve('https://soundcloud.com/eslam-zidan-yo/sets/joe-bonamassa')

assert type(playlist) is Playlist

for track in playlist.tracks:
    filename = f'./{track.artist} - {track.title}.mp3'
    with open(filename, 'wb+') as file:
      file_path = "/content/drive/MyDrive/AI_music/Real Music Data/"
      filename = f'{track.artist} - {track.title}.mp3'.replace('/','-')
      with open(file_path + filename, 'wb+') as file:
          await track.write_mp3_to(file)

playlist = await api.resolve('https://soundcloud.com/user-437851905/sets/the-best-of-alan-jackson')

assert type(playlist) is Playlist

for track in playlist.tracks:
    filename = f'./{track.artist} - {track.title}.mp3'
    with open(filename, 'wb+') as file:
      file_path = "/content/drive/MyDrive/AI_music/Real Music Data/"
      filename = f'{track.artist} - {track.title}.mp3'.replace('/','-')
      with open(file_path + filename, 'wb+') as file:
          await track.write_mp3_to(file)

playlist = await api.resolve('https://soundcloud.com/d-ndar-deniz-g-kta/sets/ella-fitzgerald')

assert type(playlist) is Playlist

for track in playlist.tracks:
    filename = f'./{track.artist} - {track.title}.mp3'
    with open(filename, 'wb+') as file:
      file_path = "/content/drive/MyDrive/AI_music/Real Music Data/"
      filename = f'{track.artist} - {track.title}.mp3'.replace('/','-')
      with open(file_path + filename, 'wb+') as file:
          await track.write_mp3_to(file)

playlist = await api.resolve('https://soundcloud.com/user-442050681-623389884/sets/let-it-be-the-beatles')

assert type(playlist) is Playlist

for track in playlist.tracks:
    filename = f'./{track.artist} - {track.title}.mp3'
    with open(filename, 'wb+') as file:
      file_path = "/content/drive/MyDrive/AI_music/Real Music Data/"
      filename = f'{track.artist} - {track.title}.mp3'.replace('/','-')
      with open(file_path + filename, 'wb+') as file:
          await track.write_mp3_to(file)


