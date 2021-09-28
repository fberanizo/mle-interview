#!/bin/python3
"""
Solution to this problem:
https://www.hackerrank.com/challenges/simple-text-editor/problem
"""
import unittest

APPEND = '1'
DELETE = '2'
PRINT = '3'
UNDO = '4'


class TextEditor:
    def __init__(self, initial_string = "", initial_stack = None):
        self.string = initial_string
        self.stack = initial_stack or []

    def appendOp(self, operation, stack=True):
        string_to_add = operation[1]
        
        if stack:
            # adds the 'inverse' operation to the stack
            delete_operation = DELETE, len(string_to_add)
            self.stack.append(delete_operation)

        self.string = f'{self.string}{string_to_add}'

    def deleteOp(self, operation, stack=True):
        number_of_characters_to_delete = int(operation[1])
        
        if stack:
            # adds the 'inverse' operation to the stack
            string_removed = self.string[-number_of_characters_to_delete:]
            append_operation = APPEND, string_removed
            self.stack.append(append_operation)
        
        self.string = self.string[:-number_of_characters_to_delete]

    def printOp(self, operation):
        character_index_to_print = int(operation[1])
        print(self.string[character_index_to_print - 1])
        
    def undoOp(self):
        operation = self.stack.pop()
        operation_type = operation[0]

        if operation_type == APPEND:
            self.appendOp(operation, stack=False)
        elif operation_type == DELETE:
            self.deleteOp(operation, stack=False)

    def process(self, operations):
        for operation in operations:
            operation_type = operation[0]
            
            if operation_type == APPEND:
                self.appendOp(operation)
            elif operation_type == DELETE:
                self.deleteOp(operation)
            elif operation_type == PRINT:
                self.printOp(operation)
            elif operation_type == UNDO:
                self.undoOp()
                

class TestTextEditor(unittest.TestCase):
    def test_append_to_empty_string(self):
        """
        Given a TextEditor with a initial_string "".
        It should add a string to text editor successfully.
        """
        editor = TextEditor()
        operation = APPEND, "abc"
        editor.appendOp(operation)

        self.assertEqual(editor.string, "abc")
        self.assertEqual(editor.stack, [(DELETE, 3,)])
        
    def test_delete_from_abc_string(self):
        """
        Given a TextEditor with a initial_string "abc".
        It should delete "abc" from TextEditor and have an empty string.
        """
        editor = TextEditor(initial_string="abc")
        operation = DELETE, "3"
        editor.deleteOp(operation)
        
        self.assertEqual(editor.string, "")
        self.assertEqual(editor.stack, [(APPEND, "abc",)])
        
    def test_undo_stack_with_delete(self):
        """
        Given a TextEditor with a initial_string "" and a initial_stack [DELETE, 3].
        It should delete "abc" from TextEditor and have an empty string and empty stack.
        """
        editor = TextEditor(initial_string="abc", initial_stack=[(DELETE, 3)])
        editor.undoOp()
        
        self.assertEqual(editor.string, "")
        self.assertEqual(editor.stack, [])
        
    def test_undo_stack_with_append(self):
        """
        Given a TextEditor with a initial_string "" and a initial_stack [APPEND, "abc"].
        It should append "abc" to the text and have an empty stack
        """
        editor = TextEditor(initial_string="", initial_stack=[(APPEND, "abc")])
        editor.undoOp()
        
        self.assertEqual(editor.string, "abc")
        self.assertEqual(editor.stack, [])


if __name__ == '__main__':
    number_of_operations = int(input())
    operations = []
    for index in range(number_of_operations):
        operations.append(input().split())
    
    TextEditor().process(operations)
    unittest.main()
