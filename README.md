Role Based Access Control
===================================
Djnago sample repo for RBAC. Includes
- Django Models Abstraction 
- Rest API using tastypie
- Access token based authorization

Resources
=========
- curl --dump-header -H "Accept: application/json" -H "Content-type: application/json" -X POST --data '{"group_name":"ITC", "create_date":"12/05/2014", "is_billed":"True"}' http://localhost:8000/api/group/?format=json

- curl --dump-header -H "Accept: application/json" -H "Content-type: application/json" -X POST --data '{"hotel_name":"ITC BLR","hotel_city":"Bangalore","hotel_region":"South", "create_date":"12/05/2014", "pricing_plan":"Basic", "group_id":"/api/group/1/"}' http://localhost:8000/api/hotel/?format=json

- curl --dump-header -H "Accept: application/json" -H "Content-type: application/json" -X POST --data '{"user_first_name":"Chetan", "user_last_name":"Giridhar", "create_date":"12/05/2014", "hotel_id":"/api/hotel/1/", "user_access_id":"1"}' http://localhost:8000/api/user/?format=json 

- curl --dump-header -H "Accept: application/json" -H "Content-type: application/json" -X PUT --data '{"user_type":"marketingrole"}' http://localhost:8000/api/user_access/2/?format=json

- curl --dump-header -H "Accept: application/json" -H "Content-type: application/json" -X POST --data '{"user_type":"marketingrole", "user_access":"2"}' http://localhost:8000/api/user_access/?format=json

- GET http://127.0.0.1:8000/api/room_rates/?access_token=1&format=json [Broswer]

- GET http://127.0.0.1:8000/api/myauth/token/?user=9&format=json [Broswer]
