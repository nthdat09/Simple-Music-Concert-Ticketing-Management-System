CREATE DATABASE dbms_py;
USE dbms_py;

create table PARTNER
(
    PTN_ID   decimal     not null
        primary key,
    PTN_NAME  varchar(30) null,
    PTN_PHONE_NUMBER varchar(30) null,
    PTN_EMAIL varchar(30) null,
    PTN_ADDRESS varchar(100)	null,
    PTN_LOGO varchar(150) null, 
    PTN_ACC_NUMBER varchar(30) null,
    PTN_BANK varchar(30) null
);

create table EMPLOYEE
(
    EMP_USERNAME   varchar(30) not null
        primary key,
    EMP_PASSWORD   varchar(30) null,
    EMP_EMAIL      varchar(30) null,
    EMP_PHONE_NUMBER        varchar(20) null,
    EMP_DOB   date	null,
    EMP_ADDRESS     varchar(100) null,
    EMP_AVATAR	varchar(150) null
);

create table ARTIST
(
    ART_ID       decimal     not null
				primary key,
    ART_NAME       varchar(30) null,
    ART_STAGE_NAME  varchar(30) null,
    ART_DOB  date        null,
    ART_DESCRIPTION		text	null,
    ART_PTN_ID decimal     null,
    constraint FK_ART_PTN
        foreign key (ART_PTN_ID) references PARTNER (PTN_ID)
);

create table CUSTOMER
(
	CUS_ID	decimal		not null	primary key,
	CUS_NAME  varchar(30) null,
    CUS_PHONE_NUMBER varchar(30) null,
    CUS_EMAIL varchar(40) null,
    CUS_ADDRESS varchar(100)	null,
    CUS_TYPE varchar (30)	null,
    CUS_TOTAL_POINT	decimal null
    
    CONSTRAINT CHECK_TYPE CHECK (CUS_TYPE = 'REGULAR' OR CUS_TYPE = 'VIP')
);

create table STAGE
(
    STG_ID         decimal     not null
        primary key,
    STG_NAME        varchar(30) null,
    STG_ADDRESS     varchar(100) null,
    STG_RENTAL_PRICE    decimal     null,
    STG_CAPACITY    decimal null,
    STG_OPEN_TIME   time null,
    STG_CLOSE_TIME	time null
);

create table EVENT
(
    EVT_ID         decimal     not null
        primary key,
    EVT_NAME        varchar(30) null,
    EVT_STG_ID       decimal     null,
    EVT_ART_ID       decimal     null,
    EVT_DATE 		 date    null,
    EVT_OPEN_TIME  time   null,
    EVT_END_TIME	time   null,
    EVT_QUANTITY    decimal     null,
    EVT_DESCRIPTION		text   null,
    constraint FK_EVT_ART
        foreign key (EVT_ART_ID) references ARTIST (ART_ID),
    constraint FK_EVT_STG
        foreign key (EVT_STG_ID) references STAGE (STG_ID)
);

create table SEAT
(
    SEAT_ID      decimal     not null,
    SEAT_TYPE     varchar(10) null,
    SEAT_STG_ID	    decimal    not null,
    primary key (SEAT_ID, SEAT_STG_ID),
    constraint FK_SEAT_STG
        foreign key (SEAT_STG_ID) references STAGE (STG_ID)
);

create table RESERVED_SEAT
(
    RSV_CUS_ID	 decimal  not null,
    RSV_SEAT_ID   decimal     not null,
    RSV_STG_ID     decimal     not null,
    RSV_EVT_ID     decimal     not null,
    primary key (RSV_CUS_ID, RSV_SEAT_ID, RSV_STG_ID, RSV_EVT_ID),
    constraint FK_RSV_EVT
        foreign key (RSV_EVT_ID) references EVENT (EVT_ID),
    constraint FK_RSV_SEAT
        foreign key (RSV_SEAT_ID, RSV_STG_ID) references SEAT (SEAT_ID, SEAT_STG_ID),
    constraint FK_RSV_CUS
        foreign key (RSV_CUS_ID) references CUSTOMER (CUS_ID)
);

create table TICKET
(
    TKT_ID          decimal not null
		primary key,
	TKT_EVT_ID	 decimal not null,
    TKT_PRICE      decimal null,
    TKT_STG_ID		decimal null,
    TKT_SEAT_ID      decimal not null,
	constraint FK_TKT_EVT
        foreign key (TKT_EVT_ID) references EVENT (EVT_ID),
    constraint FK_TKT_SEAT
        foreign key (TKT_SEAT_ID, TKT_STG_ID) references SEAT (SEAT_ID, SEAT_STG_ID)
);

create table TICKET_BOOKING
(
    TBK_TKT_ID		decimal not null,
    TBK_CUS_ID		decimal not null,
	TBK_DATETIME	date    null,
	TBT_POINT decimal null,
	primary key (TBK_TKT_ID, TBK_CUS_ID),
    constraint FK_TBK_TKT
		foreign key (TBK_TKT_ID) references TICKET (TKT_ID),
	constraint FK_TBK_CUS
		foreign key (TBK_CUS_ID) references CUSTOMER (CUS_ID)
);

-- ========================== INSERT DATA ========================================

-- INSERT INTO PARTNER
INSERT INTO PARTNER (PTN_ID,PTN_NAME,PTN_PHONE_NUMBER,PTN_EMAIL,PTN_ADDRESS,PTN_LOGO,PTN_ACC_NUMBER,PTN_BANK) VALUES 

(1,'ABC Company','123-456-7890','abc@example.com','123 Main St, Anytown, USA 12345','https://example.com/logo1.jpg','123456789','Bank of Anytown'),
(2,'XYZ Corporation','555-123-4567','xyz@example.com','456 Elm St, Anytown, USA 12345','https://example.com/logo2.png','987654321','Bank of Somewhere'),
(3,'ACME Inc.','111-222-3333','acme@example.com','789 Oak Ave, Anytown, USA 12345','https://example.com/logo3.jpg','111222333','Bank of Anytown'),
(4,'Global Enterprises','444-555-6666','global@example.com','321 Maple St, Anytown, USA 12345','https://example.com/logo4.png','444555666','Bank of Somewhere'),
(5,'ABC Widget Co.','777-888-9999','abcwidget@example.com','111 Crystal St, Anytown, USA 12345','https://example.com/logo5.jpg','777888999','Bank of Anytown'),
(6,'XYZ Services','333-444-5555','xyzservices@example.com','777 Oz Rd, Anytown, USA 12345','https://example.com/logo6.png','333444555','Bank of Somewhere'),
(7,'ACME Products','666-777-8888','acmeproducts@example.com','555 Snowflake Dr, Anytown, USA 12345','https://example.com/logo7.jpg','666777888','Bank of Anytown'),
(8,'Global Solutions','222-333-4444','globalsolutions@example.com','999 Spooky Ln, Anytown, USA 12345','https://example.com/logo8.png','222333444','Bank of Somewhere'),
(9,'ABC Industries','888-999-0000','abcindustries@example.com','888 Gold St, Anytown, USA 12345','https://example.com/logo9.jpg','888999000','Bank of Anytown'),
(10,'XYZ Technologies','444-555-6666','xyztech@example.com','444 Galaxy Blvd, Anytown, USA 12345','https://example.com/logo10.png','444555666','Bank of Somewhere');


-- INSERT INTO EMPLOYEE
INSERT INTO EMPLOYEE (EMP_USERNAME,EMP_PASSWORD,EMP_EMAIL,EMP_PHONE_NUMBER,EMP_DOB,EMP_ADDRESS,EMP_AVATAR) VALUES 

('johnsmith','password','john.smith@example.com','123-456-7890','1980-01-01','123 Main St, Anytown, USA 12345','https://example.com/avatar1.jpg'),
('janesmith','password','jane.smith@example.com','555-123-4567','1985-05-05','456 Elm St, Anytown, USA 12345','https://example.com/avatar2.jpg'),
('bobdylan','password','bob.dylan@example.com','111-222-3333','1970-12-12','789 Oak Ave, Anytown, USA 12345','https://example.com/avatar3.jpg'),
('alicecooper','password','alice.cooper@example.com','444-555-6666','1975-06-15','321 Maple St, Anytown, USA 12345','https://example.com/avatar4.jpg'),
('michaeljackson','password','michael.jackson@example.com','777-888-9999','1980-10-29','111 Crystal St, Anytown, USA 12345','https://example.com/avatar5.jpg'),
('janisjoplin','password','janis.joplin@example.com','333-444-5555','1971-03-08','777 Oz Rd, Anytown, USA 12345','https://example.com/avatar6.jpg'),
('jimihendrix','password','jimi.hendrix@example.com','666-777-8888','1972-11-27','555 Snowflake Dr, Anytown, USA 12345','https://example.com/avatar7.jpg'),
('elvispresley','password','elvis.presley@example.com','222-333-4444','1976-08-16','999 Spooky Ln, Anytown, USA 12345','https://example.com/avatar8.jpg'),
('prince','password','prince@example.com','888-999-0000','1982-06-07','888 Gold St, Anytown, USA 12345','https://example.com/avatar9.jpg'),
('davidbowie','password','david.bowie@example.com','444-555-6666','1977-01-08','444 Galaxy Blvd, Anytown, USA 12345','https://example.com/avatar10.jpg');


-- INSERT INTO ARTIST
INSERT INTO ARTIST(ART_ID,ART_NAME,ART_STAGE_NAME,ART_DOB,ART_DESCRIPTION,ART_PTN_ID) VALUES 

(1,'John Smith','The Singer','1975-01-01','A talented singer with a soulful voice.','1'),
(2,'Jane Doe','The Songwriter','1980-05-05','A prolific songwriter with a unique style.','2'),
(3,'Bob Dylan','The Legend','1941-05-24','A seminal figure in American music.','1'),
(4,'Alice Cooper','The Shock Rocker','1948-02-04','A theatrical performer known for his outlandish style.','3'),
(5,'Michael Jackson','The King of Pop','1958-08-29','A pop icon and one of the most successful musicians of all time.','1'),
(6,'Janis Joplin','The Queen of Rock and Roll','1943-01-19','A powerful singer known for her bluesy, soulful voice.','2'),
(7,'Jimi Hendrix','The Guitar God','1942-11-27','One of the most influential guitarists in the history of rock music.','3'),
(8,'Elvis Presley','The King of Rock and Roll','1935-01-08','A cultural icon and one of the most celebrated musicians of the 20th century.','1'),
(9,'Prince','The Purple One','1958-06-07','An enigmatic and prolific musician known for his musical virtuosity.','2'),
(10,'David Bowie','The Starman','1947-01-08','A visionary artist who constantly reinvented himself.','3');

 
 -- INSERT INTO CUSTOMER
INSERT INTO CUSTOMER (CUS_ID,CUS_NAME,CUS_PHONE_NUMBER,CUS_EMAIL,CUS_ADDRESS,CUS_TYPE,CUS_TOTAL_POINT) VALUES 

(1,'John Smith','123-456-7890','john.smith@example.com','123 Main St, Anytown, USA 12345','Regular','100'),
(2,'Jane Doe','555-123-4567','jane.doe@example.com','456 Elm St, Anytown, USA 12345','VIP','500'),
(3,'Bob Dylan','111-222-3333','bob.dylan@example.com','789 Oak Ave, Anytown, USA 12345','Regular','50'),
(4,'Alice Cooper','444-555-6666','alice.cooper@example.com','321 Maple St, Anytown, USA 12345','VIP','750'),
(5,'Michael Jackson','777-888-9999','michael.jackson@example.com','111 Crystal St, Anytown, USA 12345','Regular','200'),
(6,'Janis Joplin','333-444-5555','janis.joplin@example.com','777 Oz Rd, Anytown, USA 12345','VIP','1000'),
(7,'Jimi Hendrix','666-777-8888','jimi.hendrix@example.com','555 Snowflake Dr, Anytown, USA 12345','Regular','75'),
(8,'Elvis Presley','222-333-4444','elvis.presley@example.com','999 Spooky Ln, Anytown, USA 12345','VIP','1200'),
(9,'Prince','888-999-0000','prince@example.com','888 Gold St, Anytown, USA 12345','Regular','150'),
(10,'David Bowie','444-555-6666','david.bowie@example.com','444 Galaxy Blvd, Anytown, USA 12345','VIP','900');

-- INSERT INTO STAGE
INSERT INTO STAGE (STG_ID,STG_NAME,STG_ADDRESS,STG_RENTAL_PRICE,STG_CAPACITY,STG_OPEN_TIME,STG_CLOSE_TIME) VALUES 

(1,'The Grand Ballroom','123 Main St, Suite 100, Anytown, USA 12345',5000.00,500,'08:00:00','23:00:00'),
(2,'The Secret Garden','456 Elm St, Anytown, USA 12345',2500.00,250,'10:00:00','21:00:00'),
(3,'The Majestic Theater','789 Oak Ave, Anytown, USA 12345',7500.00,750,'09:00:00','22:00:00'),
(4,'The Enchanted Forest','321 Maple St, Anytown, USA 12345',1000.00,100,'12:00:00','18:00:00'),
(5,'The Crystal Palace','111 Crystal St, Anytown, USA 12345',10000.00,1000,'10:00:00','23:00:00'),
(6,'The Emerald City','777 Oz Rd, Anytown, USA 12345',5000.00,500,'11:00:00','22:00:00'),
(7,'The Winter Wonderland','555 Snowflake Dr, Anytown, USA 12345',2000.00,200,'13:00:00','20:00:00'),
(8,'The Haunted Mansion','999 Spooky Ln, Anytown, USA 12345',5000.00,500,'18:00:00','01:00:00'),
(9,'The Golden Palace','888 Gold St, Anytown, USA 12345',7500.00,750,'12:00:00','23:00:00'),
(10,'The Starry Night','444 Galaxy Blvd, Anytown, USA 12345',3000.00,300,'19:00:00','02:00:00');


-- INSERT INTO EVENT
INSERT INTO EVENT (EVT_ID, EVT_NAME, EVT_STG_ID, EVT_ART_ID, EVT_DATE, EVT_OPEN_TIME, EVT_END_TIME, EVT_QUANTITY, EVT_DESCRIPTION) VALUES 

(1,'Concert in the Park',1,2,'2023-05-01','18:00:00','20:00:00',100,'A free concert featuring local artists.'),
(2,'Summer Music Festival',2,5,'2023-07-15','12:00:00','22:00:00',500,'A day-long festival with multiple stages and headlining acts.'),
(3,'Acoustic Night',3,6,'2023-08-05','19:00:00','22:00:00',50,'An intimate night of acoustic music featuring up-and-coming artists.'),
(4,'Jazz Showcase',1,1,'2023-09-01','20:00:00','22:00:00',75,'An evening of jazz music featuring local and regional performers.'),
(5,'Rock the City',2,3,'2023-06-10','17:00:00','23:00:00',1000,'A large outdoor concert featuring top rock bands from around the country.'),
(6,'Country Jamboree',2,4,'2023-08-22','16:00:00','21:00:00',250,'A celebration of country music featuring local and national acts.'),
(7,'Blues Night',3,7,'2023-10-05','19:00:00','22:00:00',50,'A night of blues music featuring some of the best blues artists around.'),
(8,'Classical Concert',1,8,'2023-11-15','19:30:00','21:30:00',100,'An evening of classical music featuring a chamber orchestra and soloists.'),
(9,'Hip-Hop Showcase',2,10,'2023-07-30','18:00:00','23:00:00',500,'A showcase of hip-hop artists from around the city.'),
(10,'Indie Night',3,9,'2023-09-20','20:00:00','23:00:00',75,'A night of indie music featuring some of the best up-and-coming bands.');


-- INSERT INTO SEAT

INSERT INTO SEAT (SEAT_ID, SEAT_TYPE, SEAT_STG_ID) VALUES 
(1, 'VIP', 1), 
(2, 'Regular', 2),
(3, 'Premium', 3),
(4, 'General', 4),
(5, 'VIP', 5), 
(6, 'Regular', 6),
(7, 'Premium', 7),
(8, 'General', 8),
(9, 'VIP', 9), 
(10, 'Regular', 10);

-- INSERT INTO RESERVED_SEAT
