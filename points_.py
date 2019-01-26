def bat(runs,balls,fours,sixes,field):
    points = runs / 2
    if runs > 50 and runs < 100:
        points += 5
    if runs > 100:
        points += 10
    points += fours
    points += (2 * sixes)
    points += (10 * field)
    strikerate = runs / balls
    strikerate *= 100
    strikerate = int ( strikerate )
    if strikerate > 80 and strikerate < 100:
        points += 2
    if strikerate > 100:
        points += 4
    return points


def bowl(wickets,overs,runs,field):
    points = (10 * wickets)
    if wickets >= 3 and wickets < 5:
        points += 3
    if wickets >= 5:
        points += 10
    points += (10 * field)

    economy_rate = runs / overs
    if economy_rate > 3.5 and economy_rate <= 4.5:
        points += 4
    if economy_rate > 2 and economy_rate <= 3.5:
        points += 7
    if economy_rate < 2:
        points += 10
    return points

