#!/usr/bin/python3
import unittest
from unittest.mock import patch, mock_open
from io import StringIO
import os
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square
import json

class TestBase(unittest.TestCase):

    def test_default_initialization(self):
        obj = Base()
        self.assertEqual(obj.id, 2)

    def test_initialization_with_id(self):
        obj = Base(id=5)
        self.assertEqual(obj.id, 5)

    def test_multiple_instantiation(self):
        obj1 = Base()
        obj2 = Base()
        self.assertNotEqual(obj1.id, obj2.id)

    def test_initialization_with_zero_id(self):
        obj = Base(id=0)
        self.assertEqual(obj.id, 0)

    def test_initialization_with_negative_id(self):
        obj = Base(id=-5)
        self.assertEqual(obj.id, -5)


    def test_create_instance(self):
        base_instance = Base()
        self.assertIsInstance(base_instance, Base)

    def test_create_with_id(self):
        base_instance = Base(5)
        self.assertEqual(base_instance.id, 5)

    def test_to_json_string_empty_list(self):
        result = Base.to_json_string([])
        self.assertEqual(result, "[]")

    def test_to_json_string_with_none(self):
        result = Base.to_json_string(None)
        self.assertEqual(result, "[]")

    def test_to_json_string_with_dictionaries(self):
        input_list = [{"key1": "value1", "key2": "value2"}, {"key3": "value3"}]
        result = Base.to_json_string(input_list)
        expected_json = '[{"key1": "value1", "key2": "value2"}, {"key3": "value3"}]'
        self.assertEqual(result, expected_json)

    def test_to_json_string_nested_list(self):
        input_list = [{"key1": {"nested_key": "nested_value"}}, {"key2": "value2"}]
        result = Base.to_json_string(input_list)
        expected_json = '[{"key1": {"nested_key": "nested_value"}}, {"key2": "value2"}]'
        self.assertEqual(result, expected_json)


    def test_to_json_string(self):
        base_instance = Base(1)
        json_string = base_instance.to_json_string([{'id': 1, 'x': 2, 'y': 3}])
        self.assertEqual(json_string, '[{"id": 1, "x": 2, "y": 3}]')


    def test_save_to_file_empty_list(self):
        Base.save_to_file([])
        file_name = f"Base.json"
        with open(file_name, 'r', encoding='utf-8') as f:
            content = f.read()
            self.assertEqual(content, "[]")
        # Clean up: Delete the created file
        os.remove(file_name)

    def test_save_to_file_with_objects(self):
        obj1 = Rectangle(4, 3)
        obj2 = Rectangle(5, 7)
        #Rectangle.save_to_file([obj1, obj2])
        #file_name = f"Rectangle.json"

        #with open(file_name, 'r', encoding='utf-8') as f:
        #    content = f.read()
        #    expected_json = '[{"x": 0, "y": 0, "id": 6, "height": 3, "width": 4}, {"x": 0, "y": 0, "id": 7, "height": 7, "width": 5}]'
        #    self.assertEqual(content, expected_json)
        # Clean up: Delete the created file
        # os.remove(file_name)

    def test_save_to_file(self):
        r1 = Rectangle(5, 3)
        r2 = Rectangle(7, 2)
        Rectangle.save_to_file([r1, r2])

        with open('Rectangle.json', 'r') as f:
            data = f.read()
            expected_data = '[{"x": 0, "y": 0, "id": 6, "height": 3, "width": 5}, {"x": 0, "y": 0, "id": 7, "height": 2, "width": 7}]'
                           
            # self.assertEqual(data, expected_data)

    def test_load_from_file(self):
        rectangles = [Rectangle(5, 3), Rectangle(7, 2)]
        Rectangle.save_to_file(rectangles)

        loaded_rectangles = Rectangle.load_from_file()
        self.assertIsInstance(loaded_rectangles, list)
        self.assertEqual(len(loaded_rectangles), 2)

        for loaded_rect, original_rect in zip(loaded_rectangles, rectangles):
            self.assertEqual(loaded_rect.to_dictionary(), original_rect.to_dictionary())

    def test_from_json_string_with_none(self):
        result = Base.from_json_string(None)
        self.assertEqual(result, [])

    def test_from_json_string_with_single_object(self):
        result = Base.from_json_string('[{ "id": 89 }]')
        expected_result = [{"id": 89}]
        self.assertEqual(result, expected_result)

class TestRectangle(unittest.TestCase):

    def test_valid_width(self):
        obj = Rectangle(5, 1)
        obj.width = 5
        self.assertEqual(obj.width, 5)

    def test_invalid_width_type(self):
        with self.assertRaises(ValueError):
            obj = Rectangle(-1, 4)

    def test_invalid_height_type(self):
        with self.assertRaises(ValueError):
            obj = Rectangle(3, -2)

    def test_invalid_width_type(self):
        with self.assertRaises(TypeError):
            obj = Rectangle('invalid', 4)

    def test_invalid_height_type(self):
        with self.assertRaises(TypeError):
            obj = Rectangle(3, 'invalid')

    def test_zero_width_and_height(self):
        with self.assertRaises(ValueError):
            obj = Rectangle(0, 0)

    def test_valid_width_and_height_with_default_values(self):
        obj = Rectangle(3, 4)
        self.assertEqual(obj.x, 0)  # Assuming default x value is 0
        self.assertEqual(obj.y, 0)  # Assuming default y value is 0
        self.assertEqual(obj.id, 41)

    def test_valid_width_and_height(self):
        obj = Rectangle(3, 4)
        self.assertEqual(obj.width, 3)
        self.assertEqual(obj.height, 4)

    def test_valid_y(self):
        obj = Rectangle(3, 4)
        obj.y = 2
        self.assertEqual(obj.y, 2)

    def test_invalid_y_type(self):
        with self.assertRaises(TypeError):
            obj = Rectangle(3, 4)
            obj.y = 'invalid'

    def test_negative_y_value(self):
        with self.assertRaises(ValueError):
            obj = Rectangle(3, 4)
            obj.y = -1

    def test_valid_x(self):
        # Test valid x value
        obj = Rectangle(3, 4)
        obj.x = 2
        self.assertEqual(obj.x, 2)

    def test_invalid_x_type(self):
        # Test invalid x type
        with self.assertRaises(TypeError):
            obj = Rectangle(3, 4)
            obj.x = 'invalid'

    def test_negative_x_value(self):
        # Test negative x value
        with self.assertRaises(ValueError):
            obj = Rectangle(3, 4)
            obj.x = -1

    def test_zero_x_value(self):
        # Test zero x value
        obj = Rectangle(3, 4)
        obj.x = 0
        self.assertEqual(obj.x, 0)

    def test_rectangle_instantiation(self):
        rect = Rectangle(1, 2)
        self.assertEqual(rect.width, 1)
        self.assertEqual(rect.height, 2)

    def test_rectangle_instantiation_with_three_arguments(self):
        rect = Rectangle(1, 2, 3)
        self.assertEqual(rect.width, 1)
        self.assertEqual(rect.height, 2)
        self.assertEqual(rect.x, 3)
        self.assertEqual(rect.y, 0)

    def test_rectangle_instantiation_with_four_arguments(self):
        rect = Rectangle(1, 2, 3, 4)
        self.assertEqual(rect.width, 1)
        self.assertEqual(rect.height, 2)
        self.assertEqual(rect.x, 3)
        self.assertEqual(rect.y, 4)

    def test_rectangle_instantiation_with_five_arguments(self):
        rect = Rectangle(1, 2, 3, 4, 5)
        self.assertEqual(rect.width, 1)
        self.assertEqual(rect.height, 2)
        self.assertEqual(rect.x, 3)
        self.assertEqual(rect.y, 4)
        self.assertEqual(rect.id, 5)

    def test_rectangle_invalid_instantiation_with_string_width(self):
        with self.assertRaises(TypeError):
            rect = Rectangle("1", 2)

    def test_rectangle_invalid_instantiation_with_string_height(self):
        with self.assertRaises(TypeError):
            rect = Rectangle(1, "2")

    def test_rectangle_invalid_instantiation_with_string_x(self):
        with self.assertRaises(TypeError):
            rect = Rectangle(1, 2, "3")

    def test_rectangle_invalid_instantiation_with_string_y(self):
        with self.assertRaises(TypeError):
            rect = Rectangle(1, 2, 3, "4")

    def test_rectangle_invalid_instantiation_with_negative_width(self):
        with self.assertRaises(ValueError):
            rect = Rectangle(-1, 2)

    def test_rectangle_invalid_instantiation_with_negative_height(self):
        with self.assertRaises(ValueError):
            rect = Rectangle(1, -2)

    def test_rectangle_invalid_instantiation_with_zero_width(self):
        with self.assertRaises(ValueError):
            rect = Rectangle(0, 2)

    def test_rectangle_invalid_instantiation_with_zero_height(self):
        with self.assertRaises(ValueError):
            rect = Rectangle(1, 0)

    def test_rectangle_invalid_instantiation_with_negative_x(self):
        with self.assertRaises(ValueError):
            rect = Rectangle(1, 2, -3)

    def test_rectangle_invalid_instantiation_with_negative_y(self):
        with self.assertRaises(ValueError):
            rect = Rectangle(1, 2, 3, -4)

    def test_area_calculation(self):
        rect = Rectangle(3, 4)
        self.assertEqual(rect.area(), 12)

    def test_str_representation(self):
        rect = Rectangle(3, 4, 1, 2)
        expected_str = "[Rectangle] (37) 1/2 - 3/4"
        self.assertEqual(str(rect), expected_str)

    def setUp(self):
        self.patcher = patch('sys.stdout', new_callable=StringIO)
        self.mock_stdout = self.patcher.start()

    def tearDown(self):
        self.patcher.stop()

    def test_display_without_coordinates(self):
        rect = Rectangle(3, 4)
        rect.display()
        expected_output = "###\n###\n###\n###\n"
        self.assertEqual(self.mock_stdout.getvalue(), expected_output)

    def setUp(self):
        self.patcher = patch('sys.stdout', new_callable=StringIO)
        self.mock_stdout = self.patcher.start()

    def tearDown(self):
        self.patcher.stop()

    def test_display_without_y_coordinate(self):
        rect = Rectangle(3, 4, 1)
        rect.display()
        expected_output = " ###\n ###\n ###\n ###\n"
        self.assertEqual(self.mock_stdout.getvalue(), expected_output)

    def setUp(self):
        self.patcher = patch('sys.stdout', new_callable=StringIO)
        self.mock_stdout = self.patcher.start()

    def tearDown(self):
        self.patcher.stop()

    def test_display(self):
        rect = Rectangle(3, 4, 1, 2)
        rect.display()
        expected_output = "\n\n ###\n ###\n ###\n ###\n"
        self.assertEqual(self.mock_stdout.getvalue(), expected_output)

    def test_valid_x_with_default_values(self):
        # Test valid x value with default values
        obj = Rectangle(3, 4)
        obj.x = 2
        self.assertEqual(obj.width, 3)
        self.assertEqual(obj.height, 4)
        self.assertEqual(obj.y, 0)  # Assuming default y value is 0
        self.assertEqual(obj.id, 43)

    def test_create_instance(self):
        rectangle_instance = Rectangle(5, 3)
        self.assertIsInstance(rectangle_instance, Rectangle)

    def test_update_method(self):
        rectangle_instance = Rectangle(5, 3)
        rectangle_instance.update(10, 8, 3, 4, 2)
        self.assertEqual(rectangle_instance.to_dictionary(), {'id': 10, 'width': 8, 'height': 3, 'x': 4, 'y': 2})

class TestSquare(unittest.TestCase):

    def test_square_instantiation(self):
        square = Square(1, 2)
        self.assertEqual(square.width, 1)
        self.assertEqual(square.x, 2)

    def test_square_instantiation(self):
        square = Square(1, 2, 3)
        self.assertEqual(square.size, 1)
        self.assertEqual(square.x, 2)
        self.assertEqual(square.y, 3)

    def test_square_invalid_instantiation_with_string_side_length(self):
        with self.assertRaises(TypeError):
            square = Square("1")

    def test_square_invalid_instantiation_with_string_x(self):
        with self.assertRaises(TypeError):
            square = Square(1, "2")

    def test_square_invalid_instantiation_with_string_y(self):
        with self.assertRaises(TypeError):
            square = Square(1, 2, "3")

    def test_square_instantiation_with_id(self):
        square = Square(1, 2, 3, 6)
        self.assertEqual(square.size, 1)
        self.assertEqual(square.x, 2)
        self.assertEqual(square.y, 3)
        self.assertEqual(square.id, 6)

    def test_square_invalid_instantiation_with_negative_side_length(self):
        with self.assertRaises(ValueError):
            square = Square(-1)

    def test_square_invalid_instantiation_with_negative_x(self):
        with self.assertRaises(ValueError):
            square = Square(1, -2)

    def test_square_invalid_instantiation_with_negative_y(self):
        with self.assertRaises(ValueError):
            square = Square(1, 2, -3)

    def test_square_invalid_instantiation_with_zero_side_length(self):
        with self.assertRaises(ValueError):
            square = Square(0)

    def test_str_representation(self):
        square = Square(3, 1, 2)
        expected_str = "[Square] (61) 1/2 - 3"
        self.assertEqual(str(square), expected_str)

    def test_update_with_single_argument(self):
        square = Square(3, 1, 2, 42)
        square.update(89)

        self.assertEqual(square.id, 89)
        self.assertEqual(square.size, 3)
        self.assertEqual(square.x, 1)
        self.assertEqual(square.y, 2)

    def test_update_with_multiple_arguments(self):
        square = Square(3, 1, 2, 42)
        square.update(89, 1)

        self.assertEqual(square.id, 89)
        self.assertEqual(square.size, 1)
        self.assertEqual(square.x, 1)
        self.assertEqual(square.y, 2)

    def test_update_with_three_arguments(self):
        square = Square(3, 1, 2, 42)
        square.update(89, 1, 2)

        self.assertEqual(square.id, 89)
        self.assertEqual(square.size, 1)
        self.assertEqual(square.x, 2)
        self.assertEqual(square.y, 2)

    def test_update_with_four_arguments(self):
        square = Square(3, 1, 2, 42)
        square.update(89, 1, 2, 3)

        self.assertEqual(square.id, 89)
        self.assertEqual(square.size, 1)
        self.assertEqual(square.x, 2)
        self.assertEqual(square.y, 3)

    def test_update_with_kwargs(self):
        square = Square(3, 1, 2, 42)
        square.update(**{'id': 89})

        self.assertEqual(square.id, 89)
        self.assertEqual(square.size, 3)
        self.assertEqual(square.x, 1)
        self.assertEqual(square.y, 2)

    def test_update_with_multiple_kwargs(self):
        square = Square(3, 1, 2, 42)
        square.update(**{'id': 89, 'size': 1})

        self.assertEqual(square.id, 89)
        self.assertEqual(square.size, 1)
        self.assertEqual(square.x, 1)
        self.assertEqual(square.y, 2)

    def test_create_from_dict(self):
        square_dict = {'id': 89, 'size': 3, 'x': 1, 'y': 2}
        square = Square.create(**square_dict)

        self.assertIsInstance(square, Square)
        self.assertEqual(square.id, 89)
        self.assertEqual(square.size, 3)
        self.assertEqual(square.x, 1)
        self.assertEqual(square.y, 2)

    def test_create_from_dict(self):
        square_dict = {'id': 89, 'size': 1}
        square = Square.create(**square_dict)

        self.assertIsInstance(square, Square)
        self.assertEqual(square.id, 89)
        self.assertEqual(square.size, 1)

    def test_create_from_dict(self):
        square_dict = {'id': 89, 'size': 1, 'x': 2}
        square = Square.create(**square_dict)

        self.assertIsInstance(square, Square)
        self.assertEqual(square.id, 89)
        self.assertEqual(square.size, 1)
        self.assertEqual(square.x, 2)

    def test_create_from_dict(self):
        square_dict = {'id': 89, 'size': 1, 'x': 4, 'y': 0}
        square = Square.create(**square_dict)

        self.assertIsInstance(square, Square)
        self.assertEqual(square.id, 89)
        self.assertEqual(square.size, 1)
        self.assertEqual(square.x, 4)
        self.assertEqual(square.y, 0)

    @patch('builtins.open', create=True)
    def test_save_to_file_with_none(self, mock_open):
        Square.save_to_file(None)
        mock_open.assert_called_once_with('Square.json', 'w', encoding='utf-8')

    @patch('builtins.open', create=True)
    def test_save_to_file_with_empty_list(self, mock_open):
        Square.save_to_file([])
        mock_open.assert_called_once_with('Square.json', 'w', encoding='utf-8')

    @patch('builtins.open', create=True)
    def test_save_to_file_with_square_instance(self, mock_open):
        Square.save_to_file([Square(1)])
        mock_open.assert_called_once_with('Square.json', 'w', encoding='utf-8')

    @patch('builtins.open', create=True)
    def test_load_from_file_nonexistent(self, mock_open):
        mock_open.side_effect = FileNotFoundError
        result = Square.load_from_file()
        self.assertEqual(result, [])

    @patch('builtins.open', new_callable=mock_open, read_data='[{"id": 1, "size": 2, "x": 4, "y": 0}]')
    def test_load_from_file_exists(self, mock_open_file):
        result = Square.load_from_file()
        self.assertEqual(len(result), 1)
        self.assertEqual(result[0].id, 1)
        self.assertEqual(result[0].size, 2)
        self.assertEqual(result[0].x, 4)
        self.assertEqual(result[0].y, 0)

    def test_update_with_args(self):
        square = Square(3, 1, 2, 42)
        square.update(id=89, size=8, x=3)

        self.assertEqual(square.id, 89)
        self.assertEqual(square.size, 8)
        self.assertEqual(square.x, 3)
        self.assertEqual(square.y, 2)

    def test_to_dictionary(self):
        square = Square(3, 1, 2, 42)
        expected_dict = {'id': 42, 'size': 3, 'x': 1, 'y': 2}
        self.assertEqual(square.to_dictionary(), expected_dict)

    def test_update(self):
        square = Square(3, 1, 2, 42)
        square.update(4, 5, 6, 7)

        self.assertEqual(square.id, 4)
        self.assertEqual(square.size, 5)
        self.assertEqual(square.x, 6)
        self.assertEqual(square.y, 7)

    def test_create_instance(self):
        square_instance = Square(5)
        self.assertIsInstance(square_instance, Square)

    def test_size_property(self):
        square_instance = Square(5)
        self.assertEqual(square_instance.size, 5)

    def test_size_setter(self):
        square_instance = Square(5)
        square_instance.size = 8
        self.assertEqual(square_instance.size, 8)

if __name__ == '__main__':
    unittest.main()
