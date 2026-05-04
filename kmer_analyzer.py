import sys

def validate_sequence(sequence, k):
  """
  Checks to see if the input DNA sequence is valid for k-mer analyzation.
  
  Args:
    sequence (str): The inputted DNA sequence we are checking 
    k (int): The length of each k-mer
  
  Returns:
    bool: True is the length of the sequence is shorter than the length of the 
    k-mer and the sequence contains no digits, false otherwise.
    
  """
  #Check to see if the length of the sequence is less than k
  if len(sequence) < k:
      #return false if the length of the sequence is less than k
      return False
  #Loop through each of the characters in the DNA sequence
  for nucleotide in sequence:
      #Check to see if the character is a number
      if nucleotide in '1234567890':
          #return false if the character is a number. 
          return False
  #return true if the sequence is long enough and contains no numbers
  return True

def update_kmer_count(kmer_data, kmer, next_char):
  """
  Updates the k-mer data dictionary with each new k-mer and what the next 
  character will be. 
  
  Args:
    kmer_data(dict): Dictionary that stores each k-mer, and the 
    frequency of the following characters. 
    kmer(str): K-mer that is being counted.
    next_char(str): Next character that follows the k-mer. 
    
  Returns:
    kmer_data (dict): The new k-mer dictionary.
  
  """
  #Check to see if the k-mer is new (not already analyzed)
  if kmer not in kmer_data:
      #if the k-mer has not been seen before create a new entry in the 
      #dictionary, keep the entry empty for now so we are starting with a blank
      #slate
      kmer_data[kmer] = {}
    
  #Check to see if the nect character has not been seen after the current k-mer
  if next_char not in kmer_data[kmer]:
      #initialize the count of the next character
      kmer_data[kmer][next_char] = 0
  #Add one to the count for the next character 
  kmer_data[kmer][next_char] += 1

  #Return the updated k-mer data dictionary
  return kmer_data

def count_kmers_with_context(sequence, k):
  """
  Counts all of the k-mers in a sequence and keeps track of the next character 
  for each k-mer.
  
  Args:
    sequence(str): The inputted DNA sequence we are analyzing 
    k(int): The length of the sequence
    
  Returns:
    kmer_data (dict):Dictionary that stores each k-mer and the 
    frequencies of the next characters. 
    
  """
  #Create an empty k-mer data dictionary
  kmer_data = {}
    
  #Loop through the sequence and stop before the last k characters to make 
  #sure there is always a next character
  for i in range(len(sequence) - k):
      #Extract k-mer of length k from the DNA sequence, starting at index i
      kmer = sequence[i:i+k]
      #Extract the next character that comes right after the k-mer
      next_char = sequence[i+k]
        
      #Update the dictionary with the k-mer and the next character 
      kmer_data = update_kmer_count(kmer_data, kmer, next_char)
    
  #Return the k-mer data dictionary of the k-mers and the next character
  return kmer_data


def write_results_to_file(kmer_data, output_filename):
  """
  Writes the frequency of each k-mer and the frequencies of the of the next 
  characters into an output file. 
  
  Args:
    kmer_data (dict): Dictionary containing each k-mer and the 
    frequencies of the next character.
    output_filename (str): The name of the output file that the results will be 
    put into. 
    
  Returns:
  None
  """
  #Sort all of the k-mers alphabetically
  sorted_kmers = sorted(kmer_data.keys())
    
  #Open the output file and put in write mode 
  with open(output_filename, 'w') as f:
      #Loop through each of the kmers in alphabetical order 
      for kmer in sorted_kmers:
          #for the k-mer, get the frequencies of the next character from the 
          #dictionary
          next_chars = kmer_data[kmer]
          #compute the total number of each kmer
          total=sum(next_chars.values())
          #Create a new string for the next charatcers that includes the 
          #character and its frequency 
          next_char_str = ", ".join(
              f"{char}:{freq}" 
              #go through each of the characters and its frequency in the next 
              #characters 
              for char, freq in sorted(next_chars.items())
          )
            
          #Write a line to the file with the frequency of each k-mer and its 
          #next-character data
          f.write(f"{kmer} ({total}): {next_char_str}\n")


def main():
  """
  Reads all of the inputs, outputs messages for the user, processes DNA 
  sequences, and writes the results in an output file.
  
  Args:
    None 
  
  Returns:
    None
    
  """
  #Read the first argument in the command line (input file)
  sequence_file = sys.argv[1]
  #Read the second argument in the command line (length of k-mer)
  k = int(sys.argv[2])
  #Read the third argument in the command line (output file)
  output_file = sys.argv[3]
    
  #Print a message to tell the user which file the sequences are being read
  #from
  print(f"Reading sequences from {sequence_file}...")

  #Open the input file and read each of the sequences
  with open(sequence_file, 'r') as f:
      #go through each sequence
      for sequence in f:
          #remove leading and trailing characters from each sequence by using
          #.strip()
          sequence = sequence.strip()

          #Check if the sequence is not valid for k-mer analysis
          if not validate_sequence(sequence, k):
              #print a warning message for the user and skip the sequence 
              print(f"  Warning: Skipping sequence")
              continue
            
          #For the sequence, count all of the k-mers and their next characters
          kmer_data = count_kmers_with_context(sequence, k) 
          #write the results to the output file 
          write_results_to_file(kmer_data, output_file)

if __name__ == '__main__':
    main()
