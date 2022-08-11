import requests
from fastapi import FastAPI

app = FastAPI()

@app.get("/cricket")
def cricket():
    params = {
        'sports': '66',
        'count': '50',
        'lng': 'en',
        'getEmpty': 'true',
        'noFilterBlockEvent': 'true',
    }


    response = requests.get('https://linebet.com/LiveFeed/Get1x2_VZip', params=params)
    rj =response.json()
    match_lst = rj["Value"]
    print(len(match_lst))
    res_lst = []
    for match in match_lst:
        try:
            sc = match["SC"]["FS"]#score
        except Exception as e:
            print(e)
        if sc == {}:
            sc = {
                "S1":"0",
                "S2":"0"
                }
        l = match["L"]#league
        t1 = match["O1"]#T1
        t2 = match["O2"]#T2
        try:
            loc = match["MIO"]["Loc"]
        except:
            try:
                loc = match["CN"]
            except:
                loc = ""
        try:
            Type = match["MIO"]["MaF"]
        except:
            Type = ""
        cj = {
            "score":sc,
            "league":l,
            "team1":t1,
            "team2":t2,
            "location":loc,
            "type":Type,
        }
        res_lst.append(cj)
    return {"Result" : res_lst}

@app.get("/football")
def football():
    params = {
        'sports': '1',
        'count': '50',
        'lng': 'en',
        'getEmpty': 'true',
        'noFilterBlockEvent': 'true',
    }


    response = requests.get('https://linebet.com/LiveFeed/Get1x2_VZip', params=params)
    rj =response.json()
    match_lst = rj["Value"]
    print(len(match_lst))
    res_lst = []
    for match in match_lst:
        sc = match["SC"]["FS"]#score
        if sc == {}:
            sc = {"S1":0,"S2":0}
        if "S1" not in sc:
            sc["S1"] = 0
        if "S2" not in sc:
            sc["S2"] = 0
        l = match["L"]#league
        t1 = match["O1"]#T1
        t2 = match["O2"]#T2
        try:
            loc = match["MIO"]["Loc"]
        except:
            try:
                loc = match["CN"]
            except:
                loc = ""
        try:
            Type = match["MIO"]["MaF"]
        except:
            Type = ""
        print([l,t1,t2,Type,loc,str(sc)])
        cj = {
            "score":sc,
            "league":l,
            "team1":t1,
            "team2":t2,
            "location":loc,
            "type":Type,
        }
        res_lst.append(cj)
    return {"Result" : res_lst}

@app.get("/tabletennis")
def tableTennis():
    params = {
        'sports': '10',
        'count': '50',
        'lng': 'en',
        'getEmpty': 'true',
        'noFilterBlockEvent': 'true',
    }


    response = requests.get('https://linebet.com/LiveFeed/Get1x2_VZip', params=params)
    rj =response.json()
    match_lst = rj["Value"]
    print(len(match_lst))
    res_lst = []
    for match in match_lst:
        sc = match["SC"]["FS"]#score
        if sc == {}:
            sc = {
                "S1":"0",
                "S2":"0"
            }
        l = match["L"]#league
        t1 = match["O1"]#T1
        t2 = match["O2"]#T2
        try:
            loc = match["MIO"]["Loc"]
        except:
            try:
                loc = match["CN"]
            except:
                loc = ""
        try:
            Type = match["MIO"]["MaF"]
        except:
            Type = ""
        
        cj = {
            "score":sc,
            "league":l,
            "team1":t1,
            "team2":t2,
            "location":loc,
            "type":Type,
        }
        res_lst.append(cj)
    return {"Result" : res_lst}

