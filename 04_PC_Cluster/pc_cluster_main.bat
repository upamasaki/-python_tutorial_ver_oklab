echo %USERNAME%
set read_path=./%USERNAME%/run_IDlist.txt
echo %read_path%


start python pc_cluster_master_sample.py %read_path%1
start python pc_cluster_master_sample.py %read_path%2
