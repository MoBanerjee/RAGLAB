import pandas as pd

input_file = "/scratch/users/ntu/mohor001/raglab_final/datasets/library_documentation.tsv"
output_file = "/scratch/users/ntu/mohor001/raglab_final/datasets/library_documentation_colbert.tsv"

df = pd.read_csv(input_file, sep="\t")
df['doc_content'] = df['doc_content'].fillna('')
# Flatten the content by removing line breaks and trimming whitespace
df['content'] = df['doc_content'].apply(lambda x: " ".join(line.strip() for line in x.splitlines() if line.strip()))
df['id'] = range(len(df))
df[['id', 'content']].to_csv(output_file, sep="\t", index=False, header=False)
print(f"Reformatted file saved to {output_file}")
