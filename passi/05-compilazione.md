# Passo 5 · Compilazione

**Obiettivo:** trasformare regole e processi in specifiche eseguibili, così che nessun modello debba interpretarli.

## Per ogni voce di tipo `regole`

1. Crea `motori/<nome-regola>.md` dal modello `modelli/regola.md`.
2. Scrivi input, output e la regola in modo non ambiguo (tabelle, formule, condizioni).
3. Scrivi almeno cinque **casi di test** con valori reali forniti dal proprietario: casi normali, casi limite, un caso che deve essere rifiutato.
4. Fai confermare i casi di test al proprietario. I casi di test sono la vera specifica: il codice dovrà superarli tutti.

## Per ogni voce di tipo `processi`

1. Descrivi gli stati (es. richiesta, in verifica, approvata, conclusa, annullata) e le transizioni ammesse.
2. Per ogni transizione indica chi la può fare: cliente, persona dell'azienda, software.
3. Le transizioni fatte dal cliente verso l'esterno diventano capacità di tipo `scrittura`, con consenso.

## Se puoi scrivere codice

Se il referente lo chiede e l'ambiente lo permette, scrivi il codice dei motori in un progetto separato, con i casi di test come test automatici. Il codice è completo solo quando supera tutti i casi confermati.

## Uscita

`motori/` con una specifica per regola e per processo, e i casi di test approvati.

## Criterio di completamento

Ogni capacità di tipo `calcolo` della prima ondata ha almeno un motore con casi di test approvati.
