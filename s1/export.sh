docker export s1_s1_1 -o ex.tar
mkdir ex
mv ex.tar ex/
cd ex
tar -xf ex.tar
