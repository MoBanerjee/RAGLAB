from datasets import load_from_disk
import csv

def convert_to_tsv(input_path, output_path):
    dataset = load_from_disk(input_path)
    with open(output_path, mode='w', encoding='utf-8', newline='') as file:
        writer = csv.writer(file, delimiter='\t')
        writer.writerow(dataset['train'].column_names)
        for row in dataset['train']:
            writer.writerow([row[col] for col in dataset['train'].column_names])


    # Convert datasets to TSV
convert_to_tsv(
        "/scratch/users/ntu/mohor001/raglab_final/datasets/programming_solutions",
        "/scratch/users/ntu/mohor001/raglab_final/datasets/programming_solutions.tsv"
    )
convert_to_tsv(
        "/scratch/users/ntu/mohor001/raglab_final/datasets/library_documentation",
        "/scratch/users/ntu/mohor001/raglab_final/datasets/library_documentation.tsv"
    )
convert_to_tsv(
        "/scratch/users/ntu/mohor001/raglab_final/datasets/online_tutorials",
        "/scratch/users/ntu/mohor001/raglab_final/datasets/online_tutorials.tsv"
    )
convert_to_tsv(
        "/scratch/users/ntu/mohor001/raglab_final/datasets/github_repos_python",
        "/scratch/users/ntu/mohor001/raglab_final/datasets/github_repos_python.tsv"
    )
