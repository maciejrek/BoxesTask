from typing import List, Dict

box_sizes = [3, 6, 9]


def get_number_of_inner_boxes(order_size: int) -> int:
    """
    Number of inner boxes to use.
    Depends on the order size (increases by 1 every 9 items)
    :param order_size: Size of the order
    :return: Number of boxes required for given order size
    """
    if not isinstance(order_size, int):
        raise TypeError("Order size should be an integer")
    return order_size // 9 + 1 if order_size % 9 != 0 else order_size // 9


def add_outer_boxes(boxes: List) -> None:
    """
    Adds number of outer boxes to use.
    Depends on the number of inner boxes.
    :param boxes: List of inner boxes in the order.
    """
    if not isinstance(boxes, list):
        raise TypeError("Boxes should be a list")
    if len(boxes) != 3:
        raise ValueError("Invalid input data. Boxes should contain 3 values.")
    boxes.append(sum(boxes) // 2)


def prepare_response(boxes: List) -> Dict:
    """
    Auxiliary method. Prepare data to use for example in rest api.
    :param boxes: List of boxes in current order
    :return: Dictionary with required boxes info
    """
    if not isinstance(boxes, list):
        raise TypeError("Boxes should be a list")
    if len(boxes) != 4:
        raise ValueError("Invalid input data. Boxes should contain 4 values.")
    return {
        "small_box": boxes[0],
        "medium_box": boxes[1],
        "big_box": boxes[2],
        "outer_box": boxes[3]
    }


def get_number_of_boxes(order_size: int) -> List:
    """
    Calculate number of boxes required for given order size.
    :param order_size: Size of the order
    :return:
    """
    if not isinstance(order_size, int):
        raise TypeError("Order size should be an integer")
    if order_size <= 0 or order_size > 100:
        raise ValueError("Order size should be in range of 0-100")

    total_inner_boxes = get_number_of_inner_boxes(order_size)
    temp = order_size
    last_minimum = None
    result = [0, 0, 0]

    for current_box in range(0, total_inner_boxes):
        boxes_left = total_inner_boxes - current_box
        max_val_in_iter = [val * boxes_left for val
                           in box_sizes]
        diff = [val - temp for val in max_val_in_iter]
        if last_minimum is None or total_inner_boxes > 2 and boxes_left == 1:
            last_minimum = min(val for val in diff if val >= 0)
            idx = diff.index(last_minimum)
        result[idx] += 1
        temp -= box_sizes[idx]
    add_outer_boxes(result)
    return result
