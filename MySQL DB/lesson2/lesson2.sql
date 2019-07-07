{\rtf1\ansi\ansicpg1251\cocoartf1671\cocoasubrtf500
{\fonttbl\f0\fnil\fcharset0 HelveticaNeue;}
{\colortbl;\red255\green255\blue255;}
{\*\expandedcolortbl;;}
\paperw11900\paperh16840\margl1440\margr1440\vieww10800\viewh8400\viewkind0
\deftab560
\pard\pardeftab560\slleading20\partightenfactor0

\f0\fs24 \cf0 USE `lesson1`\
ALTER TABLE `countries` \
CHANGE COLUMN `cou_id` `id` INT NOT NULL AUTO_INCREMENT,\
CHANGE COLUMN `country_name` `title` VARCHAR(150) NOT NULL;\
ALTER TABLE `countries` ADD UNIQUE INDEX (`title`);\
SHOW COLUMNS FROM `countries`;\
ALTER TABLE `countries` RENAME `_countries`;\
\
ALTER TABLE `regions` RENAME `_regions`;\
ALTER TABLE `_regions` \
CHANGE COLUMN `reg_id` `id` INT NOT NULL AUTO_INCREMENT,\
CHANGE COLUMN `reg_name` `title` VARCHAR(150) NOT NULL;\
ALTER TABLE `_regions` \
CHANGE COLUMN `cou_id` `country_id` INT NOT NULL;\
ALTER TABLE `_regions` \
ADD CONSTRAINT `country_id` FOREIGN KEY (`country_id`) REFERENCES `_countries`(`id`);\
ALTER TABLE `_regions` ADD UNIQUE INDEX (`title`);\
ALTER TABLE `_regions` MODIFY `title` VARCHAR(150) NOT NULL AFTER `country_id`;\
\pard\pardeftab560\slleading20\pardirnatural\partightenfactor0
\cf0 \
\pard\pardeftab560\slleading20\partightenfactor0
\cf0 ALTER TABLE `cities` RENAME `_cities`;\
ALTER TABLE `_cities` \
CHANGE COLUMN `cit_id` `id` INT NOT NULL AUTO_INCREMENT,\
ADD COLUMN `country_id` INT NOT NULL AFTER `id`,\
ADD COLUMN `important` TINYINT(1) NOT NULL AFTER `country_id`,\
ADD COLUMN `region_id` INT NOT NULL AFTER `important`,\
CHANGE COLUMN `cit_name` `title` VARCHAR(150) NOT NULL;\
\pard\pardeftab560\slleading20\pardirnatural\partightenfactor0
\cf0 \
\pard\pardeftab560\slleading20\partightenfactor0
\cf0 UPDATE `lesson1`.`_cities` SET `country_id` = '1', `region_id` = '1' WHERE (`id` = '1');\
UPDATE `lesson1`.`_cities` SET `country_id` = '1', `region_id` = '1' WHERE (`id` = '2');\
UPDATE `lesson1`.`_cities` SET `country_id` = '1', `region_id` = '2' WHERE (`id` = '3');\
UPDATE `lesson1`.`_cities` SET `country_id` = '1', `region_id` = '2' WHERE (`id` = '4');\
UPDATE `lesson1`.`_cities` SET `country_id` = '1', `region_id` = '3' WHERE (`id` = '5');\
UPDATE `lesson1`.`_cities` SET `country_id` = '1', `region_id` = '3' WHERE (`id` = '6');\
UPDATE `lesson1`.`_cities` SET `country_id` = '1', `region_id` = '3' WHERE (`id` = '7');\
UPDATE `lesson1`.`_cities` SET `country_id` = '1', `region_id` = '4' WHERE (`id` = '8');\
UPDATE `lesson1`.`_cities` SET `country_id` = '1', `region_id` = '4' WHERE (`id` = '9');\
UPDATE `lesson1`.`_cities` SET `country_id` = '1', `region_id` = '5' WHERE (`id` = '10');\
UPDATE `lesson1`.`_cities` SET `country_id` = '1', `region_id` = '5' WHERE (`id` = '11');\
UPDATE `lesson1`.`_cities` SET `country_id` = '1' WHERE (`id` = '12');\
\pard\pardeftab560\slleading20\pardirnatural\partightenfactor0
\cf0 \
\pard\pardeftab560\slleading20\partightenfactor0
\cf0 ALTER TABLE `_cities` \
ADD CONSTRAINT `cou_id` FOREIGN KEY (`country_id`) REFERENCES `_countries`(`id`);\
ALTER TABLE `_cities` \
ADD CONSTRAINT `region_id` FOREIGN KEY (`region_id`) REFERENCES `_regions`(`id`),\
ADD UNIQUE INDEX (`title`),\
DROP COLUMN `dis_id`;}