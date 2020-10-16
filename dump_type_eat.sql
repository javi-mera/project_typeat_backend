-- MySQL dump 10.13  Distrib 8.0.21, for Linux (x86_64)
--
-- Host: localhost    Database: example
-- ------------------------------------------------------
-- Server version	8.0.21-0ubuntu0.20.04.4

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8mb4 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Dumping data for table `alembic_version`
--

LOCK TABLES `alembic_version` WRITE;
/*!40000 ALTER TABLE `alembic_version` DISABLE KEYS */;
INSERT INTO `alembic_version` VALUES ('5e85166e9a6e');
/*!40000 ALTER TABLE `alembic_version` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Dumping data for table `city`
--

LOCK TABLES `city` WRITE;
/*!40000 ALTER TABLE `city` DISABLE KEYS */;
INSERT INTO `city` VALUES (1,'Madrid'),(2,'Barcelona'),(3,'Bilbao'),(4,'Badajoz'),(5,'Cordoba');
/*!40000 ALTER TABLE `city` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Dumping data for table `dish`
--

LOCK TABLES `dish` WRITE;
/*!40000 ALTER TABLE `dish` DISABLE KEYS */;
INSERT INTO `dish` VALUES (1,'Flamenquines','Los flamenquines cordobeses son unos rollitos fritos de cerdo con jamón y queso muy típicos de Córdoba (aunque se crearon en Jaén), de ahí que se llamen flamenquines cordobeses.',1,7,'https://recetasdecocina.elmundo.es/wp-content/uploads/2016/03/receta-flamenquines.jpg'),(2,'Salmorejo','El salmorejo cordobés es una crema servida habitualmente como primer plato; se trata de una preparación tradicional de Córdoba.​​ Se elabora mediante un majado de una cierta cantidad de miga de pan, ​ a la que se le incluye además ajo, aceite de oliva, sal y tomates.​',1,7,'https://i.blogs.es/ee2696/salmorejo-tradicional-pakus-directo-al-paladar/1366_2000.jpg'),(3,'Berenjenas con miel','Las berenjenas fritas con miel de caña son una de las recetas más típicas de la cocina cordobesa.',1,7,'https://1.bp.blogspot.com/-Hc6Cw2MU41U/V-FZALWov5I/AAAAAAABxSo/qPlUD2Xnz5gmXEMfz7l2YFkV0jG52Pl_gCLcB/s1600/berenjenas%2Bcon%2Bmiel%2B3.JPG'),(4,'Callos a la madrileña','Los callos a la madrileña son uno de los platos más típicos del invierno madrileño .​ Se elabora principalmente con tripas de vaca que se ofrecen por regla general en las casquerías existentes cerca de las carnicerías de la capital madrileña.​ ',1,1,'https://encrypted-tbn0.gstatic.com/images?q=tbn%3AANd9GcQZak-T5YZAA4VrHsA6qM2-96rnwT7x_KXGBA&usqp=CAU'),(5,'Bocadillo de calamares','El bocadillo de calamares o bocata de calamares​ es una especialidad culinaria típica en Madrid consistente en, o bien calamares rebozados en harina y fritos en aceite que suele ser de oliva, o bien la versión más sofisticada que es todo lo anterior más una salsa de tomate picante y mayonesa con ajo similar a la de las patatas bravas.',1,1,'https://i.blogs.es/6ac7ba/bocadillo-de-calamares-dap/840_560.jpg'),(6,'Cocido Madrileño','El cocido madrileño es uno de los platos más representativos de la cocina de Madrid.​ Consiste en un guiso cuyo ingrediente principal son los garbanzos y los secundarios, aunque con gran protagonismo, diversas verduras, carnes y tocino de cerdo con algún embutido. ',1,2,'https://encrypted-tbn0.gstatic.com/images?q=tbn%3AANd9GcR697bHAUr-i9xrB5gm4To_RsPEBHKwNmcLJw&usqp=CAU'),(7,'Pan tumaca','El pan tumaca o pan con tomate es una receta típica de Cataluña, la cual se consume sobre todo como merienda y desayuno..',1,3,'https://ep01.epimg.net/elpais/imagenes/2018/05/18/opinion/1526635494_896871_1526643707_noticia_normal.jpg'),(8,'Pan tumaca','El mejor pan con tomate y ajo de Barcelona.',1,4,'https://blog.ruralmur.com/wp-content/uploads/2015/09/Pan-tumaca.jpg'),(9,'Butifarra con alubias','La butifarra con alubias es un plato tradicional de la cocina catalana, a base de butifarra y de judías blancas, que se popularizó sobre todo en las fondas de comida casera y popular del siglo XIX. El binomio butifarra y alubias se considera característico de la cocina catalana y occitana en general.',1,4,'https://images-gmi-pmc.edge-generalmills.com/a29e8e8b-cbd3-43c7-9393-6cd6d7305158.jpg'),(10,'Bacalao al pil-pil','El bacalao al pil-pil es un plato tradicional típico de la cocina vasca elaborado con cuatro ingredientes básicos: bacalao, aceite de oliva, ajo y pimientos guindillas. Se suele emplear por regla general en su elaboración una cazuela de barro y se sirve caliente.',1,5,'https://media-cdn.tripadvisor.com/media/photo-s/0f/7e/e3/d8/bacalao-al-pil-pil.jpg');
/*!40000 ALTER TABLE `dish` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Dumping data for table `file_contents`
--

LOCK TABLES `file_contents` WRITE;
/*!40000 ALTER TABLE `file_contents` DISABLE KEYS */;
/*!40000 ALTER TABLE `file_contents` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Dumping data for table `preferredDishes`
--

LOCK TABLES `preferredDishes` WRITE;
/*!40000 ALTER TABLE `preferredDishes` DISABLE KEYS */;
/*!40000 ALTER TABLE `preferredDishes` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Dumping data for table `restaurant`
--

LOCK TABLES `restaurant` WRITE;
/*!40000 ALTER TABLE `restaurant` DISABLE KEYS */;
INSERT INTO `restaurant` VALUES (1,'Macario´s Place','C/Canarias',777777777,'macario@gmail.com','www.macarios.es',1,'40.533568','-3.922990',1),(2,'Arrozz','C/Viena',666666666,'arroz@gmail.com','www.arrozz.es',1,'40.536308','-3.898442',1),(3,'Onyx','Plaza España',555555555,'onyx@gmail.com','www.restauranteonyx.com',1,'41.375203','2.149166',2),(4,'La Copisteria','C/de Cai Celi',444444444,'caicai@gmail.com','www.caicai.cat',1,'41.366174','2.165245',2),(5,'Botxo','Av. de las Univeridades',333333333,'botxorest@gmail.com','www.botxorest@gmail.com',1,'43.270693','-2.933565',3),(6,'El Muelle del Guadiana','Travesía Camino San Vicente Viejo',222222222,'elmuelle@yahoo.es','www.elmuelle.com',1,'38.883517','-6.976350',4),(7,'Morilete','Calle Antonio Maura, 21, 14004 Córdoba',111111111,'elmejorbar@gmail.com','www.elmejorbar.com',0,'37.882809','-4.788543',5);
/*!40000 ALTER TABLE `restaurant` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Dumping data for table `user`
--

LOCK TABLES `user` WRITE;
/*!40000 ALTER TABLE `user` DISABLE KEYS */;
/*!40000 ALTER TABLE `user` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2020-10-07 17:11:00
