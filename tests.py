import pytest
from model import Question


def test_question_correct_values():
    question = Question(title='Pergunta', points=5)
    assert 'Pergunta' == question.title
    assert 5 == question.points

def test_create_question():
    question = Question(title='q1')
    assert question.id != None

def test_choice_text_empty():
    question = Question(title='Pergunta')
    with pytest.raises(Exception):
        question.add_choice('', False)

def test_choice_text_too_long():
    question = Question(title='Pergunta')
    with pytest.raises(Exception):
        question.add_choice('a'*201, False)

def test_create_multiple_questions():
    question1 = Question(title='q1')
    question2 = Question(title='q2')
    assert question1.id != question2.id

def test_add_choice_increases_length():
    question = Question(title='Pergunta')
    initial_len = len(question.choices)
    question.add_choice('Alternativa', False)
    assert len(question.choices) == initial_len + 1

def test_create_question_with_invalid_title():
    with pytest.raises(Exception):
        Question(title='')
    with pytest.raises(Exception):
        Question(title='a'*201)
    with pytest.raises(Exception):
        Question(title='a'*500)

def test_question_default_points():
    question = Question(title='Pergunta')
    assert question.points == 1

def test_create_question_with_valid_points():
    question = Question(title='q1', points=1)
    assert question.points == 1
    question = Question(title='q1', points=100)
    assert question.points == 100

def test_question_invalid_points_low():
    with pytest.raises(Exception):
        Question(title='Pergunta', points=0)

def test_question_invalid_points_high():
    with pytest.raises(Exception):
        Question(title='Pergunta', points=101)

def test_create_choice():
    question = Question(title='q1')
    
    question.add_choice('a', False)

    choice = question.choices[0]
    assert len(question.choices) == 1
    assert choice.text == 'a'
    assert not choice.is_correct

def test_add_multiple_choices():
    question = Question(title='Pergunta')
    question.add_choice('Alternativa A', False)
    question.add_choice('Alternativa B', True)
    assert len(question.choices) == 2

def test_choice_is_correct_flag():
    question = Question(title='Pergunta')
    question.add_choice('Alternativa', True)
    assert question.choices[0].is_correct

def test_choice_is_incorrect_flag():
    question = Question(title='Pergunta')
    question.add_choice('Alternativa', False)
    assert not question.choices[0].is_correct


### exemplo de fixture:

@pytest.fixture
def question_with_choices():
    question = Question(title='Pergunta com escolhas')
    question.add_choice('errou1', False)
    question.add_choice('UHUL', True)
    question.add_choice('errou2', False)
    return question

def test_question_with_choices_count(question_with_choices):
    assert len(question_with_choices.choices) == 3

def test_question_with_choices_correct_choice(question_with_choices):
    correct_choices = [c for c in question_with_choices.choices if c.is_correct]
    assert len(correct_choices) == 1
    assert correct_choices[0].text == 'UHUL'