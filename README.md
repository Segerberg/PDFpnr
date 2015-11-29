# PDFpnr
Extraherar personnummer ur ett specifikt metadatafält i PDF-filer och genererar en CSV-fil med personnummer mappat mot filnamn
Översikt
PDFpnr är ett program som utvecklats för ett mycket specifikt behov av att göra ett stor mängd betygshandlingar sökbara i en databas. Programet extraherar personnummer ur ett specifikt metadatafält i PDF-filer och genererar en CSV-fil med personnummer mappat mot filnamn. CSV-filen kan sedan läsas in i valfri databas.

Programmet klarar att extrahera metadata ur pdf-filerna oberoende av katalogstruktur och även i de fall flera personnummer finns i ett och samma dokument förutsatt att dessa är avskilda med kommatecken.

Programmet utför också en enkel kvalitetskontroll av metadatan enligt följande: * Kontrollerar att personnummer finns * Kontroll att personnummer innehåller rätt antal tecken * Kontrollerar att personnummret endast innehåller siffror och bindestreck

Upptäcker programmet något fel exkluderas filen i och dess metadata i CSV exporten och loggas istället i separat fil. 

http://arkivwiki.se/doku.php?id=verktyg:pdfpnr
