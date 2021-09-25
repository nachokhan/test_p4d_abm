# test_p4d_abm

# Setup
## Install requirements
pip install -r requirements.txt
## Copy configuration files
for i in $(find . -name '*._sample'); do cp "$i" "${i%.*}".py; done;