#!/bin/sh
# set sh strict mode
set -o errexit
set -o nounset
IFS=$(printf '\n\t')

cd /home/scu/fetch_scaffold_from_sparc_portal

echo "starting service as"
echo   User    : "$(id "$(whoami)")"
echo   Workdir : "$(pwd)"
echo "..."
echo
# ----------------------------------------------------------------
# This script shall be modified according to the needs in order to run the service
# The inputs defined in ${INPUT_FOLDER}/inputs.json are available as env variables by their key in capital letters
# For example: input_1 -> $INPUT_1

# put the code to execute the service here
# For example:
env
echo "Input folder content:"
ls -al "${INPUT_FOLDER}"
echo "INPUT_1:", $INPUT_1

python main.py $INPUT_1

echo "Input folder content:"
ls -al "${INPUT_FOLDER}"
echo "Output folder content:"
ls -al "${OUTPUT_FOLDER}"
echo "PWD folder content:"
ls -al

cp scaffold.vtk $OUTPUT_FOLDER

# then retrieve the output and move it to the $OUTPUT_FOLDER
# as defined in the output labels
# For example: cp output.csv $OUTPUT_FOLDER or to $OUTPUT_FOLDER/outputs.json using jq
#TODO: Replace following
# cat > "${OUTPUT_FOLDER}"/outputs.json << EOF
# {
#     "output_1":"some_stuff"
# }
# EOF

