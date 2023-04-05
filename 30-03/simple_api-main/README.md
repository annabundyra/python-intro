# simple_api

| Functionality          | Endpoint                   | Data                                                                                                    |
|------------------------|----------------------------|---------------------------------------------------------------------------------------------------------|
| Add a book             | POST /books                | Request body: <br/>{"isbn":String, "author":String,"title":String, "year":integer}                      |
| Get all books          | GET /books                 | None                                                                                                    |
| Get a specific book    | GET /book/<string:isbn>    | Url_path_parameter:<br/> isbn                                                                           |
| EDIT a specific book   | PUT /book/<string:isbn>    | Url_path_parameter: <br/>isbn <br/> Request body: <br/>{"author":String,"title":String, "year":integer} |
| DELETE a specific book | DELETE /book/<string:isbn> | Url_path_parameter:<br/> isbn <br/>                                                                     |
| DELETE a specific book | DELETE /book/<string:isbn> | Url_path_parameter:<br/> isbn                                                                           |

## how to set up the and run the project

Install flask and requests

```bash
pip install flask requests
```