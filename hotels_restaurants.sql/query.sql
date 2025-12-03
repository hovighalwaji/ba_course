SELECT * FROM exploreplaces.restaurants
where delivery_available= '0';

SELECT distinct reaction_type
from review_reactions;

SELECT * FROM exploreplaces.restaurants
where city_id In ('2', '3' );

SELECT * FROM exploreplaces.users
where age between 25 and 35;

SELECT * FROM exploreplaces.reviews
where comment Like 'Great%';

SELECT restaurant_id,comment
 from reviews
where comment like '%cuisine%';

update restaurants
set delivery_available = 0
where restaurant_id = 9;

SELECT * FROM exploreplaces.reviews
where rating >4
AND (YEAR(review_date) = 2025 OR (YEAR(review_date) = 2024 AND MONTH(review_date) = 12))
  AND user_id IN (1, 11); 
  
DELETE FROM review_reactions
where user_id=10;

CREATE TABLE hotels (
    hotel_id INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(100) NOT NULL,
    city_id INT NOT NULL,
    stars INT CHECK (stars >= 1 AND stars <= 5),
    amenities VARCHAR(255),
    address VARCHAR(255),
    FOREIGN KEY (city_id) REFERENCES cities(city_id)
);

INSERT INTO hotels (name, city_id, stars, amenities, address)
VALUES
    ('Meridian', 1, 5, 'Pool, Spa, Gym', 'Amiryan, Yerevan'),
    ('Grand Hotel', 2, 3, 'Wi-Fi, Restaurant, Parking', '45 Baker Street, London');

INSERT INTO hotels (name, city_id, stars, amenities, address)
VALUES
    ('Grand Horizon Hotel', 1, 5, 'Wi-Fi, Gym', ' Park Avenue, New York');
    
update hotels
set city_id = 3
where hotel_id=4;

ALTER TABLE reviews
ADD hotel_id INT;
