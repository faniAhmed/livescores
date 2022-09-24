import requests
from fastapi import FastAPI
from bs4 import BeautifulSoup as soap
import datetime

app = FastAPI()

@app.get("/upcoming")
def upcoming():
    date = datetime.datetime.now()    
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:103.0) Gecko/20100101 Firefox/103.0',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8',
        'Accept-Language': 'en-US,en;q=0.5',
        # 'Accept-Encoding': 'gzip, deflate, br',
        'DNT': '1',
        'Connection': 'keep-alive',
        'Upgrade-Insecure-Requests': '1',
        'Sec-Fetch-Dest': 'document',
        'Sec-Fetch-Mode': 'navigate',
        'Sec-Fetch-Site': 'none',
        'Sec-Fetch-User': '?1',
    }

    response = requests.get('https://sports.ndtv.com/cricket/schedules-fixtures', headers=headers)
    page = soap(response.text, "lxml")
    aaj = page.find_all("div", {"id": date.strftime("%d-%m-20%y")})
    kal = page.find_all("div", {"id": (date + datetime.timedelta(days=1)).strftime("%d-%m-20%y")})
    parson =page.find_all("div", {"id": (date + datetime.timedelta(days=2)).strftime("%d-%m-20%y")})
    tarson = page.find_all("div", {"id": (date + datetime.timedelta(days=3)).strftime("%d-%m-20%y")})
    charson = page.find_all("div", {"id": (date + datetime.timedelta(days=4)).strftime("%d-%m-20%y")})
    pacharson = page.find_all("div", {"id": (date + datetime.timedelta(days=5)).strftime("%d-%m-20%y")})
    sarson = page.find_all("div", {"id": (date + datetime.timedelta(days=6)).strftime("%d-%m-20%y")})
    satarson = page.find_all("div", {"id": (date + datetime.timedelta(days=7)).strftime("%d-%m-20%y")})
    lst = []
    for match in aaj:
        time = match.find("div", {"class":"scr_dt-red"}).get_text()
        res = {
            "Series" : match["data-series"],
            "Team1" : match["data-teama"],
            "Team2" : match["data-teamb"],
            "Stadium" : match["data-venue"],
            "time" : time
            }
        lst.append(res)

    for match in kal:
        time = match.find("div", {"class":"scr_dt-red"}).get_text()
        res = {
            "Series" : match["data-series"],
            "Team1" : match["data-teama"],
            "Team2" : match["data-teamb"],
            "Stadium" : match["data-venue"],
            "time" : time
            }
        lst.append(res)
    for match in parson:
        time = match.find("div", {"class":"scr_dt-red"}).get_text()
        res = {
            "Series" : match["data-series"],
            "Team1" : match["data-teama"],
            "Team2" : match["data-teamb"],
            "Stadium" : match["data-venue"],
            "time" : time
            }
        lst.append(res)
    for match in tarson:
        time = match.find("div", {"class":"scr_dt-red"}).get_text()
        res = {
            "Series" : match["data-series"],
            "Team1" : match["data-teama"],
            "Team2" : match["data-teamb"],
            "Stadium" : match["data-venue"],
            "time" : time
            }
        lst.append(res)
    for match in charson:
        time = match.find("div", {"class":"scr_dt-red"}).get_text()
        res = {
            "Series" : match["data-series"],
            "Team1" : match["data-teama"],
            "Team2" : match["data-teamb"],
            "Stadium" : match["data-venue"],
            "time" : time
            }
        lst.append(res)

    for match in pacharson:
        time = match.find("div", {"class":"scr_dt-red"}).get_text()
        res = {
            "Series" : match["data-series"],
            "Team1" : match["data-teama"],
            "Team2" : match["data-teamb"],
            "Stadium" : match["data-venue"],
            "time" : time
            }
        lst.append(res)


    for match in sarson:
        time = match.find("div", {"class":"scr_dt-red"}).get_text()
        res = {
            "Series" : match["data-series"],
            "Team1" : match["data-teama"],
            "Team2" : match["data-teamb"],
            "Stadium" : match["data-venue"],
            "time" : time
            }
        lst.append(res)

    for match in satarson:
        time = match.find("div", {"class":"scr_dt-red"}).get_text()
        res = {
            "Series" : match["data-series"],
            "Team1" : match["data-teama"],
            "Team2" : match["data-teamb"],
            "Stadium" : match["data-venue"],
            "time" : time
            }
        lst.append(res)
    return {"result" : lst} 


@app.get("/cricket2")
def cricket2():
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
    res_lst = []
    for match in match_lst:
        link = match["LI"]
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
        cj = {
            "score":sc,
            "league":l,
            "team1":t1,
            "team2":t2,
            "location":loc,
            "type":Type,
            "Link":link
        }
        res_lst.append(cj)
    return {"Result" : res_lst}

@app.get("/cricket")
def cricket():
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:103.0) Gecko/20100101 Firefox/103.0',
        'Accept': 'image/avif,image/webp,*/*',
        'Accept-Language': 'en-US,en;q=0.5',
        # 'Accept-Encoding': 'gzip, deflate, br',
        'DNT': '1',
        'Connection': 'keep-alive',
        'Referer': 'https://sports.ndtv.com/',
        'Sec-Fetch-Dest': 'image',
        'Sec-Fetch-Mode': 'no-cors',
        'Sec-Fetch-Site': 'cross-site',
    }
    reqs = requests.Session()
    reqs.headers.update(headers)
    response = reqs.get('https://e3.adpushup.com/AdPushupFeedbackWebService/user/sync', headers=headers)

    result = []

    params = {
        'methodtype': '3',
        'client': '2656770267',
        'sport': '1',
        'league': '0',
        'timezone': '0530',
        'language': 'en',
        'gamestate': '1',
        'widget': 'livescorepagejs',
        'callback': 'cb',
    }

    response = reqs.get('https://sports.ndtv.com/multisportsapi/', params=params)

    matches = eval(response.text.replace(");","").replace("cb(",""))["matches"]

    for match in matches:
        result.append(
            {
                "Team 1": match["participants"][0]["name"],
                "Team 2": match["participants"][1]["name"],
                "Start date": match["start_date"],
                "Score Team 1": match["participants"][0]["value"],
                "Score Team 2": match["participants"][1]["value"],
                "event_sub_status" : match["event_sub_status"] ,
                "Tour Name": match["tour_name"],
                "Stadium": match["venue_name"],
                "Type" : match["event_format"],
            }
        )
    print(result)
    return {"Result" : result}

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
                "S1":0,
                "S2":0
            }
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

