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
    if len(sequence) < k:
        return False
    for nucleotide in sequence:
        if nucleotide in '1234567890':
            return False
    return True

def update_kmer_count(kmer_data, kmer, next_char):
  """
  Updates the k-mer data dictionary with each new k-mer and what the next 
  character will be. 
  
  Args:
    kmer_data(dict): Dictionary that stores the count of each k-mer, and the 
    frequency of the following characters. 
    kmer(str): K-mer that is being counted.
    next_char(str): Next character that follows the k-mer. 
    
  Returns:
    kmer_data (dict): The new k-mer count dictionary.
  
  """
    if kmer not in kmer_data:
        kmer_data[kmer] = {'count': 1, 'next_chars': {}}
    
    kmer_data[kmer]['count'] += 1
    
    if next_char not in kmer_data[kmer]['next_chars']:
        kmer_data[kmer]['next_chars'][next_char] = 0
    kmer_data[kmer]['next_chars'][next_char] += 1

    return kmer_data

def count_kmers_with_context(sequence, k):
  """
  Counts all of the k-mers in a sequence and keeps track of the next character 
  for each k-mer.
  
  Args:
    sequence(str): The inputted DNA sequence we are analyzing 
    k(int): The length of the sequence
    
  Returns:
    kmer_data (dict):Dictionary that stores the count of each k-mer and the 
    frequencies of the next characters. 
    
  """
    kmer_data = {}
    
    for i in range(len(sequence) - k):
        kmer = sequence[i:i+k]
        next_char = sequence[i+k]
        
        kmer_data = update_kmer_count(kmer_data, kmer, next_char)
    
    return kmer_data


def write_results_to_file(kmer_data, output_filename):
  """
  Writes the sorted k-mer data and the frequencies of the of the next characters
  into an output file. 
  
  Args:
    kmer_data (dict): Dictionary containing the counts of each k-mer and the 
    frequencies of the next character.
    output_filename (str): The name of the output file that the results will be 
    put into. 
    
  Returns:
  None
  """
    sorted_kmers = sorted(kmer_data.keys())
    
    with open(output_filename, 'w') as f:
        for kmer in sorted_kmers:
            next_chars = kmer_data[kmer]['next_chars']
            
            next_char_str = " ".join(
                f"{char}:{freq}" 
                for char, freq in sorted(next_chars.items())
            )
            
            f.write(f"{kmer} {next_char_str}\n")


def main():
  """
  Reads all of the inputs, outputs messages for the user, processes DNA 
  sequences, and writes the results in an output file.
  
  Args:
    None 
  
  Returns:
    None
    
  """
    sequence_file = sys.argv[1]
    k = int(sys.argv[2])
    output_file = sys.argv[3]
    
    print(f"Reading sequences from {sequence_file}...")

    with open(sequence_file, 'r') as f:
        for sequence in f:
            sequence = sequence.strip()

            if not validate_sequence(sequence, k):
                print(f"  Warning: Skipping sequence")
                continue
            
            kmer_data = count_kmers_with_context(sequence, k) 
            
            write_results_to_file(kmer_data, output_file)

if __name__ == '__main__':
    main()
