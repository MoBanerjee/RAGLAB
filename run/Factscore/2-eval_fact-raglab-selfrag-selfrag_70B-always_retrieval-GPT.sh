# export CUDA_VISIBLE_DEVICES=1
python  ./FActScore/factscore/factscorer.py  \
    --input_path './data/eval_results/Factscore/selfrag_reproduction-Factscore-selfrag_llama3_70B-adapter-colbert_api-0614_1214_45/rag_output-selfrag_reproduction|Factscore|selfrag_llama3_70B-adapter|colbert_api|time=0614_1214_45.jsonl' \
    --model_name "retrieval+ChatGPT"\
    --openai_key ./api_keys.txt \
    --data_dir ./data/retrieval/colbertv2.0_passages/wiki2023 \
    --verbose