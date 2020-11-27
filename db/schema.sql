Customer:
DROP TABLE IF EXISTS `Customer`;
CREATE TABLE `customer` (
  `Customer_ID` int NOT NULL AUTO_INCREMENT,
  `FirstName` varchar(45) NOT NULL,
  `LastName` varchar(45) NOT NULL,
  `Age` int NOT NULL,
  `PhoneNo` varchar(12) NOT NULL,
  `Email` varchar(45) NOT NULL,
  `StreetAddress` varchar(45) NOT NULL,
  `City` varchar(45) NOT NULL,
  `Province` varchar(45) NOT NULL,
  `PostalCode` varchar(45) NOT NULL,
  `DriversID` varchar(45) NOT NULL,
  `Password` varchar(45) NOT NULL,
  PRIMARY KEY (`Customer_ID`)
) ENGINE=InnoDB AUTO_INCREMENT=13 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

Car:
DROP TABLE IF EXISTS `Car`;
CREATE TABLE `car` (
  `ReservationID` int NOT NULL AUTO_INCREMENT,
  `Make` varchar(45) NOT NULL,
  `Model` varchar(45) NOT NULL,
  `Year` varchar(45) NOT NULL,
  `SeatingCapacity` int NOT NULL,
  `Transmission` varchar(45) NOT NULL,
  `Color` varchar(45) NOT NULL,
  PRIMARY KEY (`ReservationID`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

Deals:
DROP TABLE IF EXISTS `Deals`;
CREATE TABLE `deals` (
  `DealName` varchar(45) COLLATE utf8_bin NOT NULL,
  `DealType` varchar(45) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  `ExpiryDate` varchar(45) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  `ReservationID` int NOT NULL,
  PRIMARY KEY (`DealName`,`ReservationID`),
  KEY `Reserve_ID_idx` (`ReservationID`),
  CONSTRAINT `Reserve_ID` FOREIGN KEY (`ReservationID`) REFERENCES `reservation` (`Reservation_ID`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_bin;

Payment:
DROP TABLE IF EXISTS `Payment`;
CREATE TABLE `payment` (
  `PaymentType` varchar(45) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  `LateFee` double NOT NULL,
  `Date` date NOT NULL,
  `TotalAmount` double NOT NULL,
  `Customer_ID` int NOT NULL AUTO_INCREMENT,
  `CardHolderName` varchar(45) COLLATE utf8_bin NOT NULL,
  `CardNumber` varchar(45) COLLATE utf8_bin NOT NULL,
  `cvv` int NOT NULL,
  KEY `Customer_ID_idx` (`Customer_ID`),
  CONSTRAINT `Customer_ID` FOREIGN KEY (`Customer_ID`) REFERENCES `customer` (`Customer_ID`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB AUTO_INCREMENT=8 DEFAULT CHARSET=utf8 COLLATE=utf8_bin;

pick up:
DROP TABLE IF EXISTS `pick up`;
CREATE TABLE `pick_up` (
  `P_Address` varchar(45) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  `City` varchar(45) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  `Province` varchar(45) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  `Postal_Code` varchar(45) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_bin;

Reservation:
DROP TABLE IF EXISTS `Reservation`;
CREATE TABLE `reservation` (
  `Reservation_ID` int NOT NULL AUTO_INCREMENT,
  `ReserveTo` date DEFAULT NULL,
  `ReserveFrom` date DEFAULT NULL,
  `Insurance` varchar(45) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci DEFAULT NULL,
  `CustomerID` int DEFAULT NULL,
  PRIMARY KEY (`Reservation_ID`),
  KEY `Cust_ID_idx` (`CustomerID`)
) ENGINE=InnoDB AUTO_INCREMENT=21 DEFAULT CHARSET=utf8 COLLATE=utf8_bin;
