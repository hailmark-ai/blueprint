# Passo 4 · Validazione

**Obiettivo:** ogni voce approvata dalla persona che ne risponde.

## Cosa fai

1. Per ogni proprietario prepara un elenco delle sue voci: testo, fonte, esposizione proposta.
2. Chiedi al referente di farlo rivedere. Per ogni voce il proprietario risponde: approvata, da correggere, non nostra.
3. Correggi le voci; riassegna quelle "non nostra" al reparto giusto.
4. Segna `"approvata": true` solo per le voci confermate in modo esplicito, e annota in `stato.md` chi ha approvato e quando.
5. Segnala al referente ogni contraddizione tra fonti: non risolverla da solo.

## Attenzione all'esposizione

* Le voci di tipo `regole` non possono essere `cliente` o `pubblico`. Se il proprietario vuole rendere pubblica una condizione (es. politica di reso), è una voce di tipo `identita`.
* Nel dubbio, scegli il livello più chiuso. Si può aprire dopo.

## Uscita

Cervello approvato.

## Criterio di completamento

`python strumenti/verifica.py azienda.json` non segnala errori. Nessuna voce necessaria alla prima ondata ha `"approvata": false`.
