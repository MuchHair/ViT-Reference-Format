

python split.py --input_bib /data/xubin/code/Latex/egbib.bib --split_dir  /data/xubin/code/Latex/egbib_eccv
python main.py --split_dir /data/xubin/code/Latex/egbib_eccv --format bishe_thesis # choose a right format
python cat.py   --out_file /data/xubin/code/Latex/egbib_eccv.txt --thesis_out /data/xubin/code/Latex/egbib_eccv_out       #cat multiple output txt into a single .txt