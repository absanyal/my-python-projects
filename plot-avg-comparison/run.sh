mkdir -p data
mkdir -p plots

python3 save_positions.py
time python3 ensemble.py
time python3 sample_amit.py
time python3 sample_muhung.py