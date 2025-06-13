
# Predaj cestovných lístkov – Django Aplikácia

---

Táto jednoduchá webová aplikácia, vytvorená v Django, slúži na predaj cestovných lístkov pre registrovaných aj neregistrovaných cestujúcich. Poskytuje komplexnú správu cestujúcich, staníc, cien a zliav, spolu s vystavovaním a evidenciou lístkov.
Ako základ som použil projekt z DS2 - predaj cestovných lístkov

## Funkcie

* **Správa registrovaných pasažierov**: Evidencia mien a typov zliav pre registrovaných používateľov.
* **Predaj lístkov**: Umožňuje predaj lístkov pre **registrovaných aj neregistrovaných** cestujúcich.
* **Výpočet ceny**: Automatický výpočet ceny lístka na základe zvolených zón s možnosťou aplikovania zliav.
* **Zoznam vydaných lístkov**: Prehľadná evidencia všetkých predaných lístkov.
* **Zoznam cestujúcich**: Kompletný zoznam všetkých registrovaných pasažierov.
* **Bootstrap vzhľad**: Moderný dizajn vďaka Bootstrapu.

---

## Inštalácia a Spustenie

1.  **Naklonovanie repozitára**:
    ```bash
    git clone https://github.com/davidjopcik/ticketing_system.git
    ```

2.  **Vytvorenie virtuálneho prostredia**:
    ```bash
    python -m venv venv
    source venv/bin/activate
    ```

3.  **Vytvorenie admin účtu**:
    ```bash
    python manage.py createsuperuser
    ```

4.  **Spustenie servera**:
    ```bash
    python manage.py runserver
    ```
    Aplikácia bude dostupná na:
    http://127.0.0.1:8000/

5. **Prihlásenie sa do admin rozhrania**
    ```bash
    http://127.0.0.1:8000/admin/
    ```
---

## Použitie

Po úspešnom spustení aplikácie môžete:

* **Registrovať nových pasažierov** prostredníctvom hlavného menu.
* V sekcii "**Predaj lístkov**" zvoliť, či ide o **registrovaného alebo neregistrovaného** pasažiera.
* Vybrať **začiatočnú a cieľovú stanicu** a **platnosť** lístka.
* Po potvrdení sa **lístok vygeneruje**, zobrazí sa jeho **cena a detailné informácie**.

### Poznámky

* **Registrovaným pasažierom** sa aplikuje zľava podľa ich kategórie.
* **Neregistrovaným pasažierom** sa zľava neaplikuje.

## Autor
* Meno: Dávid Jopčík
* login: JOP0015