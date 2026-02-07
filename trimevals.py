import os
import random

input_file = r"C:\Users\Richard\Coding_Projects\pozpuz\backend\data\evals.jsonl"
output_file = r"C:\Users\Richard\Coding_Projects\pozpuz\backend\data\evals_trim.jsonl"
sample_size = 25000

def get_random_sample(file_path, num_samples):
    file_size = os.path.getsize(file_path)
    samples = set()
    
    with open(file_path, 'rb') as f:
        while len(samples) < num_samples:
            # Jump to a random byte
            pos = random.randint(0, file_size - 1024) # Leave room for a line
            f.seek(pos)
            
            # Skip the current partial line and move to the start of the next full line
            f.readline() 
            line = f.readline().decode('utf-8').strip()
            
            if line:
                samples.add(line)
                
    return samples

# Execute and write
sampled_lines = get_random_sample(input_file, sample_size)

with open(output_file, 'w', encoding='utf-8') as outfile:
    for line in sampled_lines:
        outfile.write(line + '\n')