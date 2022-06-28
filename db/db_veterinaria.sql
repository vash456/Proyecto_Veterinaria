-- MySQL dump 10.13  Distrib 8.0.27, for Win64 (x86_64)
--
-- Host: localhost    Database: bd_veterinary
-- ------------------------------------------------------
-- Server version	8.0.27

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `bill`
--

DROP TABLE IF EXISTS `bill`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `bill` (
  `id` int NOT NULL AUTO_INCREMENT,
  `veterinary_name` varchar(45) DEFAULT NULL,
  `customer_name` varchar(45) DEFAULT NULL,
  `service` varchar(45) DEFAULT NULL,
  `total` int DEFAULT NULL,
  `create_at` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `bill`
--

LOCK TABLES `bill` WRITE;
/*!40000 ALTER TABLE `bill` DISABLE KEYS */;
/*!40000 ALTER TABLE `bill` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `customer`
--

DROP TABLE IF EXISTS `customer`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `customer` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(45) NOT NULL,
  `last_name` varchar(45) NOT NULL,
  `cc` varchar(45) NOT NULL,
  `age` varchar(45) NOT NULL,
  `tell` varchar(45) NOT NULL,
  `email` varchar(45) NOT NULL,
  `created_at` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `update_at` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=9 DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `customer`
--

LOCK TABLES `customer` WRITE;
/*!40000 ALTER TABLE `customer` DISABLE KEYS */;
INSERT INTO `customer` VALUES (1,'fulano','garcia','1040123456','33','123456','mail@mail.com','2022-06-27 22:46:31','2022-06-27 22:46:31'),(2,'fulano2','garcia2','1040123456','33','123456','mail@mail.com','2022-06-27 22:46:31','2022-06-27 22:46:31'),(3,'jose','armando','46565','4','45646','correo@gmail.com','2022-06-27 22:46:31','2022-06-27 22:46:31'),(4,'carlos','gonzalo','123487','12','45678','gmail@gmail.com','2022-06-27 22:53:03','2022-06-27 22:53:03'),(5,'oscar','sanchez','4456579','25','132164','correofalso@gmail.com','2022-06-28 00:58:27','2022-06-28 00:58:27'),(6,'julio','perez','5465987','32','216564','correo123245@gmail.com','2022-06-28 01:31:30','2022-06-28 01:31:30'),(7,'julio','perez','5465987','32','216564','correo123245@gmail.com','2022-06-28 01:33:56','2022-06-28 01:33:56'),(8,'julio','perez','5465987','32','216564','correo123245@gmail.com','2022-06-28 01:36:00','2022-06-28 01:36:00');
/*!40000 ALTER TABLE `customer` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `historical`
--

DROP TABLE IF EXISTS `historical`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `historical` (
  `id` int NOT NULL AUTO_INCREMENT,
  `idServicio` int NOT NULL,
  `create_at` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`,`idServicio`),
  KEY `fk_historical_service_idx` (`idServicio`),
  CONSTRAINT `fk_historical_service` FOREIGN KEY (`idServicio`) REFERENCES `services` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `historical`
--

LOCK TABLES `historical` WRITE;
/*!40000 ALTER TABLE `historical` DISABLE KEYS */;
/*!40000 ALTER TABLE `historical` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `pets`
--

DROP TABLE IF EXISTS `pets`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `pets` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(45) DEFAULT NULL,
  `species` varchar(45) DEFAULT NULL,
  `age` varchar(45) DEFAULT NULL,
  `race` varchar(45) DEFAULT NULL,
  `color` varchar(45) DEFAULT NULL,
  `weight` varchar(45) DEFAULT NULL,
  `gender` varchar(45) DEFAULT NULL,
  `customer_idCustomer` int NOT NULL,
  `created_at` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `update_at` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`,`customer_idCustomer`),
  KEY `fk_pets_customer_idx` (`customer_idCustomer`),
  CONSTRAINT `fk_pets_customer` FOREIGN KEY (`customer_idCustomer`) REFERENCES `customer` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `pets`
--

LOCK TABLES `pets` WRITE;
/*!40000 ALTER TABLE `pets` DISABLE KEYS */;
/*!40000 ALTER TABLE `pets` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `services`
--

DROP TABLE IF EXISTS `services`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `services` (
  `id` int NOT NULL AUTO_INCREMENT,
  `description` varchar(200) DEFAULT NULL,
  `price` int DEFAULT NULL,
  `idCustomer` int NOT NULL,
  `idVeterinarian` int DEFAULT NULL,
  `create_at` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `update_at` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`,`idCustomer`),
  KEY `fk_service_customer_idx` (`idCustomer`),
  KEY `fk_service_veterinarian_idx` (`idVeterinarian`),
  CONSTRAINT `fk_service_customer` FOREIGN KEY (`idCustomer`) REFERENCES `customer` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `services`
--

LOCK TABLES `services` WRITE;
/*!40000 ALTER TABLE `services` DISABLE KEYS */;
INSERT INTO `services` VALUES (1,'corte de pelo',10000,2,123456,'2022-06-28 01:36:00','2022-06-28 01:36:00');
/*!40000 ALTER TABLE `services` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `veterinarian`
--

DROP TABLE IF EXISTS `veterinarian`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `veterinarian` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(45) DEFAULT NULL,
  `last_name` varchar(45) DEFAULT NULL,
  `cc` varchar(45) DEFAULT NULL,
  `age` varchar(45) DEFAULT NULL,
  `tell` varchar(45) DEFAULT NULL,
  `email` varchar(45) DEFAULT NULL,
  `speciality` varchar(45) DEFAULT NULL,
  `salary` varchar(45) DEFAULT NULL,
  `veterinary_idVeterinary` int NOT NULL DEFAULT '1',
  `created_at` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `update_at` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`,`veterinary_idVeterinary`),
  KEY `fk_veterinarian_veterinary1_idx` (`veterinary_idVeterinary`),
  CONSTRAINT `fk_veterinarian_veterinary1` FOREIGN KEY (`veterinary_idVeterinary`) REFERENCES `veterinary` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `veterinarian`
--

LOCK TABLES `veterinarian` WRITE;
/*!40000 ALTER TABLE `veterinarian` DISABLE KEYS */;
/*!40000 ALTER TABLE `veterinarian` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `veterinary`
--

DROP TABLE IF EXISTS `veterinary`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `veterinary` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(45) DEFAULT NULL,
  `nit` varchar(45) DEFAULT NULL,
  `email` varchar(45) DEFAULT NULL,
  `tell` varchar(45) DEFAULT NULL,
  `dir` varchar(45) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `veterinary`
--

LOCK TABLES `veterinary` WRITE;
/*!40000 ALTER TABLE `veterinary` DISABLE KEYS */;
INSERT INTO `veterinary` VALUES (1,'Veterinaria Uchiha','902156789-2','veterinaria_uchiha@gmail.com','3101234556','calle falsa 123');
/*!40000 ALTER TABLE `veterinary` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2022-06-28 17:42:38
