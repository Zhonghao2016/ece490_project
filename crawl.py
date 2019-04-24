import numpy as np


template = 'http://www.espn.com/nba/teams/comparison/_/year/2018/team1/chi/team2/gsw'
def make_team_url():
    team_name = [
        'atl',
        'bos',
        'bkn',
        'cha',
        'chi',
        'cle',
        'dal',
        'den',
        'det',
        'gsw',
        'hou',
        'ind',
        'lac',
        'lal',
        'mem',
        'mia',
        'mil',
        'min',
        'nor',
        'nyk',
        'okc',
        'orl',
        'phi',
        'pho',
        'por',
        'sac',
        'sas',
        'tor',
        'uth',
        'was',
    ]
    team_url = []
    for i in range(30):
        for j in range(i+1, 30):
            url = template.split('/')
            url[-3] = team_name[i]
            url[-1] = team_name[j]
            team_url.append('/'.join(url))
    return team_url

for item in make_team_url():
    print(item)



