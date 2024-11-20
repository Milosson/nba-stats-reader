
## WE TESTING THIS NBA ! 



 Forka projektet (om du vill skapa en egen version av projektet på GitHub)
För att skapa en egen kopia av detta projekt under ditt eget GitHub-konto, följ dessa steg:

Gå till projektets GitHub-sida: Länk till projektet
Klicka på Fork-knappen i det övre högra hörnet av sidan.
GitHub skapar nu en egen kopia av projektet under ditt användarnamn. Du kan nu göra ändringar på denna kopia utan att påverka originalprojektet.
Klona den forkade versionen till din lokala dator genom att köra följande kommando i din terminal:
bash
Kopiera kod
git clone https://github.com/Milosson/nba.git
Nu kan du börja arbeta med projektet lokalt och göra egna ändringar. För att uppdatera din forkade version kan du skapa en pull request till originalprojektet om du vill bidra med dina ändringar.
2. Klona projektet (om du bara vill kopiera projektet till din dator utan att forka)
För att klona projektet direkt till din dator utan att forka det, gör följande:

Gå till projektets GitHub-sida: Länk till projektet
Klicka på den gröna Code-knappen och kopiera URL
för kloning (HTTPS eller SSH).
Klona projektet till din dator genom att köra följande kommando i din terminal:
bash
Kopiera kod
git clone https://github.com/Milosson/nba.git
När kloningen är klar kan du navigera till projektmappen och börja arbeta med projektet lokalt.
3. Installera beroenden
För att kunna köra och utveckla projektet på din lokala maskin, se till att du har installerat de nödvändiga Python-paketen:

Se till att du har Python och pip installerat. Om inte, installera dem från python.org.
Klona projektet och navigera till projektmappen.
Skapa en virtuell miljö (rekommenderas) och aktivera den:
bash
Kopiera kod
python -m venv venv
source venv/bin/activate  # På Windows: venv\Scripts\activate
Installera de nödvändiga beroendena:
bash
Kopiera kod
pip install -r requirements.txt
Nu är du redo att börja utveckla och köra projektet lokalt!

4. Köra projektet
För att köra Streamlit-applikationen lokalt kan du använda följande kommando:

bash
Kopiera kod
streamlit run app.py
