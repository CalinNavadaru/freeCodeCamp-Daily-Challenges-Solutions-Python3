def favorite_songs(playlist: list[dict]) -> list[str]:
    max1_plays = playlist[0]["plays"]
    max1_index = 0
    max2_plays = -1
    max2_index = -1

    for i in range(1, len(playlist)):
        song = playlist[i]
        if song["plays"] > max1_plays:
            max2_plays = max1_plays
            max2_index = max1_index
            max1_plays = song["plays"]
            max1_index = i

        elif song["plays"] > max2_plays:
            max2_plays = song["plays"]
            max2_index = i
    return [playlist[max1_index]["title"], playlist[max2_index]["title"]]
