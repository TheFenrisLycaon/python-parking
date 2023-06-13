# Mercuralia

Parking and Ticketing system.

- Need to be able to book a spot
- Pay for the spot
- Cancel thre reservation
- Three types of spots :
  - Compact
  - Regular
  - Large
- Payments based on time and type of vehicle.
- Can be handled by third party

## Public Endpoints

- reserve
  - param :
    - garage_id
    - start_time
    - end_time
  - returns :
    - spot_id
    - reservation_id

- cancel
  - param :
    - reservation_id

## Private Endpoints

- book (internal)
  - param :
    - garage_id
    - vehicle_type
    - time
  - returns :
    - BOOL { True | False }

- freespots (internal)
  - params :
    - garage_id
    - vehicle_type
    - time
  - returns :
    - list of spots with spot_id
  - note :
    - Smaller vehicles can fit into larger spots

- payment (internal)
  - param
    - reservation_id
  - returns :
    - amount

- create_account
  - param :
    - email
    - password
    - first_name
    - last_name
  - Note :
    - could also integrate 3rd party

- login
  - params :
    - email
    - password
