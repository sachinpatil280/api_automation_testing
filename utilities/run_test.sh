pip install -r "../configurations/requirements.txt"

MARKER="regression"

dir=$PWD
cd "$dir"/../test_cases || exit

pytest -m $MARKER --html=../results/report.html
