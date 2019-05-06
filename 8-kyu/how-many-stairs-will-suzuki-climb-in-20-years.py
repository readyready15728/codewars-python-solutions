def stairs_in_20(stairs):
    return 20 * sum(sum(weekday) for weekday in stairs)
