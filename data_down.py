from datasets import load_dataset

# Download datasets
#programming_solutions = load_dataset("code-rag-bench/programming-solutions")
#programming_solutions.save_to_disk("/scratch/users/ntu/mohor001/raglab_final/datasets/programming_solutions")
#del programming_solutions
#library_documentation = load_dataset("code-rag-bench/library-documentation")
#library_documentation.save_to_disk("/scratch/users/ntu/mohor001/raglab_final/datasets/library_documentation")
#del library_documentation
#online_tutorials = load_dataset("code-rag-bench/online-tutorials")
#online_tutorials.save_to_disk("/scratch/users/ntu/mohor001/raglab_final/datasets/online_tutorials")
#del online_tutorials
github_repos_python = load_dataset("code-rag-bench/github-repos-python")
github_repos_python.save_to_disk("/scratch/users/ntu/mohor001/raglab_final/datasets/github_repos_python")
del github_repos
# Save datasets to disk
#programming_solutions.save_to_disk("/scratch/users/ntu/mohor001/raglab_final/datasets/programming_solutions")
#library_documentation.save_to_disk("/scratch/users/ntu/mohor001/raglab_final/datasets/library_documentation")
#online_tutorials.save_to_disk("/scratch/users/ntu/mohor001/raglab_final/datasets/online_tutorials")
#github_repos_python.save_to_disk("/scratch/users/ntu/mohor001/raglab_final/datasets/github_repos_python")
