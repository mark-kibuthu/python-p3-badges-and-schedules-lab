def badge_maker(name):
    return f"Hello, my name is {name}."

def batch_badge_creator(names):
    return [badge_maker(name) for name in names]

def assign_rooms(speakers):
    return [f"Hello, {speaker}! You'll be assigned to room {index + 1}!" for index, speaker in enumerate(speakers)]

def printer(speakers):
    for badge in batch_badge_creator(speakers):
        print(badge)
    for room_assignment in assign_rooms(speakers):
        print(room_assignment)
