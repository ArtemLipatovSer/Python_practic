-- phpMyAdmin SQL Dump
-- version 5.2.0
-- https://www.phpmyadmin.net/
--
-- Хост: 127.0.0.1:3306
-- Время создания: Янв 18 2024 г., 21:10
-- Версия сервера: 8.0.30
-- Версия PHP: 8.0.22

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- База данных: `Test`
--

-- --------------------------------------------------------

--
-- Структура таблицы `People`
--

CREATE TABLE `People` (
  `Id` int NOT NULL,
  `Age` int DEFAULT NULL,
  `Firstname` varchar(20) NOT NULL,
  `Lastname` varchar(20) DEFAULT NULL,
  `Phone` varchar(20) NOT NULL,
  `Email` varchar(30) DEFAULT NULL
) ;

--
-- Дамп данных таблицы `People`
--

INSERT INTO `People` (`Id`, `Age`, `Firstname`, `Lastname`, `Phone`, `Email`) VALUES
(1, 21, 'Tom', 'Smith', '88002301525', 'test@gmail.com'),
(3, 21, 'Ram', NULL, '88002301526', 'test@gmail.com'),
(6, 21, 'Ramz1243', NULL, '880023015123', 'test@gmail.com'),
(7, 27, 'Ramz77', NULL, '88002307777', 'test@gmail.com');

-- --------------------------------------------------------

--
-- Структура таблицы `Post`
--

CREATE TABLE `Post` (
  `id` int NOT NULL,
  `title` varchar(50) DEFAULT NULL,
  `txt` text
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3;

--
-- Дамп данных таблицы `Post`
--

INSERT INTO `Post` (`id`, `title`, `txt`) VALUES
(1, 'test', 'lorem lorem lorem lorem lorem lorem lorem'),
(2, 'test', 'lorem lorem lorem lorem lorem lorem lorem');

-- --------------------------------------------------------

--
-- Структура таблицы `Products`
--

CREATE TABLE `Products` (
  `Id` int NOT NULL,
  `ProductName` varchar(30) NOT NULL,
  `Manufactuer` varchar(20) NOT NULL,
  `ProductCount` int DEFAULT '0',
  `Price` decimal(10,0) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3;

--
-- Дамп данных таблицы `Products`
--

INSERT INTO `Products` (`Id`, `ProductName`, `Manufactuer`, `ProductCount`, `Price`) VALUES
(1, 'Iphone 8', 'Apple', 3, '2000'),
(2, 'Iphone X', 'Apple', 10, '2700'),
(3, 'Galaxy S10', 'Samsung', 5, '16000'),
(4, 'Galaxy S21', 'Samsung', 11, '26000'),
(5, 'Honor 10', 'Huawei', 3, '8000');

-- --------------------------------------------------------

--
-- Структура таблицы `user`
--

CREATE TABLE `user` (
  `id` int NOT NULL,
  `name` varchar(25) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NOT NULL,
  `age` int DEFAULT NULL,
  `about` text CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3;

--
-- Индексы сохранённых таблиц
--

--
-- Индексы таблицы `People`
--
ALTER TABLE `People`
  ADD PRIMARY KEY (`Id`),
  ADD UNIQUE KEY `Phone` (`Phone`);

--
-- Индексы таблицы `Post`
--
ALTER TABLE `Post`
  ADD PRIMARY KEY (`id`);

--
-- Индексы таблицы `Products`
--
ALTER TABLE `Products`
  ADD PRIMARY KEY (`Id`);

--
-- Индексы таблицы `user`
--
ALTER TABLE `user`
  ADD PRIMARY KEY (`id`);

--
-- AUTO_INCREMENT для сохранённых таблиц
--

--
-- AUTO_INCREMENT для таблицы `People`
--
ALTER TABLE `People`
  MODIFY `Id` int NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT для таблицы `Post`
--
ALTER TABLE `Post`
  MODIFY `id` int NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

--
-- AUTO_INCREMENT для таблицы `Products`
--
ALTER TABLE `Products`
  MODIFY `Id` int NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=6;

--
-- AUTO_INCREMENT для таблицы `user`
--
ALTER TABLE `user`
  MODIFY `id` int NOT NULL AUTO_INCREMENT;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
