# Hailmark Blueprint

**Scegli che azienda sei e come sei fatto. Dai questa cartella al tuo agente. Diventi un'azienda AI.**

Hailmark Blueprint guida un agente AI (Claude, ChatGPT o Codex, Gemini, un modello open in locale) a costruire, insieme alle persone dell'azienda:

* un **cervello**: la conoscenza dell'azienda, con un proprietario per ogni voce;
* un'**AI per reparto**, collegata a quel cervello;
* l'**architettura del tuo settore**, con ogni parte scelta come **dinamica, ibrida o statica**;
* i **motori**: le regole trasformate in codice con casi di test;
* le **capacità** pronte per andare online con [Hailmark Connect](https://github.com/hailmark-ai/connect).

## Le tre scelte

| Scelta | Dove |
|---|---|
| **Settore**: 12 settori pronti, 6 archetipi | `settori/` |
| **Struttura**: i tuoi reparti reali | passo 2 |
| **Dinamicità**: per ogni parte, dinamico, ibrido o statico | `architetture/livelli.md` |

## Come si usa

1. Copia la cartella dove il tuo agente può leggerla e scriverci.
2. Apri l'agente in quella cartella e scrivigli: **"Leggi AGENTS.md e guidami nel /init della mia azienda."**
3. Rispondi alle sue domande e coinvolgi i colleghi quando te lo chiede.
4. Alla fine controlla il risultato:

```console
python strumenti/verifica.py azienda.json
```

Serve Python 3.9 o successivo, nessuna libreria da installare.

## Cosa trovi

| Percorso | Contenuto |
|---|---|
| `AGENTS.md` | Le istruzioni per l'agente. È il punto di partenza |
| `passi/` | I sette passi del `/init` |
| `settori/` | Le architetture dei 12 settori |
| `architetture/livelli.md` | Come scegliere tra dinamico, ibrido e statico |
| `modelli/` | Inventario, interviste, voci del cervello, regole con test |
| `esempio/azienda.json` | Un'azienda inventata completata con il Blueprint |
| `strumenti/verifica.py` | Il controllo automatico |

## Le regole che il Blueprint non lascia violare

1. L'AI interpreta, il software decide: prezzi, permessi ed esiti non escono da un modello.
2. Ogni scrittura verso l'esterno richiede consenso esatto del cliente.
3. Si espongono capacità, mai regole.
4. Ogni voce del cervello ha un proprietario e una fonte.
5. Ogni parte dell'azienda ha un livello di dinamicità con il suo motivo.

## E dopo?

Con [Hailmark Connect](https://github.com/hailmark-ai/connect) vai online da solo, nei marketplace dei provider e su Hailmark. Se preferisci che lo facciamo noi, c'è Hailmark Studio.

Licenza: Apache 2.0 per il codice, CC BY 4.0 per i testi (vedi LICENSE e LICENSE-TESTI.md).
