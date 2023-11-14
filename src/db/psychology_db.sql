-- MySQL dump 10.13  Distrib 8.0.34, for Win64 (x86_64)
--
-- Host: localhost    Database: psychology_bd
-- ------------------------------------------------------
-- Server version	5.5.5-10.4.28-MariaDB

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
-- Table structure for table `citations`
--

DROP TABLE IF EXISTS `citations`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `citations` (
  `citation_id` int(11) NOT NULL AUTO_INCREMENT,
  `citation_date` date DEFAULT NULL,
  `description` text DEFAULT NULL,
  `status` int(11) DEFAULT 1,
  `created_at` timestamp NOT NULL DEFAULT current_timestamp(),
  `updated_at` timestamp NOT NULL DEFAULT current_timestamp() ON UPDATE current_timestamp(),
  `psychologist_id` int(11) DEFAULT NULL,
  `patient_id` int(11) DEFAULT NULL,
  PRIMARY KEY (`citation_id`),
  KEY `psychologist_id` (`psychologist_id`),
  KEY `patient_id` (`patient_id`),
  CONSTRAINT `patient_id` FOREIGN KEY (`patient_id`) REFERENCES `users` (`user_id`) ON DELETE NO ACTION ON UPDATE NO ACTION,
  CONSTRAINT `psychologist_id` FOREIGN KEY (`psychologist_id`) REFERENCES `users` (`user_id`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB AUTO_INCREMENT=8 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `citations`
--

LOCK TABLES `citations` WRITE;
/*!40000 ALTER TABLE `citations` DISABLE KEYS */;
INSERT INTO `citations` VALUES (5,'2023-11-17','Este es un rol de prueba xd',1,'2023-11-14 00:09:58','2023-11-14 00:09:58',4,3);
/*!40000 ALTER TABLE `citations` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `document_types`
--

DROP TABLE IF EXISTS `document_types`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `document_types` (
  `document_type_id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(50) DEFAULT NULL,
  `description` text DEFAULT NULL,
  `status` int(11) DEFAULT 1,
  `created_at` timestamp NOT NULL DEFAULT current_timestamp(),
  `updated_at` timestamp NOT NULL DEFAULT current_timestamp() ON UPDATE current_timestamp(),
  PRIMARY KEY (`document_type_id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `document_types`
--

LOCK TABLES `document_types` WRITE;
/*!40000 ALTER TABLE `document_types` DISABLE KEYS */;
INSERT INTO `document_types` VALUES (1,'CC','Cédula de Ciudadanía',1,'2023-10-28 22:49:08','2023-10-28 22:49:08');
/*!40000 ALTER TABLE `document_types` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `history`
--

DROP TABLE IF EXISTS `history`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `history` (
  `history_id` int(11) NOT NULL AUTO_INCREMENT,
  `patient_id` int(11) DEFAULT NULL,
  `psychologist_id` int(11) DEFAULT NULL,
  `status` int(11) DEFAULT 1,
  `update_at` timestamp NOT NULL DEFAULT current_timestamp() ON UPDATE current_timestamp(),
  `create_at` timestamp NOT NULL DEFAULT current_timestamp(),
  PRIMARY KEY (`history_id`),
  KEY `patient_id` (`patient_id`),
  KEY `psychologist_id` (`psychologist_id`),
  CONSTRAINT `history_ibfk_1` FOREIGN KEY (`patient_id`) REFERENCES `users` (`user_id`),
  CONSTRAINT `history_ibfk_2` FOREIGN KEY (`psychologist_id`) REFERENCES `users` (`user_id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `history`
--

LOCK TABLES `history` WRITE;
/*!40000 ALTER TABLE `history` DISABLE KEYS */;
INSERT INTO `history` VALUES (1,3,4,1,'2023-11-14 02:46:21','2023-11-14 02:46:21'),(2,3,1,1,'2023-11-14 04:52:35','2023-11-14 04:52:35');
/*!40000 ALTER TABLE `history` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `programs`
--

DROP TABLE IF EXISTS `programs`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `programs` (
  `program_id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(255) DEFAULT NULL,
  `description` text DEFAULT NULL,
  `duration` int(11) DEFAULT NULL,
  `status` int(11) DEFAULT 1,
  `update_at` timestamp NOT NULL DEFAULT current_timestamp() ON UPDATE current_timestamp(),
  `create_at` timestamp NOT NULL DEFAULT current_timestamp(),
  PRIMARY KEY (`program_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `programs`
--

LOCK TABLES `programs` WRITE;
/*!40000 ALTER TABLE `programs` DISABLE KEYS */;
/*!40000 ALTER TABLE `programs` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `results`
--

DROP TABLE IF EXISTS `results`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `results` (
  `result_id` int(11) NOT NULL AUTO_INCREMENT,
  `appointment_id` int(11) DEFAULT NULL,
  `rating` int(11) DEFAULT NULL,
  `feedback` text DEFAULT NULL,
  `status` int(11) DEFAULT 1,
  `create_at` timestamp NOT NULL DEFAULT current_timestamp(),
  `update_at` timestamp NOT NULL DEFAULT current_timestamp() ON UPDATE current_timestamp(),
  PRIMARY KEY (`result_id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `results`
--

LOCK TABLES `results` WRITE;
/*!40000 ALTER TABLE `results` DISABLE KEYS */;
INSERT INTO `results` VALUES (1,5,2,'wdfdsff',1,'2023-11-14 03:40:39','2023-11-14 03:40:39');
/*!40000 ALTER TABLE `results` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `roles`
--

DROP TABLE IF EXISTS `roles`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `roles` (
  `rol_id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(50) DEFAULT NULL,
  `description` text DEFAULT NULL,
  `status` int(11) DEFAULT 1,
  `created_at` timestamp NOT NULL DEFAULT current_timestamp(),
  `updated_at` timestamp NOT NULL DEFAULT current_timestamp() ON UPDATE current_timestamp(),
  PRIMARY KEY (`rol_id`)
) ENGINE=InnoDB AUTO_INCREMENT=8 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `roles`
--

LOCK TABLES `roles` WRITE;
/*!40000 ALTER TABLE `roles` DISABLE KEYS */;
INSERT INTO `roles` VALUES (1,'Admin','Este usuario tiene todos los privilegios',1,'2023-10-28 22:00:31','2023-10-28 22:15:37'),(2,'Psychologist','Este usuario puede...',1,'2023-10-28 22:02:19','2023-10-29 00:04:09'),(3,'Patient','Este usuario puede...',1,'2023-10-28 22:07:39','2023-10-29 00:04:09'),(4,'Professor','Este es el rol para los profesores (obvio ¿no?)',1,'2023-11-13 21:33:06','2023-11-13 21:33:06'),(5,'Prueba','Este es un rol de prueba xd',0,'2023-11-13 21:33:23','2023-11-13 21:48:23'),(6,'prueba cul 1','esto solo es para el vídeo bro 1',0,'2023-11-14 04:53:34','2023-11-14 04:54:09'),(7,'hola','hola',1,'2023-11-14 04:55:24','2023-11-14 04:55:24');
/*!40000 ALTER TABLE `roles` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `tuitions`
--

DROP TABLE IF EXISTS `tuitions`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `tuitions` (
  `tuition_id` int(11) NOT NULL AUTO_INCREMENT,
  `program_id` int(11) DEFAULT NULL,
  `user_id` int(11) DEFAULT NULL,
  `tation_date` date DEFAULT NULL,
  `status` int(11) DEFAULT 1,
  PRIMARY KEY (`tuition_id`),
  KEY `program_id` (`program_id`),
  KEY `user_id` (`user_id`),
  CONSTRAINT `tuitions_ibfk_1` FOREIGN KEY (`program_id`) REFERENCES `programs` (`program_id`),
  CONSTRAINT `tuitions_ibfk_2` FOREIGN KEY (`user_id`) REFERENCES `users` (`user_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `tuitions`
--

LOCK TABLES `tuitions` WRITE;
/*!40000 ALTER TABLE `tuitions` DISABLE KEYS */;
/*!40000 ALTER TABLE `tuitions` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `users`
--

DROP TABLE IF EXISTS `users`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `users` (
  `user_id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(50) DEFAULT NULL,
  `middlename` varchar(50) DEFAULT NULL,
  `first_lastname` varchar(50) DEFAULT NULL,
  `second_lastname` varchar(50) DEFAULT NULL,
  `identification` varchar(20) DEFAULT NULL,
  `age` int(11) DEFAULT NULL,
  `telephone` varchar(15) DEFAULT NULL,
  `phone` varchar(15) DEFAULT NULL,
  `username` varchar(50) DEFAULT NULL,
  `password` varchar(255) DEFAULT NULL,
  `status` int(11) DEFAULT 1,
  `created_at` timestamp NOT NULL DEFAULT current_timestamp(),
  `updated_at` timestamp NOT NULL DEFAULT current_timestamp() ON UPDATE current_timestamp(),
  `rol_id` int(11) DEFAULT NULL,
  `document_type_id` int(11) DEFAULT NULL,
  PRIMARY KEY (`user_id`),
  KEY `users_ibfk_2` (`document_type_id`),
  KEY `users_ibfk_1` (`rol_id`),
  CONSTRAINT `users_ibfk_1` FOREIGN KEY (`rol_id`) REFERENCES `roles` (`rol_id`) ON DELETE CASCADE ON UPDATE CASCADE,
  CONSTRAINT `users_ibfk_2` FOREIGN KEY (`document_type_id`) REFERENCES `document_types` (`document_type_id`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB AUTO_INCREMENT=20 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `users`
--

LOCK TABLES `users` WRITE;
/*!40000 ALTER TABLE `users` DISABLE KEYS */;
INSERT INTO `users` VALUES (1,'Carlo','Alberto','Melo','Sierra','3444444',40,'334543234','34543234','CAlberto123','123',1,'2023-10-28 23:38:12','2023-11-13 01:51:55',2,1),(3,'Zacarias','Flores','Del Campo','Templado','123456789',30,'1234567890','9876543210','DelCampo123','123',1,'2023-10-28 23:43:12','2023-10-29 00:07:44',3,1),(4,'9','2','3','4','5',6,'7','8',NULL,NULL,1,'2023-11-12 22:36:54','2023-11-13 22:00:48',2,1),(5,'SanchoPansa123','Enrique','Pansa','Salazar','12324',32,'143234','234242',NULL,NULL,1,'2023-11-12 22:40:17','2023-11-13 22:00:48',3,1),(6,'Sancho2','Enrique','Pansa','Salazar','12324',32,'143234','234242',NULL,NULL,1,'2023-11-12 22:41:32','2023-11-13 22:00:48',3,1),(7,'Juancho','asdads','asdasd','Alverto','2234',2343,'(4) 4855748','23424',NULL,NULL,1,'2023-11-12 22:46:35','2023-11-13 22:00:48',2,1),(8,'Juancho2','asdads','asdasd','Alverto','2234',2343,'(4) 4855748','23424',NULL,NULL,1,'2023-11-12 22:51:40','2023-11-13 22:00:48',3,1),(9,'Prueba1','Prueba1','Prueba1','Prueba1','1111111',111,'111111111','111111','Prueba1','123',0,'2023-11-13 00:29:01','2023-11-14 04:50:13',2,1),(10,'11','22','33','44','55',66,'77','88','','1010',0,'2023-11-13 00:32:36','2023-11-13 22:00:48',1,1),(16,'xxxxxx','xxxxx','xxxxxx','xxxxx','11111',11111,'xxxxxx','3053804049','xxxxxxxxxxxxx','xxxxxxxxxxxxxx',1,'2023-11-13 01:20:38','2023-11-13 01:20:38',1,1),(17,'PArangaquiturimicuaro','zzzzzzzz','zzzzzzz','zzzzzz','22222',2222,'zzzzzzzz','zzzzzzzzzz','zzzzzzzz','zzzzzzz',0,'2023-11-13 01:42:45','2023-11-13 20:34:58',3,1),(18,'zzzzzz','zzzzzzzz','zzzzzzz','zzzzzz','22222',2222,'zzzzzzzz','zzzzzzzzzz','zzzzzzzz','jhgfdsasdfg',1,'2023-11-13 20:32:59','2023-11-13 20:32:59',1,1),(19,'Joseph ','De Jesus','Sierra','Beleño','1001947812',22,'33333333','3333333','Joshsb','123',1,'2023-11-14 04:48:48','2023-11-14 04:48:48',1,1);
/*!40000 ALTER TABLE `users` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `visits`
--

DROP TABLE IF EXISTS `visits`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `visits` (
  `visit_id` int(11) NOT NULL AUTO_INCREMENT,
  `notes` text DEFAULT NULL,
  `status` int(11) DEFAULT 1,
  `created_at` timestamp NOT NULL DEFAULT current_timestamp(),
  `updated_at` timestamp NOT NULL DEFAULT current_timestamp() ON UPDATE current_timestamp(),
  `visit_date` date DEFAULT NULL,
  `psychologist_id` int(11) DEFAULT NULL,
  `patient_id` int(11) DEFAULT NULL,
  PRIMARY KEY (`visit_id`),
  KEY `psychologist_id` (`psychologist_id`),
  KEY `patient_id` (`patient_id`),
  CONSTRAINT `visits_ibfk_1` FOREIGN KEY (`psychologist_id`) REFERENCES `users` (`user_id`),
  CONSTRAINT `visits_ibfk_2` FOREIGN KEY (`patient_id`) REFERENCES `users` (`user_id`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `visits`
--

LOCK TABLES `visits` WRITE;
/*!40000 ALTER TABLE `visits` DISABLE KEYS */;
INSERT INTO `visits` VALUES (1,'El paciente tiene delirios de grandeza, le dije que me dijera lo que tenía y me dijo que no hablaba con negros.',0,'2023-11-14 02:24:06','2023-11-14 02:26:09','2023-11-03',7,6),(2,'El paciente es cule man esquizofrenico nojodaaa, llegó diciendo y que el nacional le gana al Junior.',1,'2023-11-14 02:17:31','2023-11-14 02:17:31','2023-11-01',1,3),(3,'Hola historial!',1,'2023-11-14 02:41:53','2023-11-14 02:41:53','2023-11-13',1,3),(4,'hola esto es para el historial ahora sí :v',1,'2023-11-14 02:46:21','2023-11-14 02:46:21','2023-11-01',4,3),(5,'El estudiante tenía síntomas de esquizofrenia :) 1',0,'2023-11-14 04:52:53','2023-11-14 04:53:02','2023-11-15',4,6);
/*!40000 ALTER TABLE `visits` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2023-11-14  0:00:36
