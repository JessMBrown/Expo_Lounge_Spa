CREATE DATABASE Spa;
USE Spa;


CREATE TABLE Employee (
	Employee_ID INT NOT NULL AUTO_INCREMENT,
	Role VARCHAR (40) NOT NULL,
	Salary INT NOT NULL,
	Work_Days VARCHAR (40) NOT NULL,
	Work_Start TIME(0) NOT NULL,
    Work_End TIME(0) NOT NULL,
CONSTRAINT PK_Employee_ID PRIMARY KEY (Employee_ID)
);

CREATE TABLE Treatments (
	Treatment_ID INT NOT NULL AUTO_INCREMENT,
	Treatment_Name VARCHAR (40) NOT NULL,
	Price_Per_Treatment DECIMAL(10,2) NOT NULL,
CONSTRAINT PK_Treatment_ID PRIMARY KEY (Treatment_ID)
);

CREATE TABLE Spa_Booking (
	Spa_Booking_ID INT NOT NULL AUTO_INCREMENT,
	Date_of_Treatment DATE NOT NULL,
	Time_of_Treatment TIME NOT NULL,
	Treatment_ID INT NOT NULL,
	Employee_ID INT NOT NULL,
CONSTRAINT PK_Spa_Booking_ID PRIMARY KEY (Spa_Booking_ID),
CONSTRAINT FK_EmployeeID_SpaBooking FOREIGN KEY (Employee_ID) REFERENCES Employee (Employee_ID),
CONSTRAINT FK_TreatmentID_SpaBooking FOREIGN KEY (Treatment_ID) REFERENCES Treatments (Treatment_ID)
);


INSERT INTO Spa_Booking (Date_of_Treatment, Time_of_Treatment, Treatment_ID, Employee_ID)
VALUES
('2024-06-01', '10:30:00', 1, 2),
('2024-06-01', '13:00:00', 1, 2),
('2024-06-01', '11:30:00', 7, 6),
('2024-06-01', '12:15:00', 8, 6),
('2024-06-01', '11:30:00', 4, 4),
('2024-06-01', '12:15:00', 5, 4),
('2024-06-02', '10:30:00', 1, 1),
('2024-06-02', '13:00:00', 1, 1),
('2024-06-02', '11:30:00', 7, 5),
('2024-06-02', '12:15:00', 8, 5),
('2024-06-02', '11:30:00', 7, 3),
('2024-06-02', '14:15:00', 8, 3),
('2024-06-03', '10:30:00', 1, 1),
('2024-06-03', '13:00:00', 1, 1),
('2024-06-03', '09:30:00', 2, 5),
('2024-06-03', '12:15:00', 5, 5),
('2024-06-03', '10:30:00', 7, 3),
('2024-06-03', '12:45:00', 8, 3),
('2024-06-04', '10:30:00', 1, 2),
('2024-06-04', '13:00:00', 1, 2),
('2024-06-04', '11:30:00', 9, 6),
('2024-06-04', '15:15:00', 10, 6),
('2024-06-04', '10:30:00', 7, 6),
('2024-06-04', '14:00:00', 8, 6),
('2024-06-01', '11:30:00', 6, 1),
('2024-06-01', '12:15:00', 3, 1),
('2024-06-01', '11:30:00', 10, 2),
('2024-06-01', '12:15:00', 9, 2),
('2024-06-01', '11:30:00', 5, 3),
('2024-06-01', '14:15:00', 11, 3),
('2024-06-01', '11:30:00', 4, 4),
('2024-06-01', '12:15:00', 11, 4),
('2024-06-01', '11:30:00', 7, 5),
('2024-06-01', '12:15:00', 8, 5),
('2024-06-01', '11:30:00', 7, 6),
('2024-06-01', '12:15:00', 7, 6)
;

INSERT INTO Employee (Role, Salary, Work_Days, Work_Start, Work_End)
VALUES
('Masseuse', '35000.00', 'MON,TUE,WED,THU,SUN', '09:00:00', '18:00:00'),
('Masseuse', '35000.00', 'TUE,WED,THU,FRI,SAT', '09:00:00', '18:00:00'),
('Beautician', '39000.00', 'MON,TUE,WED,THU,SUN', '09:00:00', '18:00:00'),
('Beautician', '39000.00', 'TUE,WED,THU,FRI,SAT', '09:00:00', '18:00:00'),
('Nail_Technician', '30000.00', 'MON,TUE,WED,THU,SUN', '09:00:00', '18:00:00'),
('Nail_Technician', '30000.00', 'TUE,WED,THU,FRI,SAT', '09:00:00', '18:00:00')
;



INSERT INTO Treatments (Treatment_Name, Price_Per_Treatment)
VALUES
('Body_Massage', 125.00),
('Calming_Facial', 65.00),
('Rejuvenating_Facial', 75.00),
('Lip_Filler', 85.00),
('Chemical_Peel', 105.00),
('Swedish_Massage', 125.00),
('Manicure', 30.00),
('Pedicure', 35.00),
('Back_Neck_And_Shoulder_Massage', 95.00),
('Hot_Stone_Massage', 130.00),
('Spray_Tan', 45.00)
;



-- A Spa has just opened up in a hotel on the 1st June.
-- bookings are going well so far each new member of staff has at least 2 bookings a day
--
