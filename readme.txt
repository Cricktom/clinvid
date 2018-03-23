This project is hosted using flask server. So to run the server type:
"python clinvid.py"

for parsing the string call api converter by sending a post request.
Example to call api converter:

"curl -d '["profile|73241234|<Niharika><><Khan>|<Mumbai><<72.872075><19.075606>>|73241234.jpg**followers|54543343|<Amitabh><><>|<Dehradun><<><>>|54543343.jpg@@|22112211|<Piyush><><>||"]' -H "Content-Type: application/json" -X POST http://localhost:7080/clinvid/app/converter"
