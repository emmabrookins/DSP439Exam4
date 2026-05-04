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
  
from kmer_analyzer import update_kmer_count

#Initial test of adding a new kmer and next character 
def test_update_kmer_count_new():
  kmer_data={}
  kmer="AT"
  next_char="G"
  result=update_kmer_count(kmer_data,kmer,next_char)
  obs=result["AT"]["G"]
  exp=1
  assert obs == exp
  
#Test for adding to an already existing kmer 
def test_update_kmer_count_add():
  kmer_data={"AT": {"G":1}}
  kmer="AT"
  next_char="G"
  result=update_kmer_count(kmer_data,kmer,next_char)
  obs=result["AT"]["G"]
  exp=2
  assert obs == exp
  
#Test for adding a new next character to an already existing kmer 
def test_update_kmer_count_newnextchar():
  kmer_data={"AT": {"G":1}}
  kmer="AT"
  next_char="C"
  result=update_kmer_count(kmer_data,kmer,next_char)
  obs=result["AT"]["C"]
  exp=1 
  assert obs == exp
  

def test_placeholder():
    assert True
