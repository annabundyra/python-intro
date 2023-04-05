
Simple application to book a hotel

| Functinality              | Endpoint                          | Params                                                                                                                                     |
|---------------------------|-----------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------|
| Get all bookings          | GET /bookings                     | None                                                                                                                                       |
| View a specific booking   | GET /bookings/<int:booking_id>    | url_path_parameter:<br/>booking_id                                                                                                         |
| Add a booking             | POST /bookings                    | Request body:<br/> {"guest_name": String, "arrival_date": "YYYY-MM-DD","departure_date":"YYYY-MM-DD"}                                      |
| edit a specific booking   | PUT /bookings/<int:booking_id>    | url_path_parameter: booking_id <br/> Request Body<br/>  {"guest_name": String, "arrival_date": "YYYY-MM-DD","departure_date":"YYYY-MM-DD"} |
| Delete a specific booking | DELETE /bookings/<int:booking_id> | url_path_parameter:<br/>booking_id                                                                                                         |
