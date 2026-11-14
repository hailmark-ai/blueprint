"""Controllo automatico di azienda.json secondo le regole dell'architettura.

Uso:
    python strumenti/verifica.py azienda.json           controllo completo
    python strumenti/verifica.py azienda.json --bozza   solo struttura e regole (passo 1)

Nessuna dipendenza esterna. Esce con codice 1 se trova errori.
"""

from __future__ import annotations

import json
import sys

ARCHETIPI = ("catalogo", "agenda", "contratto", "configurazione", "pratica", "asset")
TIPI_CONOSCENZA = ("fatti", "regole", "processi", "sapere", "identita")
ESPOSIZIONE = ("segreto", "interno", "partner", "cliente", "pubblico")
TIPI_CAPACITA = ("lettura", "calcolo", "scrittura", "consulenza")
ESECUTORI = ("software", "ai", "persona")
LIVELLI = ("dinamico", "ibrido", "statico")
CAMPI = ("id", "nome", "archetipo", "perche", "reparti", "cervello", "capacita",
         "prima_ondata", "mai_ai", "norme")


def regole_architettura(bp: dict) -> list[str]:
    """Le regole dell'architettura Hailmark."""
    errori: list[str] = []
    for campo in CAMPI:
        if not bp.get(campo):
            errori.append(f"campo mancante o vuoto: {campo}")
    if errori:
        return errori
    if bp["archetipo"] not in ARCHETIPI:
        errori.append(f"archetipo sconosciuto: {bp['archetipo']}")
    reparti = set(bp["reparti"])

    for voce in bp["cervello"]:
        etichetta = f"cervello '{voce.get('voce')}'"
        if voce.get("tipo") not in TIPI_CONOSCENZA:
            errori.append(f"{etichetta}: tipo sconosciuto")
        if voce.get("esposizione") not in ESPOSIZIONE:
            errori.append(f"{etichetta}: esposizione sconosciuta")
        if voce.get("proprietario") not in reparti:
            errori.append(f"{etichetta}: il proprietario deve essere un reparto")
        if voce.get("tipo") == "regole" and voce.get("esposizione") in ("cliente", "pubblico"):
            errori.append(f"{etichetta}: si espone la capacità, non la regola")

    nomi = [c.get("nome") for c in bp["capacita"]]
    if len(nomi) != len(set(nomi)):
        errori.append("nomi di capacità duplicati")
    for c in bp["capacita"]:
        etichetta = f"capacità '{c.get('nome')}'"
        tipo, esegue = c.get("tipo"), c.get("esegue")
        if tipo not in TIPI_CAPACITA:
            errori.append(f"{etichetta}: tipo sconosciuto")
        if esegue not in ESECUTORI:
            errori.append(f"{etichetta}: esecutore sconosciuto")
        if c.get("esposizione") not in ESPOSIZIONE[1:]:
            errori.append(f"{etichetta}: esposizione non valida per una capacità")
        if tipo == "scrittura" and c.get("consenso") is not True:
            errori.append(f"{etichetta}: ogni scrittura richiede consenso esatto")
        if tipo != "scrittura" and c.get("consenso") is not False:
            errori.append(f"{etichetta}: il consenso si chiede solo per le scritture")
        if tipo == "scrittura" and esegue == "ai":
            errori.append(f"{etichetta}: un modello non esegue scritture")
        if tipo == "calcolo" and esegue != "software":
            errori.append(f"{etichetta}: prezzi e calcoli li fa il software")
        if esegue == "ai" and tipo != "consulenza":
            errori.append(f"{etichetta}: l'AI dell'azienda fa solo consulenza")
        if tipo == "lettura" and esegue != "software":
            errori.append(f"{etichetta}: le letture vengono dal registro")
    if not any(c.get("esposizione") == "pubblico" for c in bp["capacita"]):
        errori.append("serve almeno una capacità pubblica")
    sconosciute = [n for n in bp["prima_ondata"] if n not in nomi]
    if sconosciute:
        errori.append(f"prima ondata con capacità inesistenti: {', '.join(sconosciute)}")
    return errori


def controlla(azienda: dict, bozza: bool = False) -> list[str]:
    """Regole dell'architettura più quelle del /init: identità, fonti, approvazioni."""
    errori = regole_architettura(azienda)
    info = azienda.get("azienda")
    if not isinstance(info, dict) or not info.get("nome"):
        errori.append("manca il blocco 'azienda' con almeno il nome (passo 1)")
    for voce in azienda.get("cervello", []):
        etichetta = f"cervello '{voce.get('voce')}'"
        if "fonte" not in voce or "approvata" not in voce:
            errori.append(f"{etichetta}: servono i campi 'fonte' e 'approvata' (passo 1)")
            continue
        if bozza:
            continue
        if not str(voce.get("fonte", "")).strip():
            errori.append(f"{etichetta}: fonte vuota (passo 3)")
        if voce.get("approvata") is not True:
            errori.append(f"{etichetta}: non ancora approvata dal proprietario (passo 4)")
    livelli = azienda.get("dinamicita")
    if not livelli:
        if not bozza:
            errori.append("manca la scelta di dinamicità delle parti dell'azienda (passo 1)")
    else:
        for parte in livelli:
            nome = parte.get("parte") if isinstance(parte, dict) else None
            if not isinstance(parte, dict) or not str(nome or "").strip():
                errori.append("dinamicità: ogni voce deve avere una 'parte'")
                continue
            if parte.get("livello") not in LIVELLI:
                errori.append(f"dinamicità '{nome}': il livello deve essere dinamico, ibrido o statico")
            if not str(parte.get("motivo", "")).strip():
                errori.append(f"dinamicità '{nome}': manca il motivo")
    return errori


def main(argv: list[str]) -> int:
    try:
        sys.stdout.reconfigure(encoding="utf-8")
    except (AttributeError, ValueError):
        pass
    if not argv or argv[0].startswith("-"):
        print(__doc__)
        return 2
    bozza = "--bozza" in argv
    try:
        with open(argv[0], encoding="utf-8") as handle:
            azienda = json.load(handle)
    except (OSError, json.JSONDecodeError) as error:
        print(f"Impossibile leggere {argv[0]}: {error}")
        return 1
    errori = controlla(azienda, bozza=bozza)
    if errori:
        print(f"{len(errori)} problemi da risolvere:")
        for errore in errori:
            print(f"  - {errore}")
        return 1
    print("valido" + (" (bozza: fonti e approvazioni non ancora controllate)" if bozza else ""))
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
