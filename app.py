import streamlit as st

# API leagues
url = "https://api-football-v1.p.rapidapi.com/v3/leagues"

headers = {
    "X-RapidAPI-Key": "bb9249e25dmshc5d78685a4da268p16a12djsn4ca0e8774982",
    "X-RapidAPI-Host": "api-football-v1.p.rapidapi.com"
}

# nadpis aplikace a unsafe_allow_html je abych umožnil používat HTML a css
st.write("<div style='text-align: center; margin-bottom: 30px; font-size: 30px;'> {} </div>".format(
    "Football App Standing"), unsafe_allow_html=True)

# response ukládá odpověď na HTTP GET požadavek na API endpoint v url, včetně stavového kódu, hlaviček a těla odpovědi.
response = requests.get(url, headers=headers)

# json_leagues načítá data ze serverové odpovědi v JSON formátu uložené v proměnné response.text.
json_leagues = json.loads(response.text)
col1, col2 = st.columns(2)  # sloupce

# Vytváří prázdné slovníky leagues_dict a leagues_year na ukládání dat.
leagues_dict = {}
leagues_year = {}

# Tento kód je určen pro zpracování dat v JSON formátu, která obsahují informace o fotbalových ligách a soutěžích z celého světa.
# Kód prochází všechny ligy v JSON datovém souboru, získává jejich názvy, ID, zemi a typ(národní nebo mezinárodní). Pokud je liga mezi vybranými ligami, které jsou definovány v podmínkách(např. Ligue 1 v zemi Francie), tak jsou uloženy do slovníku s názvem 'leagues_dict'.
# Pro každou ligu jsou také získávány roky sezón, ve kterých se liga konala. Tyto roky jsou pak uloženy do slovníku 'leagues_year' pro každou ligu zvlášť.
# Podmínky pro výběr lig jsou definovány pomocí if -else podmínek. Pro každou vybranou ligu se procházejí její sezóny a získávají se roky, ve kterých se liga konala. Pokud jsou výsledné roky v určitém rozmezí, jsou přidány do seznamu 'leagues_year_list' a nakonec uloženy do slovníku 'leagues_year'.
for league in json_leagues["response"]:
    league_id = league["league"]["id"]
    league_name = league["league"]["name"]
    league_country = league["country"]["name"]
    league_type = league["league"]["type"]
    if league_name == "Ligue 1" and league_country == "France":
        leagues_dict[league_id] = f'{league_country} - {league_name}'
        leagues_year_list = []
        for season in league["seasons"]:
            leagues_year_list.append(season["year"])
        leagues_year[league_id] = leagues_year_list
    elif league_name == "World Cup" and league_type == "international":
        leagues_dict[league_id] = f'{league_country} - {league_name}'
        leagues_year_list = []
        for season in league["seasons"]:
            leagues_year_list.append(season["year"])
        leagues_year[league_id] = leagues_year_list
    elif league_name == "Euro" and league_type == "international":
        leagues_dict[league_id] = f'{league_country} - {league_name}'
        leagues_year_list = []
        for season in league["seasons"]:
            leagues_year_list.append(season["year"])
        leagues_year[league_id] = leagues_year_list
    elif league_name == "Serie A" and league_country == "Italy":
        leagues_dict[league_id] = f'{league_country} - {league_name}'
        leagues_year_list = []
        for season in league["seasons"]:
            leagues_year_list.append(season["year"])
        leagues_year[league_id] = leagues_year_list
    elif league_name == "Premier League" and league_country == "England":
        leagues_dict[league_id] = f'{league_country} - {league_name}'
        leagues_year_list = []
        for season in league["seasons"]:
            leagues_year_list.append(season["year"])
        leagues_year[league_id] = leagues_year_list
    elif league_name == "Bundesliga" and league_country == "Germany":
        leagues_dict[league_id] = f'{league_country} - {league_name}'
        leagues_year_list = []
        for season in league["seasons"]:
            leagues_year_list.append(season["year"])
        leagues_year[league_id] = leagues_year_list
    elif league_name == "Primeira Liga" and league_country == "Portugal":
        leagues_dict[league_id] = f'{league_country} - {league_name}'
        leagues_year_list = []
        for season in league["seasons"]:
            leagues_year_list.append(season["year"])
        leagues_year[league_id] = leagues_year_list
    elif league_name == "Eredivisie" and league_country == "Netherlands":
        leagues_dict[league_id] = f'{league_country} - {league_name}'
        leagues_year_list = []
        for season in league["seasons"]:
            leagues_year_list.append(season["year"])
        leagues_year[league_id] = leagues_year_list
    elif league_name == "La Liga" and league_country == "Spain":
        leagues_dict[league_id] = f'{league_country} - {league_name}'
        leagues_year_list = []
        for season in league["seasons"]:
            leagues_year_list.append(season["year"])
        leagues_year[league_id] = leagues_year_list
    elif league_name == "Euro Championship" and league_country == "World":
        leagues_dict[league_id] = f'{league_country} - {league_name}'
        leagues_year_list = []
        for season in league["seasons"]:
            year = season["year"]
            if year >= 2020 and year <= 2020:
                leagues_year_list.append(year)
        leagues_year[league_id] = leagues_year_list
    elif league_name == "World Cup" and league_country == "World":
        leagues_dict[league_id] = f'{league_country} - {league_name}'
        leagues_year_list = []
        for season in league["seasons"]:
            year = season["year"]
            if year >= 2018 and year <= 2022:
                leagues_year_list.append(year)
        leagues_year[league_id] = leagues_year_list
    elif league_name == "UEFA Champions League" and league_country == "World":
        leagues_dict[league_id] = f'{league_country} - {league_name}'
        leagues_year_list = []
        for season in league["seasons"]:
            leagues_year_list.append(season["year"])
        leagues_year[league_id] = leagues_year_list
    elif league_name == "UEFA Europa League" and league_country == "World":
        leagues_dict[league_id] = f'{league_country} - {league_name}'
        leagues_year_list = []
        for season in league["seasons"]:
            year = season["year"]
            if year >= 2018 and year <= 2022:
                leagues_year_list.append(year)
        leagues_year[league_id] = leagues_year_list
    elif league_name == "UEFA Europa Conference League" and league_country == "World":
        leagues_dict[league_id] = f'{league_country} - {league_name}'
        leagues_year_list = []
        for season in league["seasons"]:
            leagues_year_list.append(season["year"])
        leagues_year[league_id] = leagues_year_list

with col1:  # 1 sloupec
    # kód vytváří výběrové pole s názvy lig uloženými v proměnné leagues_dict. Po výběru ligy se uloží název do proměnné chosen_league_name.
    chosen_league_name = st.selectbox(
        # 1. values dá hodnoty do slovníku
        'Select a leagues:', options=leagues_dict.values())

# key, value prochází každý prvek v leagues_dict.items() pomocí for smyčky.
for key, value in leagues_dict.items():
    # Porovnává název ligy (value) s chosen_league_name.
    if value == chosen_league_name:
        # Pokud se názvy shodují, uloží příslušné ID ligy (key) do proměnné chosen_league_id.
        chosen_league_id = key

# Vypíše ID vybrané ligy pomocí funkce st.write(chosen_league_id).
st.write(chosen_league_id)

with col2:  # 2 sloupec
    # Po výběru se uloží název vybraného ročníku do proměnné chosen_seasons.
    chosen_seasons = st.selectbox(
        # vybrat ročník ze seznamu možností uložených v proměnné
        'Select a seasons:', options=leagues_year[chosen_league_id])

# API standings
url = "https://api-football-v1.p.rapidapi.com/v3/standings"

querystring = {
    "season": chosen_seasons,
    "league": chosen_league_id
}

headers = {
    "X-RapidAPI-Key": "bb9249e25dmshc5d78685a4da268p16a12djsn4ca0e8774982",
    "X-RapidAPI-Host": "api-football-v1.p.rapidapi.com"
}

# Tento kód slouží k získání dat o aktuálním pořadí týmů v lize, kterou uživatel vybral v předchozím kroku. K tomu využívá API-endpointu pro získání informací o aktuálním pořadí týmů (standings).
response = requests.request("GET", url, headers=headers, params=querystring)
response_standing = response
json_standings = json.loads(response_standing.text)

# tabulka
df_standing = pd.DataFrame()

# Proměnná "data" je prázdný seznam, který bude sloužit k ukládání řádků (záznamů) do pandas DataFrame.
data = []

# API Top Scorers
url = "https://api-football-v1.p.rapidapi.com/v3/players/topscorers"

querystring = {
    "season": chosen_seasons,
    "league": chosen_league_id
}

headers = {
    "X-RapidAPI-Key": "bb9249e25dmshc5d78685a4da268p16a12djsn4ca0e8774982",
    "X-RapidAPI-Host": "api-football-v1.p.rapidapi.com"
}

response = requests.get(url, headers=headers, params=querystring)

response = requests.get(url, headers=headers, params=querystring)
response_topscorers = response
json_topscorers = json.loads(response_topscorers.text)

df_gol = pd.DataFrame()

for item in json_topscorers["response"]:
    player_name = item["player"]["name"]
    for stat in item["statistics"]:
        team_name = stat["team"]["name"]
        goals_total = stat["goals"]["total"]
        goal_statistics = pd.DataFrame.from_dict({
            "player": player_name,
            "team": team_name,
            "goals": goals_total, }, orient='index').transpose()
        df_gol = pd.concat([df_gol, goal_statistics]).reset_index(drop=True)
        df_gol.index += 1
        df_gol = df_gol.sort_values(by="goals", ascending=False).head(8)

# API Top Assists
url = "https://api-football-v1.p.rapidapi.com/v3/players/topassists"

querystring = {
    "season": chosen_seasons,
    "league": chosen_league_id
}

headers = {
    "X-RapidAPI-Key": "bb9249e25dmshc5d78685a4da268p16a12djsn4ca0e8774982",
    "X-RapidAPI-Host": "api-football-v1.p.rapidapi.com"
}

response = requests.get(url, headers=headers, params=querystring)
response_topassists = response
json_topassists = json.loads(response_topassists.text)

df_assists = pd.DataFrame()

for item in json_topassists["response"]:
    player_name = item["player"]["name"]
    for stat in item["statistics"]:
        team_name = stat["team"]["name"]
        assists_total = stat["goals"]["assists"]
        assists_statistics = pd.DataFrame.from_dict({
            "player": player_name,
            "team": team_name,
            "assists": assists_total, }, orient='index').transpose()
        df_assists = pd.concat(
            [df_assists, assists_statistics]).reset_index(drop=True)
        df_assists.index += 1
        df_assists = df_assists.sort_values(
            by="assists", ascending=False).head(8)

# API Red Cards
url = "https://api-football-v1.p.rapidapi.com/v3/players/topredcards"

querystring = {
    "season": chosen_seasons,
    "league": chosen_league_id
}

headers = {
    "X-RapidAPI-Key": "bb9249e25dmshc5d78685a4da268p16a12djsn4ca0e8774982",
    "X-RapidAPI-Host": "api-football-v1.p.rapidapi.com"
}

response = requests.get(url, headers=headers, params=querystring)

response_topredcard = response
json_topredcard = json.loads(response_topredcard.text)

df_redcard = pd.DataFrame()

for item in json_topredcard["response"]:
    player_name = item["player"]["name"]
    for stat in item["statistics"]:
        team_name = stat["team"]["name"]
        redcard_total = stat["cards"]["red"]
        redcard_statistics = pd.DataFrame.from_dict({
            "player": player_name,
            "team": team_name,
            "red cards": redcard_total, }, orient='index').transpose()
        df_redcard = pd.concat(
            [df_redcard, redcard_statistics]).reset_index(drop=True)
        df_redcard.index += 1
        df_redcard = df_redcard.sort_values(
            by="red cards", ascending=False).head(8)

df_yellowred = pd.DataFrame()

for item in json_topredcard["response"]:
    player_name = item["player"]["name"]
    for stat in item["statistics"]:
        team_name = stat["team"]["name"]
        yellowred_total = stat["cards"]["yellowred"]
        yellowred_statistics = pd.DataFrame.from_dict({
            "player": player_name,
            "team": team_name,
            "yellowred cards": yellowred_total, }, orient='index').transpose()
        df_yellowred = pd.concat(
            [df_yellowred, yellowred_statistics]).reset_index(drop=True)
        df_yellowred.index += 1
        df_yellowred = df_yellowred.sort_values(
            by="yellowred cards", ascending=False).head(8)

# Sloučit tabulky podle sloupců "player" a "team"
df_combined = pd.merge(df_redcard, df_yellowred, on=[
                       "player", "team"], how="outer")
# Převést prázdné hodnoty na 0
df_combined = df_combined.fillna(0)
# Vytvořit sloupec "total cards" jako součet počtu červených a žlutých karet
df_combined["total cards"] = df_combined["red cards"] + \
    df_combined["yellowred cards"]
# Seřadit podle "total cards" sestupně a vybrat prvních 8 řádků
df_combined = df_combined.sort_values(
    by="total cards", ascending=False).head(8)
# Omezit na sloupce "player", "team" a "total cards"
df_combined = df_combined[["player", "team", "total cards"]]
# Resetovat index
df_combined = df_combined.reset_index(drop=True)
df_combined.index += 1

# API Yellow Cards
url = "https://api-football-v1.p.rapidapi.com/v3/players/topyellowcards"

querystring = {
    "season": chosen_seasons,
    "league": chosen_league_id
}

headers = {
    "X-RapidAPI-Key": "bb9249e25dmshc5d78685a4da268p16a12djsn4ca0e8774982",
    "X-RapidAPI-Host": "api-football-v1.p.rapidapi.com"
}

response = requests.get(url, headers=headers, params=querystring)

response_top_yellow_card = response
json_top_yellow_card = json.loads(response_top_yellow_card.text)

df_yellow_card = pd.DataFrame()

for item in json_top_yellow_card["response"]:
    player_name = item["player"]["name"]
    for stat in item["statistics"]:
        team_name = stat["team"]["name"]
        yellow_card_total = stat["cards"]["yellow"]
        yellow_card_statistics = pd.DataFrame.from_dict({
            "player": player_name,
            "team": team_name,
            "yellow cards": yellow_card_total, }, orient='index').transpose()
        df_yellow_card = pd.concat(
            [df_yellow_card, yellow_card_statistics]).reset_index(drop=True)
        df_yellow_card.index += 1
        df_yellow_card = df_yellow_card.sort_values(
            by="yellow cards", ascending=False).head(8)

# tlačítko na request
if st.button('send a request'):
    st.write("<div style='text-align: center; margin-bottom: 30px; font-size: 25px;'> {} </div>".format(
        "Standing"), unsafe_allow_html=True)
    # Tento kód projde první tabulku první ligy v JSON objektu a extrahuje informace o každém týmu v této tabulce, jako je pořadí, počet bodů, název týmu, počet odehraných zápasů, počet vyhraných zápasů, počet prohraných zápasů a počet remíz. pak to přidá do tabulky pandas
    for gr in json_standings["response"][0]["league"]["standings"]:
        group = gr[0]["group"]
        for standing in gr:
            standing_rank = standing["rank"]
            standing_points = standing["points"]
            standing_name = standing["team"]["name"]
            standing_played_all = standing["all"]["played"]
            standing_win_game = standing["all"]["win"]
            standing_lose_game = standing["all"]["lose"]
            standing_draw_game = standing["all"]["draw"]
            standing_app = pd.DataFrame.from_dict({
                "team": standing_name,
                "played": standing_played_all,
                "points": standing_points,
                "win": standing_win_game,
                "lose": standing_lose_game,
                "draw": standing_draw_game,
                "rank": standing_rank}, orient='index').transpose()
            df_standing = pd.concat(
                [df_standing, standing_app]).reset_index(drop=True)
            df_standing.index += 1
            # check if we have processed all teams in current group
        if standing == gr[-1]:
            # create table for current group
            group_table = df_standing.tail(len(gr)).reset_index(drop=True)
            # add group name to the table
            group_table.insert(0, "group", group)
            group_table.index += 1
            group_table = group_table.drop('group', axis=1)
            # display the group table using Streamlit's dataframe element
            st.write(group)
            st.table(group_table)
            # reset the df_standing for the next group
            df_standing = pd.DataFrame()
    st.write("<div style='text-align: center; margin-bottom: 30px; font-size: 25px;'> {} </div>".format(
        "Player Stats"), unsafe_allow_html=True)
    col3, col4 = st.columns(2)  # sloupce
    col5, col6 = st.columns(2)  # sloupce
    with col3:  # 3 sloupec
        st.write("<div style='text-align: center; margin-bottom: 30px; font-size: 20px;'> {} </div>".format(
            "Goals"), unsafe_allow_html=True)
        st.table(df_gol)
    with col4:  # 4 sloupec
        st.write("<div style='text-align: center; margin-bottom: 30px; font-size: 20px;'> {} </div>".format(
            "Assists"), unsafe_allow_html=True)
        st.table(df_assists)
    with col5:  # 5 sloupec
        st.write("<div style='text-align: center; margin-bottom: 30px; font-size: 20px;'> {} </div>".format(
            "Red Cards"), unsafe_allow_html=True)
        st.table(df_combined)
    with col6:  # 6 sloupec
        st.write("<div style='text-align: center; margin-bottom: 30px; font-size: 20px;'> {} </div>".format(
            "Yellow Cards"), unsafe_allow_html=True)
        st.table(df_yellow_card)
