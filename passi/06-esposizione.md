# Passo 6 · Esposizione

**Obiettivo:** decidere cosa possono chiedere gli agenti dei clienti, e a quali condizioni.

## Cosa fai

1. Rivedi le `capacita` in `azienda.json` con il referente. Per ognuna conferma:

| Campo | Domanda |
|---|---|
| `tipo` | Legge, calcola, scrive verso l'esterno o dà consulenza? |
| `esegue` | Chi la esegue? `software` per letture, calcoli e la maggior parte delle scritture; `persona` quando decide qualcuno; `ai` solo per la consulenza |
| `consenso` | `true` per ogni scrittura, `false` altrimenti |
| `esposizione` | `pubblico` (qualsiasi agente), `cliente` (cliente autenticato, sui suoi dati), `partner` (controparti con contratto), `interno` |
| `descrizione` | Cosa ottiene chi la chiama, in una riga |

2. Scegli con il referente la **prima ondata**: poche capacità, utili, già supportate da voci approvate e motori con test. Almeno una deve essere `pubblico`.
3. Per le capacità con `"esegue": "ai"` verifica che si basino solo su voci di tipo `sapere` o `identita` approvate.

## Uscita

Contratto delle capacità e prima ondata in `azienda.json`.

## Criterio di completamento

`python strumenti/verifica.py azienda.json` restituisce "valido". Il referente approva la prima ondata.

## E poi

Il contratto è pronto per essere pubblicato: server MCP, Agent Card A2A, indici aperti, directory dei provider. Puoi farlo con il tuo team tecnico o con un servizio che lo gestisce per te.
