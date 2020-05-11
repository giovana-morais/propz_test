# Propz Data Science Test

This test is organized as follows:

- The main file is `main.py`. It calls questions that needed implementation;
- Code questions are implemented in separated files `question/question_<number>.py`
- Tests for the above are in `test/test_question_<number>.py`
- Theoretical questions are implemented together in a LaTeX file
`theory.tex`, as well as the .pdf file `theory.pdf`

## Getting Started

You should have `Python 3.8` to run this project. Some external
libraries are needed, like `numpy` and `pytest`. I recommend you to create
a [`virtualenv`](https://docs.python.org/3/library/venv.html), so you it
won't break any-python-thing you might have installed on your machine.

To run the main program, install, create and activate your `virtualenv`

`pip install virtualenv`

`virtualenv -p python3 venv`

`source venv/bin/activate`

Install all depedencies

`pip install -r requirements.txt`

## Running tests

Then install the `question` package to help `pytest` find our files

`pip install -e .`

Finally, `cd` to `tests/` and run

`pytest <test_file> -v`
