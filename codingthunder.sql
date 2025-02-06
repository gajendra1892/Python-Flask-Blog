-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Feb 06, 2025 at 05:49 AM
-- Server version: 8.0.41
-- PHP Version: 8.0.30

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `codingthunder`
--

-- --------------------------------------------------------

--
-- Table structure for table `contacts`
--

CREATE TABLE `contacts` (
  `sno` int NOT NULL,
  `name` text NOT NULL,
  `email` varchar(50) NOT NULL,
  `phone_num` varchar(50) NOT NULL,
  `msg` text NOT NULL,
  `date` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Dumping data for table `contacts`
--

INSERT INTO `contacts` (`sno`, `name`, `email`, `phone_num`, `msg`, `date`) VALUES
(1, 'FirstPost', 'firstpost@gmailcom', '1234567891', 'first post done', '2025-02-05 11:27:21'),
(2, 'Gajendra Rathor', 'abs@gmail.com', '9723456789', 'tets', '2025-02-05 14:47:21'),
(3, 'Gajendra Rathor', 'abs@gmail.com', '9723456789', 'sdffas', '2025-02-05 15:43:17'),
(4, 'Gajendra Rathor', 'abs@gmail.com', '9723456789', 'sdfds', '2025-02-05 15:47:16'),
(5, 'Gajendra Rathor', 'abs@gmail.com', '9723456789', 'xZCx', '2025-02-05 15:48:52');

-- --------------------------------------------------------

--
-- Table structure for table `posts`
--

CREATE TABLE `posts` (
  `sno` int NOT NULL,
  `title` text NOT NULL,
  `content` text NOT NULL,
  `date` datetime DEFAULT CURRENT_TIMESTAMP,
  `slug` varchar(25) NOT NULL,
  `img_file` varchar(20) NOT NULL,
  `tagline` varchar(25) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Dumping data for table `posts`
--

INSERT INTO `posts` (`sno`, `title`, `content`, `date`, `slug`, `img_file`, `tagline`) VALUES
(1, 'This is my first post', 'This is my first post\r\nI am very much existed for this.Update', '2025-02-06 07:07:03', 'first-post', 'about-bg.jpg', 'This new tagLineqqq'),
(2, 'This my second post', 'I have done posting twice', '2025-02-06 07:21:33', 'second-post', 'contact-bg.jpg', 'update tagline'),
(3, 'This my Third post', 'This my Third post\r\nAnd I am done with posting.\r\n', '2025-02-05 17:08:52', 'third-post', '', ''),
(4, 'imgFile', 'imgFile', NULL, 'imgFile', '', 'imgFile'),
(5, 'img_file', 'img_file', NULL, 'img_file', '', 'img_file'),
(6, 'img_file', 'img_file', '2025-02-05 19:59:05', 'img_file', '', 'img_file');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `contacts`
--
ALTER TABLE `contacts`
  ADD PRIMARY KEY (`sno`);

--
-- Indexes for table `posts`
--
ALTER TABLE `posts`
  ADD PRIMARY KEY (`sno`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `contacts`
--
ALTER TABLE `contacts`
  MODIFY `sno` int NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=6;

--
-- AUTO_INCREMENT for table `posts`
--
ALTER TABLE `posts`
  MODIFY `sno` int NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=8;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
