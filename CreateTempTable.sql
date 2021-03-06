CREATE TABLE `hasindatabase`.`Temp Table` (
  `PCNumber` INT NOT NULL,
  `Date` DATE NOT NULL,
  `Item` VARCHAR(255) NOT NULL,
  `Price` DECIMAL(7,2) NULL,
  `Items Sold` INT(5) NULL,
  `Sold Amount` DECIMAL(11,2) NULL,
  `Percent Sold` DECIMAL(5,2) NULL,
  `Item Reduction` DECIMAL(7,2) NULL,
  `Item Refunds` DECIMAL(7,2) NULL,
  `Item Net Sales` DECIMAL(11,2) NULL,
  PRIMARY KEY (`PCNumber`, `Date`, `Item`));