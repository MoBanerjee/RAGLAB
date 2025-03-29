import pandas as pd

input_file_g = "/scratch/users/ntu/mohor001/raglab_final/datasets/github_repos_python.tsv"
output_file = "/scratch/users/ntu/mohor001/raglab_final/datasets/all_colbert.tsv"

dfg = pd.read_csv(input_file_g, sep="\t")
dfg['text'] = dfg['text'].fillna('')
dfg['content'] = dfg['text'].apply(lambda x: " ".join(line.strip() for line in x.splitlines() if line.strip()))
dfg['id'] = range(len(dfg))
dfg=dfg[['id', 'content']]


input_file_o = "/scratch/users/ntu/mohor001/raglab_final/datasets/online_tutorials.tsv"


dfo = pd.read_csv(input_file_o, sep="\t")
dfo['text'] = dfo['text'].fillna('')
dfo['content'] = dfo['text'].apply(lambda x: " ".join(line.strip() for line in x.splitlines() if line.strip()))
dfo['id'] = range(len(dfo))
dfo=dfo[['id', 'content']]
input_file_p = "/scratch/users/ntu/mohor001/raglab_final/datasets/programming_solutions.tsv"

dfp = pd.read_csv(input_file_p, sep="\t")
dfp['text'] = dfp['text'].fillna('')
dfp['content'] = dfp['text'].apply(lambda x: " ".join(line.strip() for line in x.splitlines() if line.strip()))
dfp['id'] = range(len(dfp))
dfp=dfp[['id', 'content']]
input_file_l = "/scratch/users/ntu/mohor001/raglab_final/datasets/library_documentation.tsv"


dfl = pd.read_csv(input_file_l, sep="\t")
dfl['doc_content'] = dfl['doc_content'].fillna('')

dfl['content'] = dfl['doc_content'].apply(lambda x: " ".join(line.strip() for line in x.splitlines() if line.strip()))
dfl['id'] = range(len(dfl))
dfl=dfl[['id', 'content']]


df= pd.concat([dfo, dfp, dfl, dfg], ignore_index=True)
df["id"]=range(len(df))
df[['id', 'content']].to_csv(output_file, sep="\t", index=False, header=False)
print(f"Reformatted file saved to {output_file}")
