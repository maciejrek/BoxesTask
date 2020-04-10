from boxes import get_number_of_boxes, prepare_response

for order_size in range(1, 101):
    print(
        f"Order size: {order_size}:\n"
        f"{prepare_response(get_number_of_boxes(order_size))}")
