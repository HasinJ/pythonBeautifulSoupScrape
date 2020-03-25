CREATE TABLE `hasindatabase`.`testcsv` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `PC Number` INT NOT NULL,
  `Date` DATE NOT NULL,
  `Item` VARCHAR(255) NOT NULL,
  `Price` DECIMAL(7,2) NULL,
  `Items Sold` INT(5) NULL,
  `Sold Amount` DECIMAL(11,2) NULL,
  `Percent Sales` DECIMAL(5,2) NULL,
  `Item Reductions` DECIMAL(7,2) NULL,
  `Item Refunds` DECIMAL(7,2) NULL,
  `Item Net Sales` DECIMAL(11,2) NULL,
  PRIMARY KEY (`id`));
  
  CREATE TABLE `hasindatabase`.`new_table` (
  `idnew_table` INT NOT NULL AUTO_INCREMENT,
  PRIMARY KEY (`idnew_table`));