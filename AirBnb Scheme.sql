CREATE TABLE "users" (
  "id" serial PRIMARY KEY,
  "phone_number" integer NOT NULL,
  "first_name" varchar NOT NULL,
  "last_name" varchar NOT NULL,
  "email" varchar NOT NULL,
  "birth_date" date NOT NULL,
  "password" varchar NOT NULL,
  "country_id" integer NOT NULL,
  "created_at" timestamp DEFAULT (now()),
  "deleted" bool NOT NULL DEFAULT False
);

CREATE TABLE "hosts" (
  "id" integer NOT NULL PRIMARY KEY,
  "deleted" bool NOT NULL DEFAULT False
);

CREATE TABLE "guests" (
  "id" integer NOT NULL PRIMARY KEY,
  "deleted" bool NOT NULL DEFAULT False
);

CREATE TABLE "countries" (
  "id" serial PRIMARY KEY,
  "name" varchar NOT NULL,
  "country_code" varchar NOT NULL
);

CREATE TABLE "cities" (
  "id" serial PRIMARY KEY,
  "name" varchar NOT NULL,
  "country_id" integer NOT NULL
);

CREATE TABLE "rooms" (
  "id" serial PRIMARY KEY,
  "amount_of_residence" integer,
  "is_air_condition" bool NOT NULL DEFAULT True,
  "is_fridge" bool NOT NULL DEFAULT True,
  "price_per_day" decimal NOT NULL,
  "host_id" integer NOT NULL,
  "allow_animals" bool NOT NULL DEFAULT True,
  "allow_infants" bool NOT NULL DEFAULT True,
  "city_id" integer NOT NULL,
  "deleted" bool NOT NULL DEFAULT False
);

CREATE TABLE "reservations" (
  "id" serial PRIMARY KEY,
  "room_id" integer NOT NULL,
  "guest_id" integer NOT NULL,
  "date_from" date NOT NULL,
  "date_to" date NOT NULL,
  "count_of_adults" integer DEFAULT 1,
  "count_of_children" integer DEFAULT 0,
  "count_of_infants" integer DEFAULT 0,
  "with_animals" bool DEFAULT False,
  "price" decimal NOT NULL,
  "estimation" integer DEFAULT 0,
  "text_rewiew" varchar,
  "payed" bool NOT NULL DEFAULT False,
  "cancelled" bool NOT NULL DEFAULT False
);

ALTER TABLE "users" ADD FOREIGN KEY ("country_id") REFERENCES "countries" ("id");

ALTER TABLE "hosts" ADD FOREIGN KEY ("id") REFERENCES "users" ("id");

ALTER TABLE "guests" ADD FOREIGN KEY ("id") REFERENCES "users" ("id");

ALTER TABLE "cities" ADD FOREIGN KEY ("country_id") REFERENCES "countries" ("id");

ALTER TABLE "rooms" ADD FOREIGN KEY ("host_id") REFERENCES "hosts" ("id");

ALTER TABLE "rooms" ADD FOREIGN KEY ("city_id") REFERENCES "cities" ("id");

ALTER TABLE "reservations" ADD FOREIGN KEY ("room_id") REFERENCES "rooms" ("id");

ALTER TABLE "reservations" ADD FOREIGN KEY ("guest_id") REFERENCES "guests" ("id");

INSERT INTO 
	countries 
	(name, country_code) 
	VALUES 
	('Ukraine', '+380'), 
	('Poland', '+48'), 
	('United Kingdom', '+44');
	
INSERT INTO 
	cities
	(name, country_id)
	VALUES
	('Kyiv', 1),  
	('Sevastopol', 1), 
	('London', 3);
	
INSERT INTO users
	(phone_number, first_name, last_name, email, birth_date, password, country_id)
	VALUES 
	('667109999', 'Olga', 'Levchenko', 'olga.levch@gmail.com', TO_DATE('19971127', 'YYYYMMDD'), 'password', 1),
	('667109998', 'Inna', 'Obadina', 'inna.obadina@gmail.com', TO_DATE('2001001', 'YYYYMMDD'), 'password', 1),
	('667109997', 'Sergey', 'Miroshnichenko', 'serg.mir@gmail.com', TO_DATE('19850112', 'YYYYMMDD'), 'password', 1),
	('667109996', 'Anton', 'Listopad', 'anton@gmail.com', TO_DATE('19850112', 'YYYYMMDD'), 'password', 1),
	('667109995', 'Katya', 'Alekseeva', 'katya@gmail.com', TO_DATE('19850112', 'YYYYMMDD'), 'password', 1);
	
INSERT INTO
	guests
	(id)
VALUES
	(1), (2);

INSERT INTO 
	hosts
	(id)
VALUES
	(3), (4), (5);
	
INSERT INTO 
	rooms
	(amount_of_residence, is_air_condition, is_fridge, price_per_day, host_id, city_id)
	VALUES 
	(3, True, False, 200, 3, 1),
	(1, False, False, 100, 4, 1),
	(2, True, True, 500, 5, 1);
	
INSERT INTO 
	reservations
	(room_id, guest_id, date_from, date_to, price, estimation, text_rewiew, payed)
	VALUES 
	(1, 1, TO_DATE('20230521', 'YYYYMMDD'), TO_DATE('20230527', 'YYYYMMDD'), 1200, 5, 'Perfect apartment with beautiful view', True),
	(2, 1, TO_DATE('20230521', 'YYYYMMDD'), TO_DATE('20230527', 'YYYYMMDD'), 600, 5, 'Perfect apartment with beautiful view', True),
	(3, 1, TO_DATE('20230521', 'YYYYMMDD'), TO_DATE('20230527', 'YYYYMMDD'), 3000, 5, 'Perfect apartment with beautiful view', True),
	(1, 1, TO_DATE('20230601', 'YYYYMMDD'), TO_DATE('20230603', 'YYYYMMDD'), 400, NULL, NULL, False),
	(1, 2, TO_DATE('20230604', 'YYYYMMDD'), TO_DATE('20230605', 'YYYYMMDD'), 200, NULL, NULL, False);
	

/*Find a user who had biggest amount of reservation. Return user name and user_id*/
SELECT 
	u.id, u.last_name || ' ' || u.first_name as name
FROM users u 
WHERE u.id IN 
(SELECT 
	t.guest_id 
FROM 
(SELECT 
	COUNT(r.id) as c, r.guest_id
FROM reservations r
GROUP BY r.guest_id
ORDER BY c DESC
LIMIT 1) as t)
	
	
/*Find a host who earned biggest amount of money for the last month. Return host name and host_id*/
SELECT h.id, u.last_name || ' ' || u.first_name
FROM hosts h
INNER JOIN users u on h.id = u.id
INNER JOIN 
(
	SELECT rm.host_id, SUM(rs.price) AS price
	FROM Reservations rs
	INNER JOIN Rooms rm ON rs.room_id = rm.id
	WHERE rs.date_from >= (now() - interval '1 month')
	GROUP BY rm.host_id
) payments ON h.id = payments.host_id
ORDER BY payments.price desc
LIMIT 1	
	
	
/*Find a host with best average rating. Return host name and host_id*/	
SELECT h.id AS host_id, u.last_name || ' ' || u.first_name as host_name, AVG(r.estimation) AS average_rating
FROM hosts h
JOIN users u ON h.id = u.id
JOIN rooms rm ON h.id = rm.host_id
JOIN reservations r ON rm.id = r.room_id
WHERE r.estimation IS NOT NULL
GROUP BY h.id, host_name
ORDER BY average_rating DESC
LIMIT 1;	