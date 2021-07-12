# Recruitment For Intern 07-2021.
### Mariusz Rogawski

---
## Logger

---

### Główne informacje

Logger to program, który zapisuje domyślnie wszystkie wywołane zdarzenia do plików o rozszerzeniach:
 * .json
 * .csv
 * .sqlite
 * .txt

Zapisane logi w plikach można odczytać według określonych metod:
* Szukanie logów poprzez tekst, który zawierają wiadomości logów
* Szukanie logów poprzez dopasowanie tekstu z wiadomości loga do wzorca wyrażenia regularnego
* Grupowanie logów według ich poziomu
* Grupowanie logów wedługo miesiąca ich utworzenia

Dodatkowo w każdej z powyższych metod można wpisać zakres dat dla których należy wyświetlić logi.

---

### Instalacja

Logger można zainstalować z githuba, z terminala za pomoca polecenia

    $ pip install git+https://github.com/Mairon88/Recruitment_task_backend_internship_2021_07.git#egg=logmaster

Github poprosi o wprowadzenie loginu i hasła do konta na githubie zanim biblioteka zostanie zainstalowana.

### Jak korzystać? 

Po zainstalowaniu biblioteki u siebie w projekcie, aby swobodnie korzystać z jej funkcjonalności należy zaimportować 
odpowiednie moduły tak jak pokazano poniżej:

    from Recruitment_task_backend_internship_2021_07.handlers import JsonHandler, CSVHandler, SQLLiteHandler, FileHandler
    from Recruitment_task_backend_internship_2021_07.profil_logger import ProfilLogger
    from Recruitment_task_backend_internship_2021_07.profil_logger_reader import ProfilLoggerReader

Następnie należy utworzyć handlery do zapisu i odczytu plików w interesująym nas formacie jak pokazano poniżej:

    json_handler = JsonHandler("logs.json")
    csv_handler = CSVHandler("logs.csv")
    sql_handler = SQLLiteHandler("logs.sqlite")
    file_handler = FileHandler("logs.txt")


W przykładzie handlery zostały zapisane w liście i przekazane jako parametr do klasy ProfilLogger.

    handlers = [json_handler, csv_handler, sql_handler, file_handler]
    logger = ProfilLogger(handlers)

Za pomocą obiektu logger i metod jakie mamy do dyspozycji możemy:
* ustawić minimalny poziom loga, od którego nastąpi zapis do pliku (poziomy od najniższego do najwyższego -> 'DEBUG', 'INFO', 'WARNING', 'ERROR', 'CRITICAL' )
  
        logger.set_log_level('DEBUG')

* wywołać log do zapisu, poniżej przedastawiono wywołanie logów dla każdego poziomu
    
        logger.info("Some info message")
        logger.warning("Some warning message")
        logger.debug("Some debug message")
        logger.critical("Some critical message")
        logger.error("Some error message")
  
    powyższe wywołanie zapisuje logi do każdego pliku wskazanego przez handlery

Odczyt logów z plików umożliwia klasa ProfilLoggerReader, która jako parametr przyjmuje odpowiedniego handlera.

    log_reader_json = ProfilLoggerReader(handler=json_handler)
    log_reader_csv = ProfilLoggerReader(handler=csv_handler)
    log_reader_sqlite = ProfilLoggerReader(handler=sql_handler)
    log_reader_txt = ProfilLoggerReader(handler=file_handler)

Stworzone powyżej obiekty przechowują odczytane dane z polików w postaci listy.

Do wyświetlenia odpowiednich logów, powyższe obiekty posiadają metody:

* find_by_text
    
    metoda ta szuka logów poprzez tekst, który zawierają wiadomości logów

        log_reader_json.find_by_text("info",'07-07-2021 16:00:00','07-08-2021 22:20:00')

    Jako pierwszy argument należy podać tekst -> str, który zostanie wyszukany w utworzonych logach oraz opcjonalnie daty
    w formacie jak pokazano w powyższym fragmencie.
  

* find_by_regex
    
    metoda ta szuka logów poprzez dopasowanie tekstu z wiadomości loga do wzorca wyrażenia regularnego

        log_reader_json.find_by_regex(r"\w\w\w\w \w\w\w\w ", '07-07-2021 16:00:00','07-08-2021 22:20:00')

    Jako pierwszy argument należy podać regex -> str, który zostanie wyszukany w utworzonych logach oraz opcjonalnie daty
    w formacie jak pokazano w powyższym fragmencie.
    

* groupby_level
    
  metoda ta grupuje logi według ich poziomu

        log_reader_json.groupby_level('07-01-2021 16:00:00','07-12-2021 22:20:00')

    opcjonalnie jako argumenty można podać daty w formacie jak pokazano w powyższym fragmencie.
    

* groupby_month
metoda ta grupuje logi według miesiąca ,w którym został utworzony log w postaci słownika

        log_reader_json.groupby_level('07-01-2021 16:00:00','07-12-2021 22:20:00')

    opcjonalnie jako argumenty można podać daty w formacie jak pokazano w powyższym fragmencie.


### Przykładowe użycia.

Zapisane dane zgodnie z poniższym fragmentem

      json_handler = JsonHandler("logs.json")
      csv_handler = CSVHandler("logs.csv")
      sql_handler = SQLLiteHandler("logs.sqlite")
      file_handler = FileHandler("logs.txt")
      
      handlers = [json_handler, csv_handler, sql_handler, file_handler]
      logger = ProfilLogger(handlers)
  
      logger.set_log_level('WARNING')
      logger.info("Some info message")
      logger.warning("Some warning message")
      logger.debug("Some debug message")
      logger.critical("Some critical message")
      logger.error("Some error message")

  Powodują powstanie następujących plików

![Alt text](github_img/rys_1.png)

, które zgodnie z ustawioną wartością w set_log_level powinny zawierać
  logi od poziomu WARNING.

![Alt text](github_img/rys2.png)

Odczyt plików za pomocą poniższych metod 

    log_reader_csv = ProfilLoggerReader(handler=csv_handler)
    log_reader_csv.find_by_text("ing me", '10-07-2021 00:00:00','07-08-2021 22:20:00') 
    log_reader_csv.find_by_regex(r"\w\w\w\w e", '07-07-2021 00:00:00','10-08-2021 22:20:00')
    log_reader_csv.groupby_level('07-01-2021 16:00:00','07-12-2021 22:20:00')
    log_reader_csv.groupby_month('07-01-2021 16:00:00','07-12-2021 22:20:00')

spowoduje wyświetlenie listy logów

![Alt text](github_img/rys_3.png)

![Alt text](github_img/rys_5.png)

![Alt text](github_img/rys_4.png)

![Alt text](github_img/rys_6.png)

Niepoprawne wpisanie daty, np. data końcowa jest wcześniejsza od początkowej 

    log_reader_csv.groupby_month('07-12-2021 22:20:00','07-01-2021 00:00:00')

spowoduje pojawienie się komunikatu

    WARNING: Start date should be earlier than end date



