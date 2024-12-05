import data
from typing import Optional


# Write your functions for each part in the space below.

# Part 1
def create_rectangle(p1: data.Point, p2: data.Point)-> data.Rectangle:
    top_left_x = min(p1.x, p2.x)
    top_left_y = max(p1.y, p2.y)
    bottom_right_x = max(p1.x, p2.x)
    bottom_right_y = min(p1.y, p2.y)
    top_left = data.Point(top_left_x, top_left_y)
    bottom_right = data.Point(bottom_right_x, bottom_right_y)
    return data.Rectangle(top_left, bottom_right)

# Part 2
def shorter_duration_than(duration1: str, duration2: str) -> bool:
    duration1_total_seconds = duration1.hours * 3600 + duration1.minutes * 60 + duration1.seconds
    duration2_total_seconds = duration2.hours * 3600 + duration2.minutes * 60 + duration2.seconds
    return duration1_total_seconds < duration2_total_seconds

# Part 3
def duration_in_seconds(duration: data.Duration) -> int:
    return duration.minutes * 60 + duration.seconds


def song_shorter_than(songs: list[data.Song], upper_bound: data.Duration) -> list[data.Song]:
    upper_bound_seconds = duration_in_seconds(upper_bound)
    return [song for song in songs if duration_in_seconds(song.duration) < upper_bound_seconds]

# Part 4
def running_time(songs: list[data.Song], playlist: list[int]) -> data.Duration:
    total_seconds = 0
    for song_index in playlist:
        if 0 <= song_index < len(songs):
            total_seconds += duration_in_seconds(songs[song_index].duration)
    total_minutes = total_seconds // 60
    remaining_seconds = total_seconds % 60
    return data.Duration(total_minutes, remaining_seconds)


# Part 5
def validate_route(city_links: list[list[str]], route: list[str]) -> bool:
    for i in range(len(route) - 1):
        city_pair1 = [route[i], route[i + 1]]
        city_pair2 = [route[i + 1], route[i]]
        if city_pair1 not in city_links and city_pair2 not in city_links:
            return False
    return True

# Part 6
def longest_repetition(numbers: list[int]) -> [int]:
    if not numbers:
        return None
    max_length = 1
    max_start_index = 0
    current_length = 1
    current_start_index = 0
    for i in range(1, len(numbers)):
        if numbers[i] == numbers[i - 1]:
            current_length += 1
        else:
            if current_length > max_length:
                max_length = current_length
                max_start_index = current_start_index
            current_length = 1
            current_start_index = i
    if current_length > max_length:
        max_start_index = current_start_index
    return max_start_index
