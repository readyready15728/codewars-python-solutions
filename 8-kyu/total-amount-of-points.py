def points(games):
    total = 0

    for game in games:
        x, y = [int(x) for x in game.split(':')]
        
        if x > y:
            total += 3
        elif x == y:
            total += 1
    
    return total
