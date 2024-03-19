rm -f data/D_list.txt

for i in {1..5000}
do
    echo "Running $i"
    python3 save_positions.py
    python3 sample_amit.py
done