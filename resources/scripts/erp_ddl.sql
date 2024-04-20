CREATE TABLE `erp_orders` (
  `order_id` INT NOT NULL AUTO_INCREMENT,
  `order_date` DATE NOT NULL,
  `expected_delivery_date` DATE NOT NULL,
  `actual_delivery_date` DATE,
  `delivery_status` VARCHAR(50),
  `delivery_cost` DECIMAL(10, 2),
  PRIMARY KEY (`order_id`)
);

CREATE TABLE `customer_feedback` (
  `feedback_id` INT NOT NULL AUTO_INCREMENT,
  `order_id` INT NOT NULL,
  `satisfaction_rating` TINYINT NOT NULL,
  `comment` TEXT,
  PRIMARY KEY (`feedback_id`),
  FOREIGN KEY (`order_id`) REFERENCES `erp_orders`(`order_id`) ON DELETE CASCADE
);

-- Créer un index sur la colonne `satisfaction_rating`
CREATE INDEX idx_satisfaction ON customer_feedback (satisfaction_rating);
