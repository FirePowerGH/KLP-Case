# En enkel bankløsning for KLP

Denne oppgaven bruker **Flask** med *python* for å lage en webserver og **SQLite** for en backend database til å lagre dataen.

> **SQLite** er en versjon av **MySQL** som blir lagret som en fil, istedet for å ligge i minnet.
>
> Jeg har valgt å bruke **SQLite** fordi jeg har bare vært borti **MySQL** før, så for å lære noe nytt. Men også for den er enklere å dele, og opprette i koden på sparket.
>> Hadde jeg brukt **MySQL** ville jeg med tanke på sikkerhet lagret databasen på en fjern-server, hvor det kunne vært vanskelig for dere å få tilgang uten en SSH-nøkkel.

## Login systemet
For login systemet har jeg lagret alle bruker detaljene i databasen. Men før de bli lagret, passer jeg på å hashe passord og legger til salt i hashen. Dette er for å forhindre at noen med tilgang til databasen kan hente inn passordene til alle sammen, og salt forhindrer *rainbow-table* og *dictionary* angrep ved å gjøre alle hash helt ulike uansett hva passordet originalt var. Så uten det originale passordet og saltet, er det **umulig** å finne passordene.