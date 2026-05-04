import pytest
import kmer_analyzer
from kmer_analyzer import validate_sequence

#Test to make sure the function recognizes a valid sequence 
def test_validate_sequence_isvalid():
  sequence="ACTG"
  k=2
  result=validate_sequence(sequence,k)
  obs=result
  exp=True 
  assert obs == exp
  
#Test a sequence that is too short
def test_validate_sequence_short():
  sequence="A"
  k=2
  result=validate_sequence(sequence,k)
  obs=result 
  exp=False
  assert obs == exp
  
#Test a sequence with a digit in it 
def test_validate_sequence_digit():
  sequence="AC3T"
  k=2
  result=validate_sequence(sequence,k)
  obs=result 
  exp=False 
  assert obs == exp
  

def test_placeholder():
    assert True
