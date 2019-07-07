-- MySQL dump 10.13  Distrib 8.0.16, for macos10.14 (x86_64)
--
-- Host: 192.168.0.120    Database: lesson1
-- ------------------------------------------------------
-- Server version	8.0.13

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
 SET NAMES utf8 ;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `_cities`
--

DROP TABLE IF EXISTS `_cities`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
 SET character_set_client = utf8mb4 ;
CREATE TABLE `_cities` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `country_id` int(11) NOT NULL,
  `important` tinyint(1) NOT NULL,
  `region_id` int(11) NOT NULL,
  `title` varchar(150) COLLATE utf8mb4_unicode_ci NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `title` (`title`),
  KEY `cou_id` (`country_id`),
  KEY `region_id` (`region_id`),
  CONSTRAINT `cou_id` FOREIGN KEY (`country_id`) REFERENCES `_countries` (`id`),
  CONSTRAINT `region_id` FOREIGN KEY (`region_id`) REFERENCES `_regions` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=13 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `_cities`
--

LOCK TABLES `_cities` WRITE;
/*!40000 ALTER TABLE `_cities` DISABLE KEYS */;
INSERT INTO `_cities` VALUES (1,1,0,1,'Александров'),(2,1,0,1,'Карабаново'),(3,1,0,2,'Ме́ленки'),(4,1,0,2,'Митино'),(5,1,0,3,'Зеленогорск'),(6,1,0,3,'Сестрорецк'),(7,1,0,3,'Кронштадт'),(8,1,0,4,'Видное'),(9,1,0,4,'Ашукино'),(10,1,0,5,'Волосово'),(11,1,0,5,'Гатчина'),(12,1,0,6,'Коркино');
/*!40000 ALTER TABLE `_cities` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `_countries`
--

DROP TABLE IF EXISTS `_countries`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
 SET character_set_client = utf8mb4 ;
CREATE TABLE `_countries` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `title` varchar(150) COLLATE utf8mb4_unicode_ci NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `title_2` (`title`),
  KEY `title` (`title`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `_countries`
--

LOCK TABLES `_countries` WRITE;
/*!40000 ALTER TABLE `_countries` DISABLE KEYS */;
INSERT INTO `_countries` VALUES (2,'Автралия'),(4,'Вьетнам'),(5,'Нидерланды'),(1,'Россия'),(3,'США');
/*!40000 ALTER TABLE `_countries` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `_regions`
--

DROP TABLE IF EXISTS `_regions`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
 SET character_set_client = utf8mb4 ;
CREATE TABLE `_regions` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `country_id` int(11) NOT NULL,
  `title` varchar(150) COLLATE utf8mb4_unicode_ci NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `title` (`title`),
  KEY `country_id` (`country_id`),
  CONSTRAINT `country_id` FOREIGN KEY (`country_id`) REFERENCES `_countries` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=21 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `_regions`
--

LOCK TABLES `_regions` WRITE;
/*!40000 ALTER TABLE `_regions` DISABLE KEYS */;
INSERT INTO `_regions` VALUES (1,1,'Владимирская'),(2,1,'Москва'),(3,1,'Санкт-Петербург'),(4,1,'Московская'),(5,1,'Ленинградская'),(6,1,'Челябинская'),(7,2,'Австралийская столичная территория'),(8,2,'Виктория'),(9,2,'Западная Австралия'),(10,2,'Квинсленд'),(11,2,'Новый Южный Уэльс'),(12,3,'Айдахо'),(13,3,'Вашингтон'),(14,3,'Индиана'),(15,3,'Массачусетс'),(16,4,'Лайтяу'),(17,4,'Кханьхоа'),(18,5,'Гелдерланд'),(19,5,'Северная Голландия '),(20,5,'Фрисландия ');
/*!40000 ALTER TABLE `_regions` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `districts`
--

DROP TABLE IF EXISTS `districts`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
 SET character_set_client = utf8mb4 ;
CREATE TABLE `districts` (
  `dis_id` int(11) NOT NULL AUTO_INCREMENT,
  `dis_name` varchar(100) CHARACTER SET utf8mb4 COLLATE utf8mb4_bin NOT NULL,
  `reg_id` int(11) DEFAULT NULL,
  PRIMARY KEY (`dis_id`)
) ENGINE=InnoDB AUTO_INCREMENT=13 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `districts`
--

LOCK TABLES `districts` WRITE;
/*!40000 ALTER TABLE `districts` DISABLE KEYS */;
INSERT INTO `districts` VALUES (1,'Александровский',1),(2,'Меленковский',1),(3,'Митино',2),(4,'Раменки',2),(5,'Курортный',3),(6,'Кронштадтский',3),(7,'Ленинский',4),(8,'Пушкинский',4),(9,'Волосовский',5),(10,' Гатчинский',5),(11,'Агаповский',6),(12,'Коркинский',6);
/*!40000 ALTER TABLE `districts` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2019-07-08  0:43:05
