import pytest
import time
from spec.store import testStore
from step import StepService
import copy

store = copy.deepcopy(testStore)

#step service

#getting user
def test_get_existing_user():
    '''returns step data for existing user'''
    store = testStore
    service = StepService(store)
    assert service.get('james') == store['james']

def test_get_nonexisting_user():
    '''returns None for nonexisting user'''
    store = testStore
    service = StepService(store)
    assert service.get('sasha') == None

#Adding 5 steps
def test_adding_steps_existing_user():
    '''is succesfull when user exists'''
    store = testStore
    service = StepService(store)
    service.add('jenna',time.time(),5)
    assert service.get('jenna')['cumulativeSteps'] == 12323+5

def test_adding_steps_nonexisting_user():
    '''is succesfull when user didn't previously exist'''
    store = testStore
    service = StepService(store)
    service.add('tommy',time.time(),5)
    assert service.get('tommy')['cumulativeSteps'] == 5


