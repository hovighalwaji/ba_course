select airplane_type.type_id,
airplane.capacity,
airplane.airplane_id,
airplane_type.identifier,
flight.flightno,
flight.departure,
flight.arrival,
flight.airline_id,
flight.from,
airport.name,
airline.airlinename
from airplane_type
join airplane on airplane.type_id= airplane_type.type_id
cross join flight on flight.airplane_id=airplane.airplane_id
cross join airline on airline.airline_id=flight.airline_id
cross join airport on airport.airport_id=flight.from;