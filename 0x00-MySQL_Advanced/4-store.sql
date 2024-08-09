-- Creates a trigger to decrease item quantity after an order
DELIMITER //

CREATE TRIGGER after_insert_order
AFTER INSERT ON orders
FOR EACH ROW
BEGIN
    UPDATE items SET quantity = quantity - NEW.number
    WHERE name = NEW.item_name;
END //

DELIMITER ;

