file = open("input.txt")
# ans = open("09.a")
# arr = []
# while ans:
#     n = ans.readline()
#     if not n:
#         break
#     arr.append(float(n))
# for i in arr:
#     print(i)
# print("len =", len(arr))
# input()


teams = {}
players = {}
# arr1 = []
# q = 0
while True:
    line = file.readline()
    if not line:
        break
    if line[0] == '\"':
        team1 = ""
        team2 = ""
        i = 1
        while line[i] != '\"':
            team1 += line[i]
            i += 1
        i += 1
        while line[i] != '\"':
            i += 1
        i += 1
        while line[i] != '\"':
            team2 += line[i]
            i += 1
        i += 1
        while line[i] == ' ':
            i += 1
        goals1 = ""
        goals2 = ""
        while line[i] != ':':
            goals1 += line[i]
            i += 1
        i += 1
        while (i < len(line)) and (line[i] != ' '):
            goals2 += line[i]
            i += 1
        team_goals1 = []
        team_goals2 = []
        for j in range(int(goals1)):
            line = file.readline()
            i = 0
            player = ""
            while (i < len(line)) and (line[i] == ' '):
                i += 1
            while (i < len(line)) and (line[i] not in "0123456789"):
                player += line[i]
                i += 1
            if player[len(player) - 1] == ' ':
                player = player[:-1]
            while (i < len(line)) and (line[i] == ' '):
                i += 1
            minute = ""
            while (i < len(line)) and (line[i] != '\''):
                minute += line[i]
                i += 1
            team_goals1.append([int(minute), player])
        for j in range(int(goals2)):
            line = file.readline()
            i = 0
            player = ""
            while (i < len(line)) and (line[i] == ' '):
                i += 1
            while (i < len(line)) and (line[i] not in "0123456789"):
                player += line[i]
                i += 1
            if player[len(player) - 1] == ' ':
                player = player[:-1]
            while (i < len(line)) and (line[i] == ' '):
                i += 1
            minute = ""
            while (i < len(line)) and (line[i] != '\''):
                minute += line[i]
                i += 1
            team_goals2.append([int(minute), player])

        if teams.get(team1) is None:
            teams[team1] = [1, int(goals1), int(goals1), 0, set()]
        else:
            teams[team1][0] += 1
            teams[team1][1] += int(goals1)
            teams[team1][2] = teams[team1][1] / teams[team1][0]

        if teams.get(team2) is None:
            teams[team2] = [1, int(goals2), int(goals2), 0, set()]
        else:
            teams[team2][0] += 1
            teams[team2][1] += int(goals2)
            teams[team2][2] = teams[team2][1] / teams[team2][0]

        for goal in team_goals1:
            teams[team1][4].add(goal[1])
            if players.get(goal[1]) is None:
                players[goal[1]] = [0, 0, 0, 0, {}]
        for goal in team_goals2:
            teams[team2][4].add(goal[1])
            if players.get(goal[1]) is None:
                players[goal[1]] = [0, 0, 0, 0, {}]

        for player in teams[team1][4]:
            players[player][0] += 1
            # players[player][2] = players[player][1] / players[player][0]
            players[player][2] = players[player][1] / teams[team1][0]
        for player in teams[team2][4]:
            players[player][0] += 1
            # players[player][2] = players[player][1] / players[player][0]
            players[player][2] = players[player][1] / teams[team2][0]

        # s_players = set()
        # for goal in team_goals2:
        #     if goal[1] not in s_players:
        #         if players.get(goal[1]) is None:
        #             players[goal[1]] = [1, 0, 0, 0, {}]
        #         else:
        #             players[goal[1]][0] += 1
        #     s_players.add(goal[1])

        for goal in team_goals1:
            players[goal[1]][1] += 1
            # players[goal[1]][2] = players[goal[1]][1] / players[goal[1]][0]
            players[goal[1]][2] = players[goal[1]][1] / teams[team1][0]
            if players[goal[1]][4].get(goal[0]) is None:
                players[goal[1]][4][goal[0]] = 1
            else:
                players[goal[1]][4][goal[0]] += 1

        for goal in team_goals2:
            players[goal[1]][1] += 1
            # players[goal[1]][2] = players[goal[1]][1] / players[goal[1]][0]
            players[goal[1]][2] = players[goal[1]][1] / teams[team2][0]
            if players[goal[1]][4].get(goal[0]) is None:
                players[goal[1]][4][goal[0]] = 1
            else:
                players[goal[1]][4][goal[0]] += 1

        team_goals1.sort()
        team_goals2.sort()
        if (int(goals1) > 0) and (int(goals2) > 0):
            if team_goals1[0][0] < team_goals2[0][0]:
                teams[team1][3] += 1
                players[team_goals1[0][1]][3] += 1
            else:
                teams[team2][3] += 1
                players[team_goals2[0][1]][3] += 1
        elif int(goals1) > 0:
            teams[team1][3] += 1
            players[team_goals1[0][1]][3] += 1
        elif int(goals2) > 0:
            teams[team2][3] += 1
            players[team_goals2[0][1]][3] += 1
        # print(teams)
        # print(players)
        # input()
    elif "Total goals for" in line:
        # q += 1
        # print(q, end='\t')
        i = 0
        while line[i] != '\"':
            i += 1
        i += 1
        team = ""
        while line[i] != '\"':
            team += line[i]
            i += 1
        if teams.get(team) is not None:
            print(teams[team][1])
            # arr1.append(teams[team][1])
        else:
            print(0)
            # arr1.append(0)
    elif "Mean goals per game for" in line:
        # q += 1
        # print(q, end='\t')
        i = 0
        while line[i] != '\"':
            i += 1
        i += 1
        team = ""
        while line[i] != '\"':
            team += line[i]
            i += 1
        # print('\'' + team + '\'')
        if teams.get(team) is not None:
            print(teams[team][2])
            # arr1.append(teams[team][2])
        else:
            print(0)
            # arr1.append(0)
    elif "Total goals by" in line:
        # q += 1
        # print(q, end='\t')
        i = 0
        while line[i] != 'y':
            i += 1
        i += 1
        while line[i] == ' ':
            i += 1
        player = ""
        # while (i < len(line)) and (line[i] != ' '):
        while (i < len(line)) and (line[i] != '\n'):
            player += line[i]
            i += 1
        # print('\'' + player + '\'')

        if players.get(player) is not None:
            print(players[player][1])
            # arr1.append(players[player][1])
        else:
            print(0)
            # arr1.append(0)
    elif "Mean goals per game by" in line:
        # q += 1
        # print(q, end='\t')
        i = 0
        while line[i] != 'y':
            i += 1
        i += 1
        while line[i] == ' ':
            i += 1
        player = ""
        while (i < len(line)) and (line[i] != '\n'):
            player += line[i]
            i += 1
        # print('\'' + player + '\'', players[player])
        # print(players)
        if players.get(player) is not None:
            print(players[player][2])
            # arr1.append(players[player][2])
        else:
            print(0)
            # arr1.append(0)
    elif "Goals on minute" in line:
        # q += 1
        # print(q, end='\t')
        i = 0
        while line[i] not in "0123456789":
            i += 1
        minute = ""
        while (i < len(line)) and (line[i] != '\n') and (line[i] in "0123456789"):
            minute += line[i]
            i += 1

        while line[i] != 'y':
            i += 1
        i += 1
        while line[i] == ' ':
            i += 1
        player = ""
        while (i < len(line)) and (line[i] != '\n'):
            player += line[i]
            i += 1
        if (players.get(player) is not None) and (players[player][4].get(int(minute)) is not None):
            print(players[player][4][int(minute)])
            # arr1.append(players[player][4][int(minute)])
        else:
            print(0)
            # arr1.append(0)
    elif "Goals on first" in line:
        # q += 1
        # print(q, end='\t')
        i = 0
        while line[i] not in "0123456789":
            i += 1
        minute = ""
        while (i < len(line)) and (line[i] != '\n') and (line[i] in "0123456789"):
            minute += line[i]
            i += 1

        while line[i] != 'y':
            i += 1
        i += 1
        while line[i] == ' ':
            i += 1
        player = ""
        while (i < len(line)) and (line[i] != '\n'):
            player += line[i]
            i += 1

        if players.get(player) is not None:
            cnt = 0
            for mnt, num in players[player][4].items():
                if mnt <= int(minute):
                    cnt += num
            print(cnt)
            # arr1.append(cnt)
        else:
            print(0)
            # arr1.append(0)
    elif "Goals on last" in line:
        # q += 1
        # print(q, end='\t')
        i = 0
        while line[i] not in "0123456789":
            i += 1
        minute = ""
        while (i < len(line)) and (line[i] != '\n') and (line[i] in "0123456789"):
            minute += line[i]
            i += 1

        while line[i] != 'y':
            i += 1
        i += 1
        while line[i] == ' ':
            i += 1
        player = ""
        while (i < len(line)) and (line[i] != '\n'):
            player += line[i]
            i += 1
        # print(player, minute)
        if players.get(player) is not None:
            cnt = 0
            for mnt, num in players[player][4].items():
                if mnt >= 91 - int(minute):
                    cnt += num
            print(cnt)
            # arr1.append(cnt)
        else:
            print(0)
            # arr1.append(0)
    elif "Score opens by \"" in line:
        # q += 1
        # print(q, end='\t')
        i = 0
        while line[i] != '\"':
            i += 1
        i += 1
        team = ""
        while line[i] != '\"':
            team += line[i]
            i += 1
        if teams.get(team) is not None:
            print(teams[team][3])
            # arr1.append(teams[team][3])
        else:
            print(0)
            # arr1.append(0)
    elif "Score opens by" in line:
        # q += 1
        # print(q, end='\t')
        i = 0
        while line[i] != 'y':
            i += 1
        i += 1
        while line[i] == ' ':
            i += 1
        player = ""
        while (i < len(line)) and (line[i] != '\n'):
            player += line[i]
            i += 1
        if players.get(player) is not None:
            print(players[player][3])
            # arr1.append(players[player][3])
        else:
            print(0)
            # arr1.append(0)

# input()
# for i in range(len(arr1)):
#     print(arr1[i], end=' ')
#     if arr1[i] != arr[i]:
#         print("false(" + str(i+1) + ")", arr[i])
#     else:
#         print()
