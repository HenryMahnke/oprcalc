# This is a sample Python script.
import numpy as np
import requests
import json

url = "https://frc-api.firstinspires.org/v2.0/2020/matches/ARLI?tournamentLevel=Qualification"
credentials = '48d7bd35-7e9f-472e-9214-b86197af4f5b'
payload = {

}

params = {

}
api_key = "henrym:48d7bd35-7e9f-472e-9214-b86197af4f5b"  # but convert to base 64
headers = {
    'Authorization': 'Basic aGVucnltOjQ4ZDdiZDM1LTdlOWYtNDcyZS05MjE0LWI4NjE5N2FmNGY1Yg0K',
    'If-Modified-Since': '',
    'Content-Type': 'application/json',
    'Last-Modified': 'sed in laboris'
}

response = requests.request("GET", url, headers=headers, data=payload)

Json = response.text
Json = json.loads(Json)
# getting the teams at the competition
TeamsInMatch = []
ShowOrNotMatrix1 = []
TeamsInMatches = []
RedScores = []
BlueScores = []
JustTeamsList = []
BlueAndRedScores = []
for x in Json['Matches']:
    teams = x['teams']
    teams = [y['teamNumber'] for y in teams]
    copyMatrix = ShowOrNotMatrix1
    TeamsInMatches.append(teams)
    RedScores.append([x['scoreRedFinal']])
    BlueScores.append([x['scoreBlueFinal']])
    BlueAndRedScores.append([x['scoreRedFinal']])
    BlueAndRedScores.append([x['scoreBlueFinal']])
    for j in teams:
        TeamsInMatch.append(j)
for x in TeamsInMatch:
    if x not in JustTeamsList:
        JustTeamsList.append(x)
        ShowOrNotMatrix1.append(0)
finalRed = []
finalBlue = []
bothAlliances = []
for match in enumerate(TeamsInMatches):
    RedAlliance = match[1][0:3]
    BlueAlliance = match[1][3:6]
    TransformMat = ShowOrNotMatrix1.copy()
    TransformMat2 = ShowOrNotMatrix1.copy()
    for index in enumerate(JustTeamsList):
        for c in range(3):
            if index[1] == RedAlliance[c]:
                TransformMat[index[0]] = 1
                break
            if index[1] == BlueAlliance[c]:
                TransformMat2[index[0]] = 1
                break
    finalRed.append(TransformMat)
    finalBlue.append(TransformMat2)
    bothAlliances.append(TransformMat)
    bothAlliances.append(TransformMat2)
    # has to be every other becasue thats how the scores have to operate, and the alliances have to accurately correlate

transpose = np.transpose(bothAlliances)
res1 = np.dot(transpose, bothAlliances)
res2 = np.dot(transpose, BlueAndRedScores)

x2 = np.linalg.solve(res1, res2)

final = []
for x in range(len(JustTeamsList)):
    final.append(JustTeamsList[x])
    final.append(x2[x][0])
print(final)
# print(TeamsInMatches)
# print(TeamsInMatch)
