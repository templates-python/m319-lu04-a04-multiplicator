import pytest
from main import multiplicator

def test_multiplicator_int(monkeypatch, capsys):
    input_values = ['5', '3']
    input_generator = iter(input_values)
    prompts = []

    def mock_input(prompt):
        prompts.append(prompt)
        return next(input_generator)

    monkeypatch.setattr('builtins.input', mock_input)
    multiplicator()
    captured = capsys.readouterr()

    # Check the input prompts
    assert prompts == [
        'Please provide factor one:\n',
        'Please provide factor two:\n'
    ]

    # Check the printed output
    assert captured.out == (
        'Welcome to the MULTIPLICATOR!\n'
        'Result: 15.0\n'
    )

def test_multiplicator_float(monkeypatch, capsys):
    input_values = ['5.5', '3']
    input_generator = iter(input_values)
    prompts = []

    def mock_input(prompt):
        prompts.append(prompt)
        return next(input_generator)

    monkeypatch.setattr('builtins.input', mock_input)
    multiplicator()
    captured = capsys.readouterr()

    # Check the input prompts
    assert prompts == [
        'Please provide factor one:\n',
        'Please provide factor two:\n'
    ]

    # Check the printed output
    assert captured.out == (
        'Welcome to the MULTIPLICATOR!\n'
        'Result: 16.5\n'
    )