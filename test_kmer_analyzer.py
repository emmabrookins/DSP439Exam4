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
  
from kmer_analyzer import count_kmers_with_context

#Initial test with one kmer to test counting 
def test_count_kmers_with_context_onekmer():
  sequence="ATG"
  k=2
  result=count_kmers_with_context(sequence,k)
  obs=result["AT"]["G"]
  exp=1
  assert obs == exp
  
#Test for repeated kmers
def test_count_kmers_with_context_repeat():
  sequence="ATGATG"
  k=2
  result=count_kmers_with_context(sequence,k)
  obs=result["AT"]["G"]
  exp=2
  assert obs == exp
  
#Test with different next characters 
def test_count_kmers_with_context_different():
  sequence="ATGC"
  k=2
  result=count_kmers_with_context(sequence,k)
  obs1=result["AT"]["G"]
  exp1=1
  assert obs1 == exp1
  obs2=result["TG"]["C"]
  exp2=1
  assert obs2 == exp2

from kmer_analyzer import write_results_to_file
import os 

#First test for one kmer and one next character 
def test_write_results_to_file_single():
  kmer_data={"AT": {"G": 2}}
  output_file="test_output_single.txt"
  write_results_to_file(kmer_data,output_file)
  with open (output_file, "r") as f:
    contents = f.read().strip()
  obs=contents
  exp="AT (2): G:2"
  assert obs == exp
  os.remove(output_file)
  
#Test for one kmer and multiple next characters 
def test_write_results_to_file_one_kmer_multiple_chars():
    kmer_data={"AT": {"C": 1, "G": 2}}
    output_file="test_output_single_kmer_multiple_chars.txt"
    write_results_to_file(kmer_data, output_file)
    with open (output_file, "r") as f:
        contents = f.read().strip()
    obs=contents
    exp = "AT (3): C:1, G:2"
    assert obs == exp
    os.remove(output_file)

#Test for more than one kmer 
def test_write_results_to_file_multiple():
    kmer_data={
        "TG": {"C": 1},
        "AT": {"G": 2}
    }
    output_file="test_output_multiple.txt"
    write_results_to_file(kmer_data, output_file)
    with open(output_file, "r") as f:
        contents = f.read().strip().split("\n")
    obs=contents
    exp = [
        "AT (2): G:2",
        "TG (1): C:1"
    ]
    assert obs == exp
    os.remove(output_file)

#Test to make sure the total is correct 
def test_write_results_to_file_total_correct():
    kmer_data={"AA": {"A": 3, "T": 1}}
    output_file="test_output_total.txt"
    write_results_to_file(kmer_data, output_file)
    with open(output_file, "r") as f:
        contents=f.read().strip()
    obs=contents
    exp="AA (4): A:3, T:1"
    assert obs == exp
    os.remove(output_file)


def test_placeholder():
    assert True
