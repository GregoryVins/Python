Бот работает с криптовалютной площадкой Binance (https://binance.com/)
Работа происходит через API keys (https://api.binance.com/)

Необходимо записать KEY и SECRET KEY в текстовый файл API.txt, который располагается в корневом каталоге.
Первой строкой должен быть записал KEY, без пробелов
Второй строкой должен быть записал SECRET KEY, без пробелов
Пример:
XUXp1IEL1e8xK78lqBdTRfiY7ZdsA8npeA5SlJ5bwbQo6ooUVEsLOmpcTFf9aaqw
KJdf98LMi4FFldlkfndKJNF94FLKflkdf8dslfmsdNF9dflmdfdfdFK8dfda7Fdd


Бот содержит 3 модуля, binance_api.py, history_request.py и macd_strategy.py

binance_api.py - отвечает за соединение и запросы.
history_request.py - отвечает за выгрузку истории через предоставленные API в файл history.json
macd_strategy.py - считывает историю из файла history.json и на его основе создаёт файл result.csv с списком сделок
                   за конкретный период времени. Стоит учитывать, что данные файла не перезаписываются, и для
                   сохранения данных нового запроса следует удалить файл result.csv либо отчистить его содержимое.

Программа была написана на Python 3.8.3
