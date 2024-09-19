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

    # Check the printed output and format
    expected_output = 'Result: 15.00\n'
    actual_output = captured.out.splitlines()[-1]  # Fetch the result line only
    assert actual_output == expected_output, (
        f"Output format error: expected '{expected_output}' but got '{actual_output}'. "
        "Check f-string formatting to ensure two digits after the decimal point."
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

    # Check the printed output and format
    expected_output = 'Result: 16.50\n'
    actual_output = captured.out.splitlines()[-1]  # Fetch the result line only
    assert actual_output == expected_output, (
        f"Output format error: expected '{expected_output}' but got '{actual_output}'. "
        "Check f-string formatting to ensure two digits after the decimal point."
    )
