def runoff(voters):
    print (voters)
    candidate = {}
    for voter in voters:

        if voter[0] not in candidate:
            candidate[voter[0]] = 1
        else:
            candidate[voter[0]] += 1
        index = 1
        while index < len(voter):
            if voter[index] not in candidate:
                candidate[voter[index]] = 0
            index += 1

    for i in candidate:
        if 100 * candidate[i] / (len(voters)) > 50:
            return (i)

    minor = []
    for i in candidate:
        if minor == []:
            minor.append(i)
        elif i not in minor:
            if candidate[minor[0]] > candidate[i]:
                minor = [i]
            elif candidate[minor[0]] == candidate[i]:
                minor.append(i)

    numofminorvotest = sum([ candidate[i] for i in minor])
    print (numofminorvotest)
    if numofminorvotest == len(voters):
        return None
    else:
        for voter in voters:
            index = len(voter) - 1
            while index >= 0:
                if voter[index] in minor:
                    del voter[index]
                index -=1

    return runoff(voters)

samples = [[["dem", "ind", "rep"],
            ["rep", "ind", "dem"],
            ["ind", "dem", "rep"],
            ["ind", "rep", "dem"]],
           [["a", "c", "d", "e", "b"],
            ["e", "b", "d", "c", "a"],
            ["d", "e", "c", "a", "b"],
            ["c", "e", "d", "b", "a"],
            ["b", "e", "a", "c", "d"]],
           [['e', 'c', 'a', 'b', 'd'],
            ['e', 'a', 'b', 'd', 'c'],
            ['d', 'b', 'e', 'c', 'a'],
            ['a', 'c', 'e', 'b', 'd'],
            ['e', 'd', 'a', 'c', 'b']],
           [['a', 'c', 'b', 'd', 'e'],
            ['d', 'c', 'a', 'b', 'e'],
            ['e', 'b', 'd', 'a', 'c'],
            ['e', 'a', 'b', 'c', 'd'],
            ['b', 'c', 'e', 'a', 'd']],
           [['Reinhard von Musel', 'Daisuke Aramaki', 'Frank Underwood', 'Brian J. Mason', 'Gihren Zabi',
             'Abelt Dessler'],
            ['Brian J. Mason', 'Frank Underwood', 'Abelt Dessler', 'Daisuke Aramaki', 'Gihren Zabi',
                                'Reinhard von Musel'],
            ['Reinhard von Musel', 'Abelt Dessler', 'Gihren Zabi', 'Brian J. Mason', 'Daisuke Aramaki',
             'Frank Underwood'],
            ['Frank Underwood', 'Brian J. Mason', 'Abelt Dessler', 'Gihren Zabi', 'Daisuke Aramaki',
             'Reinhard von Musel'],
            ['Daisuke Aramaki', 'Abelt Dessler', 'Reinhard von Musel', 'Gihren Zabi', 'Frank Underwood',
             'Brian J. Mason']],
           [['Frank Underwood', 'Gihren Zabi', 'Abelt Dessler', 'Drake Luft', 'Reinhard von Musel', 'Brian J. Mason'],
            ['Abelt Dessler', 'Brian J. Mason', 'Drake Luft', 'Reinhard von Musel', 'Gihren Zabi','Frank Underwood'],
            ['Abelt Dessler', 'Brian J. Mason', 'Drake Luft', 'Frank Underwood', 'Gihren Zabi','Reinhard von Musel'],
            ['Drake Luft', 'Gihren Zabi', 'Reinhard von Musel', 'Abelt Dessler', 'Frank Underwood', 'Brian J. Mason']],
           [['Frank Underwood', 'Gihren Zabi', 'Abelt Dessler', 'Drake Luft', 'Reinhard von Musel', 'Brian J. Mason'],
            ['Abelt Dessler', 'Brian J. Mason', 'Drake Luft', 'Reinhard von Musel', 'Gihren Zabi','Frank Underwood'],
            ['Abelt Dessler', 'Brian J. Mason', 'Drake Luft', 'Frank Underwood', 'Gihren Zabi','Reinhard von Musel'],
            ['Drake Luft', 'Gihren Zabi', 'Reinhard von Musel','Abelt Dessler', 'Frank Underwood', 'Brian J. Mason']]]

#x = runoff(voters)
#print (x)
for voters in samples:
    print (runoff(voters))



