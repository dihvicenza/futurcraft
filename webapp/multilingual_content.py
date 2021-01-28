"""
This file contains strings to translate the Dash app into 3 languages: English, Italian and German.
All the content variable names must be identical to 'id' attributes of the corresponding html elements
"""
h1 = {
"en": "Educational Offer vs Business Needs",
"de": "Schulungsangebot im Vergleich zu Geschäftsanforderungen",
"it": "La presenza di competenze nelle imprese e l'offerta formativa nelle scuole"
}

p_desc = {
"en": """Lorem ipsum dolor sit amet, consectetuer adipiscing elit. Aenean commodo ligula eget dolor. Aenean massa. 
Cum sociis natoque penatibus et magnis dis parturient montes, nascetur ridiculus mus. Donec quam felis, 
ultricies nec, pellentesque eu, pretium quis, sem. Nulla consequat massa quis enim. Donec pede justo, fringilla vel, 
aliquet nec, vulputate eget, arcu. In enim justo, rhoncus ut, imperdiet a, venenatis vitae, justo. Nullam dictum 
felis eu pede mollis pretium. Integer tincidunt. Cras dapibus. Vivamus elementum semper nisi. Aenean vulputate 
eleifend tellus. Aenean leo ligula, porttitor eu, consequat vitae, eleifend ac, enim. Aliquam lorem ante, dapibus in, 
viverra quis, feugiat a, tellus.""",

"de": """Auch gibt es niemanden, der den Schmerz an sich liebt, sucht oder wünscht, nur, weil er Schmerz ist, 
es sei denn, es kommt zu zufälligen Umständen, in denen Mühen und Schmerz ihm große Freude bereiten können. Um ein 
triviales Beispiel zu nehmen, wer von uns unterzieht sich je anstrengender körperlicher Betätigung, außer um Vorteile 
daraus zu ziehen? Aber wer hat irgend ein Recht, einen Menschen zu tadeln, der die Entscheidung trifft, eine Freude 
zu genießen, die keine unangenehmen Folgen hat, oder einen, der Schmerz vermeidet, welcher keine daraus resultierende 
Freude nach sich zieht? Auch gibt es niemanden, der den Schmerz an sich liebt, sucht oder wünscht, nur, 
weil er Schmerz ist, es sei denn, es kommt zu zufälligen Umständen.""",

"it": """L’iniziativa FuturCRAFT avrà il compito di definire i possibili scenari futuri per i profili di competenza 
digitale nell’artigianato e di illustrare le opportunità di digitalizzazione disponibili per le aziende artigiane. 
Con il supporto di svariate ricerche ed analisi verrà esaminata l’attuale offerta formativa: un’indagine Delphi ed 
alcune discussioni tra esperti mostreranno l’influenza della digitalizzazione sui mestieri artigiani, 
si effettueranno delle visite in realtà artigiane ed in generale si prenderà contatto più da vicino con la realtà 
dell’artigianato. Sulla base dei risultati si cercherà di sviluppare delle strategie di digitalizzazione utili per 
sostenere le aziende nella propria attività di innovazione."""
}

p_dev_by = {
"en": "Developed by [Digital Innovation Hub Vicenza](https://digitalinnovationhubvicenza.it/)",
"de": "Entwickelt von [Digital Innovation Hub Vicenza](https://digitalinnovationhubvicenza.it/)",
"it": "Sviluppato da [Digital Innovation Hub Vicenza](https://digitalinnovationhubvicenza.it/)"
}

p_read_more = {
"en": "Read more on [Confartigianato Vicenza - FuturCRAFT](https://www.confartigianatovicenza.it/futurcraft/)",
"de": "Lesen Sie mehr: [Confartigianato Vicenza - FuturCRAFT](https://www.confartigianatovicenza.it/futurcraft/)",
"it": "Scopri di più su [Confartigianato Vicenza - FuturCRAFT](https://www.confartigianatovicenza.it/futurcraft/)"
}

h2_ref = {
"en": """
## Data Citation
- Aggregated data of the provinces of TV, VI and BZ. SELFI4.0 survey project [Punto Impresa Digitale](https://www.puntoimpresadigitale.camcom.it/)
- FuturCRAFT survey data on upper secondary schools and vocational training centers in mechanics and carpentry""",
"de": """
## Datenzitat
- Aggregierte Daten der Provinzen TV, VI und BZ. SELFI4.0-Umfrageprojekt [Punto Impresa Digitale](https://www.puntoimpresadigitale.camcom.it/)
- FuturCRAFT-Umfragedaten zu Schulen der Sekundarstufe II und Berufsbildungszentren für Mechaniker und Schreiner""",

"it": """
## Citazione dei dati
- Dati aggregati delle provincie di TV, VI e BZ. Indagine SELFI4.0 Progetto [Punto Impresa Digitale](https://www.puntoimpresadigitale.camcom.it/)
- Dati indagine FuturCRAFT su scuole secondarie di secondo grado e centri di formazione professionale di indirizzo meccanica e legno"""
}

# Prepare a list of all variables declared above
variables = [v for v in dir() if "__" not in v]
