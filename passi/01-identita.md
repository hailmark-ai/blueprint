# Passo 1 · Identità

**Obiettivo:** capire chi è l'azienda e partire dal blueprint del suo settore.

## Domande al referente

1. Nome dell'azienda, sito, sede.
2. Cosa compra il cliente, in una frase? Usa la risposta per scegliere l'archetipo:

| Il cliente compra | Archetipo |
|---|---|
| Un prodotto già fatto | catalogo |
| Un orario, un servizio su prenotazione | agenda |
| Un contratto con obblighi di legge (polizza, conto, fornitura) | contratto |
| Qualcosa fatto su misura | configurazione |
| Un procedimento o un adempimento | pratica |
| Un'operazione su beni fisici (produzione, trasporto, manutenzione) | asset |

3. Quale settore in `settori/` è più vicino? Se nessuno è adatto, parti da quello con lo stesso archetipo.

## Cosa fai

1. Copia il blueprint scelto da `settori/<settore>.json` in `azienda.json`.
2. Aggiungi in cima il blocco:

```json
"azienda": { "nome": "...", "sito": "...", "settore_di_partenza": "<settore>" }
```

3. Adatta `nome` e `perche` all'azienda. Non toccare ancora cervello e capacità: sono ipotesi da verificare nei passi successivi.
4. Per ogni voce del cervello aggiungi `"fonte": ""` e `"approvata": false`.
5. Elenca con il referente le parti principali dell'azienda (es. risposte ai clienti, prezzi, pianificazione, macchinari) e per ognuna scegli il livello con `architetture/livelli.md`. Scrivilo in `azienda.json`:

```json
"dinamicita": [ { "parte": "...", "livello": "dinamico | ibrido | statico", "motivo": "..." } ]
```

6. Crea `stato.md` con il passo corrente.

## Uscita

`azienda.json` con l'identità dell'azienda, lo scheletro del settore e i livelli di dinamicità.

## Criterio di completamento

`python strumenti/verifica.py azienda.json --bozza` non segnala errori di struttura. Il referente conferma settore e archetipo.
