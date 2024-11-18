import streamlit as st
import pandas as pd
import plotly.express as px
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split

# Förklaring av kolumnförkortningar
column_rename_dict = {
    'PTS': 'Points',
    'AST': 'Assists',
    'REB': 'Rebounds',
    'FG%': 'Field Goal Percentage',
    '3P%': 'Three Point Percentage',
    'FT%': 'Free Throw Percentage',
    'MIN': 'Minutes Played',
    'FGM': 'Field Goals Made',
    'FGA': 'Field Goals Attempted',
    '3PM': 'Three Pointers Made',
    '3PA': 'Three Pointers Attempted',
    'FTM': 'Free Throws Made',
    'FTA': 'Free Throws Attempted',
    'ORB': 'Offensive Rebounds',
    'DRB': 'Defensive Rebounds',
    'TRB': 'Total Rebounds',
    'STL': 'Steals',
    'BLK': 'Blocks',
    'TOV': 'Turnovers',
    'PF': 'Personal Fouls',
    'PLUS-MINUS': 'Plus Minus',
    'Season': 'Season'
}

# Huvudrubrik
st.title("NBA Stats Visualizer")
st.write("Analysera och visualisera NBA-statistik för spelare och lag!")

# Steg 1: Ladda upp data
uploaded_file = st.file_uploader("Ladda upp en NBA-statistikfil (CSV)", type=["csv"])

if uploaded_file:
    # Försök läsa filen med rätt separator och kodning
    try:
        df = pd.read_csv(uploaded_file, encoding='ISO-8859-1', sep=';')
    except UnicodeDecodeError:
        st.error("Det gick inte att läsa filen med ISO-8859-1-kodning. Försök med en annan fil.")
        st.stop()  # Stoppar här om det inte går att läsa filen

    # Omnämna kolumner med hjälp av ordboken
    df.rename(columns=column_rename_dict, inplace=True)

    # Visa kolumnnamn för att säkerställa att filen lästs korrekt
    st.write("### Kolumnnamn i CSV-filen:")
    column_legend = pd.DataFrame(list(column_rename_dict.items()), columns=["Förkortning", "Fullständig beskrivning"])
    st.dataframe(column_legend)

    st.write("### Dataförhandsvisning")
    st.dataframe(df.head())

    # Kontrollera kolumner och visa möjliga val
    numeric_cols = df.select_dtypes(include=['float64', 'int64']).columns.tolist()
    player_col = st.selectbox("Välj kolumn för spelarnamn:", df.columns, index=0)
    stat_col = st.selectbox("Välj en statistikkolumn för analys:", numeric_cols, index=1)

    # Steg 2: Filtrering
    st.write("### Filtrera spelare")
    unique_players = df[player_col].unique().tolist()
    selected_players = st.multiselect("Välj spelare att analysera:", unique_players, unique_players[:5])

    filtered_df = df[df[player_col].isin(selected_players)]

    st.write("### Filtrerad data")
    st.dataframe(filtered_df)

    # Steg 3: Visualiseringar
    st.write("### Visualiseringar")

    # Stapeldiagram för valda spelares genomsnittliga statistik
    avg_stats = filtered_df.groupby(player_col)[stat_col].mean().reset_index()
    fig_bar = px.bar(
        avg_stats,
        x=player_col,
        y=stat_col,
        color=player_col,
        title=f"Genomsnittlig {stat_col} för valda spelare",
        labels={player_col: "Spelare", stat_col: stat_col},
        height=400,
    )
    st.plotly_chart(fig_bar)

    # Linjediagram över statistikens utveckling
    st.write("### Poängutveckling över tid (Exempel)")
    if 'Season' in df.columns:
        line_fig = px.line(
            filtered_df,
            x="Season",
            y=stat_col,
            color=player_col,
            title=f"{stat_col} över säsonger",
            labels={"Season": "Säsong", stat_col: stat_col},
        )
        st.plotly_chart(line_fig)

    # Automatisk prediktion (för nästa säsong)
    if 'Season' in df.columns:
        try:
            df['Season'] = df['Season'].astype(int)  # Försäkra att Season är ett heltal
        except ValueError:
            st.error("Kolumnen 'Season' måste vara numerisk för prediktion.")
            st.stop()

        # Kontrollera om vald statistikkolumn är numerisk
        if stat_col not in df.columns:
            st.error(f"Den valda kolumnen '{stat_col}' finns inte i data.")
            st.stop()

        X = df[['Season']].values
        y = df[stat_col].values

        # Se till att både X och y inte är tomma
        if X.shape[0] == 0 or y.shape[0] == 0:
            st.error("Data för prediktion är otillräcklig.")
            st.stop()

        # Dela upp data i tränings- och testset
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

        # Skapa och träna modellen
        model = LinearRegression()
        model.fit(X_train, y_train)

        # Gör prediktioner
        y_pred = model.predict(X_test)

        # Visualisera prediktioner
        test_results = pd.DataFrame({'Verklig': y_test, 'Predikterad': y_pred})
        st.write("Prediktioner jämfört med verkliga värden:")
        st.dataframe(test_results.head())

        # Enkel framtida prediktion
        next_season = max(X.flatten()) + 1
        pred_next_season = model.predict([[next_season]])[0]
        st.write(f"Förutsägelse för nästa säsong ({next_season}): **{pred_next_season:.2f} {stat_col}**.")
