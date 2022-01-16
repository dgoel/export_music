from export import paths_from_xml


def test_paths_from_xml():
    xml_data = """<?xml version="1.0" encoding="UTF-8"?>
<playlist version="1" xmlns="http://xspf.org/ns/0/">
  <trackList>
    <track>
      <location>/mnt/music/album_a/artist_a/song_a.mp3</location>
      <title>song_a</title>
      <album>album_a</album>
      <duration>267000</duration>
      <image>/mnt/music/album_a/artist_a/song_a.jpg</image>
    </track>
    <track>
      <location>/mnt/music/album_b/artist_b/song_b.mp3</location>
      <title>song_b</title>
      <album>album_b</album>
      <duration>358000</duration>
      <image>/mnt/music/album_b/artist_b/song_b.jpg</image>
    </track>
  </trackList>
</playlist>"""

    parsed_paths = paths_from_xml(xml_data)
    assert len(parsed_paths) == 2
    assert parsed_paths[0] == "/mnt/music/album_a/artist_a/song_a.mp3"
    assert parsed_paths[1] == "/mnt/music/album_b/artist_b/song_b.mp3"
