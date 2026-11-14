# Passo 3 · Reparti

**Obiettivo:** estrarre la conoscenza reparto per reparto e scriverla come voci del cervello, ognuna con la sua fonte.

## Ordine

Parti dal reparto che possiede ciò che l'archetipo richiede per primo:

| Archetipo | Si estrae per primo | Reparto tipico |
|---|---|---|
| catalogo | Catalogo, prezzi, disponibilità | Prodotto e acquisti |
| agenda | Servizi, risorse, disponibilità | Accettazione o ricevimento |
| contratto | Prodotti, documenti, regole di adeguatezza | Compliance e tecnico |
| configurazione | Materiali e vincoli tecnici | Ufficio tecnico |
| pratica | Requisiti, documenti, scadenze | Uffici di settore |
| asset | Stato degli asset e degli ordini | Operazioni |

## Per ogni reparto

1. Prepara l'intervista con `modelli/intervista.md` e mandala al referente.
2. Leggi i documenti e i sistemi indicati nell'inventario.
3. Scrivi una voce per file in `cervello/<reparto>/` usando `modelli/voce.md`.
4. Classifica ogni voce per tipo:

| Tipo | Riconoscila così |
|---|---|
| fatti | È un dato: prodotto, prezzo di listino, orario, sede, cliente |
| regole | Contiene "se... allora", un calcolo, un limite, un'idoneità |
| processi | Ha passi in sequenza e stati: richiesta, approvazione, consegna |
| sapere | È esperienza: come si risolve un caso, cosa consigliare |
| identita | È ciò che l'azienda dichiara al pubblico: chi siamo, garanzie, condizioni |

5. Aggiorna il cervello in `azienda.json`: voce, tipo, proprietario, esposizione proposta, `fonte`, `"approvata": false`.

## Uscita

`cervello/` con una cartella per reparto; `azienda.json` aggiornato.

## Criterio di completamento

Ogni voce ha una fonte non vuota. Le voci che servono alla prima ondata di capacità esistono tutte.
