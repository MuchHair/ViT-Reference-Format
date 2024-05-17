# ViT-Reference-Format
## Input
```
python split.py --input_bib /root/action.bib --split_dir  nips
```

## Transform

ECCV, CVPR, NIPS and IJCV format are available. Choose one format, i.e., nips
```
python main.py --split_dir  nips --format nips # 
```

## Output
"thesis_out" is the output dir from the former step.
```
python cat.py   --out_file nips.txt --thesis_out nips_out   # 
```