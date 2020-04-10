import unittest
from boxes import (
    get_number_of_inner_boxes,
    get_number_of_boxes,
    add_outer_boxes,
    prepare_response
)


class TestBoxes(unittest.TestCase):
    resp_vec = [
        [1, 0, 0, 0], [1, 0, 0, 0], [1, 0, 0, 0],
        [0, 1, 0, 0], [0, 1, 0, 0], [0, 1, 0, 0],
        [0, 0, 1, 0], [0, 0, 1, 0], [0, 0, 1, 0],
        [0, 2, 0, 1], [0, 2, 0, 1], [0, 2, 0, 1],
        [0, 0, 2, 1], [0, 0, 2, 1], [0, 0, 2, 1],
        [0, 0, 2, 1], [0, 0, 2, 1], [0, 0, 2, 1],
        [1, 0, 2, 1], [1, 0, 2, 1], [1, 0, 2, 1],
        [0, 1, 2, 1], [0, 1, 2, 1], [0, 1, 2, 1],
        [0, 0, 3, 1], [0, 0, 3, 1], [0, 0, 3, 1],
        [1, 0, 3, 2], [1, 0, 3, 2], [1, 0, 3, 2],
        [0, 1, 3, 2], [0, 1, 3, 2], [0, 1, 3, 2],
        [0, 0, 4, 2], [0, 0, 4, 2], [0, 0, 4, 2]
    ]

    def test_get_number_of_inner_boxes_wrong_input(self):
        """
        Provide wrong input parameters.
        We expect TypeError to be raised.
        """
        with self.assertRaises(TypeError):
            get_number_of_inner_boxes('wrong_input')

    def test_get_number_of_inner_boxes(self):
        """
        Number of inner boxes should change according to order size.
        Check method result with known values.
        """
        self.assertEqual(1, get_number_of_inner_boxes(5))
        self.assertEqual(3, get_number_of_inner_boxes(25))
        self.assertEqual(5, get_number_of_inner_boxes(45))

    def test_add_outer_boxes_wrong_input(self):
        """
        Provide wrong input parameters.
        We expect TypeError to be raised for the first test,
        and ValueError for the second one.
        """
        with self.assertRaises(TypeError):
            add_outer_boxes('wrong_input')
        with self.assertRaises(ValueError):
            add_outer_boxes([1, 2])
        with self.assertRaises(ValueError):
            add_outer_boxes([1, 2, 7, 3])

    def test_add_outer_boxes(self):
        """
        Number of outer boxes should change,
        according to the number of inner boxes.
        Check method result with known values.
        """
        result = self.resp_vec[0]
        inner_boxes = result[:-1]
        add_outer_boxes(inner_boxes)
        self.assertEqual(result, inner_boxes)

        result = self.resp_vec[27]
        inner_boxes = result[:-1]
        add_outer_boxes(inner_boxes)
        self.assertEqual(result, inner_boxes)

    def test_get_number_of_boxes_wrong_input(self):
        """
        Provide wrong input parameters.
        We expect TypeError to be raised for the first test,
        and ValueError for the second one.
        """
        with self.assertRaises(TypeError):
            get_number_of_boxes('wrong_input')

        with self.assertRaises(ValueError):
            get_number_of_boxes(0)
        with self.assertRaises(ValueError):
            get_number_of_boxes(101)

    def test_get_number_of_boxes(self):
        """
        Number of boxes should change,
        according to the number of the order size.
        Check method result with known values.
        """
        for i in range(1, 37):
            self.assertEqual(self.resp_vec[i - 1], get_number_of_boxes(i))

    def test_prepare_response_wrong_input(self):
        """
        Provide wrong input parameters.
        We expect TypeError to be raised for the first test,
        and ValueError for the second one.
        """
        with self.assertRaises(TypeError):
            prepare_response('wrong_input')

        with self.assertRaises(ValueError):
            prepare_response([1, 0])

    def test_prepare_response(self):
        """
        This method should return dict with data, according to the result
        of get_number_of_boxes method.
        Check method result with known values.
        """
        input_data = self.resp_vec[10]
        expected_response = {
            "small_box": input_data[0],
            "medium_box": input_data[1],
            "big_box": input_data[2],
            "outer_box": input_data[3]
        }
        self.assertEqual(expected_response, prepare_response(input_data))
