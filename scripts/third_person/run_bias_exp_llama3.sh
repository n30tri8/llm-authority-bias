#!/bin/bash
CLI="../../cli.py"
Q_BANK="my_qbank_path"

python $CLI measure --qbank $Q_BANK --model "Llama-3-8B-Instruct-Deepinfra" --profession "general neurologist"
python $CLI measure --qbank $Q_BANK --model "Llama-3-8B-Instruct-Deepinfra" --profession "general neurologist" --gender "male"

python $CLI measure --qbank $Q_BANK --model "Llama-3-8B-Instruct-Deepinfra" --profession "general neurologist" --gender "female"

python $CLI measure --qbank $Q_BANK --model "Llama-3-8B-Instruct-Deepinfra" --profession "general neurologist" --gender "male" --position "attending"
python $CLI measure --qbank $Q_BANK --model "Llama-3-8B-Instruct-Deepinfra" --profession "general neurologist" --gender "female" --position "attending"

python $CLI measure --qbank $Q_BANK --model "Llama-3-8B-Instruct-Deepinfra" --profession "general neurologist" --gender "male" --position "student"
python $CLI measure --qbank $Q_BANK --model "Llama-3-8B-Instruct-Deepinfra" --profession "general neurologist" --gender "female" --position "student"

python $CLI measure --qbank $Q_BANK --model "Llama-3-8B-Instruct-Deepinfra" --profession "general neurologist" --gender "male" --position "resident"
python $CLI measure --qbank $Q_BANK --model "Llama-3-8B-Instruct-Deepinfra" --profession "general neurologist" --gender "female" --position "resident"

python $CLI measure --qbank $Q_BANK --model "Llama-3-8B-Instruct-Deepinfra" --profession "general neurologist" --gender "male" --workplace_study "world-class institution"
python $CLI measure --qbank $Q_BANK --model "Llama-3-8B-Instruct-Deepinfra" --profession "general neurologist" --gender "female" --workplace_study "world-class institution"

python $CLI measure --qbank $Q_BANK --model "Llama-3-8B-Instruct-Deepinfra" --profession "general neurologist" --gender "male" --workplace_study "regional-level institution"
python $CLI measure --qbank $Q_BANK --model "Llama-3-8B-Instruct-Deepinfra" --profession "general neurologist" --gender "female" --workplace_study "regional-level institution"

python $CLI measure --qbank $Q_BANK --model "Llama-3-8B-Instruct-Deepinfra" --profession "general neurologist" --position "attending"
python $CLI measure --qbank $Q_BANK --model "Llama-3-8B-Instruct-Deepinfra" --profession "general neurologist" --position "resident"
python $CLI measure --qbank $Q_BANK --model "Llama-3-8B-Instruct-Deepinfra" --profession "general neurologist" --position "student"

python $CLI measure --qbank $Q_BANK --model "Llama-3-8B-Instruct-Deepinfra" --profession "general neurologist" --position "attending" --workplace_study "world-class institution"
python $CLI measure --qbank $Q_BANK --model "Llama-3-8B-Instruct-Deepinfra" --profession "general neurologist" --position "attending" --workplace_study "regional-level institution"
python $CLI measure --qbank $Q_BANK --model "Llama-3-8B-Instruct-Deepinfra" --profession "general neurologist" --position "resident" --workplace_study "world-class institution"
python $CLI measure --qbank $Q_BANK --model "Llama-3-8B-Instruct-Deepinfra" --profession "general neurologist" --position "resident" --workplace_study "regional-level institution"
python $CLI measure --qbank $Q_BANK --model "Llama-3-8B-Instruct-Deepinfra" --profession "general neurologist" --position "student" --workplace_study "world-class institution"
python $CLI measure --qbank $Q_BANK --model "Llama-3-8B-Instruct-Deepinfra" --profession "general neurologist" --position "student" --workplace_study "regional-level institution"

python $CLI measure --qbank $Q_BANK --model "Llama-3-8B-Instruct-Deepinfra" --profession "general neurologist" --workplace_study "world-class institution"
python $CLI measure --qbank $Q_BANK --model "Llama-3-8B-Instruct-Deepinfra" --profession "general neurologist" --workplace_study "regional-level institution"

python $CLI measure --qbank $Q_BANK --model "Llama-3-8B-Instruct-Deepinfra" --profession "general neurologist" --gender "male" --position "attending" --workplace_study "world-class institution"
python $CLI measure --qbank $Q_BANK --model "Llama-3-8B-Instruct-Deepinfra" --profession "general neurologist" --gender "female" --position "attending" --workplace_study "world-class institution"
python $CLI measure --qbank $Q_BANK --model "Llama-3-8B-Instruct-Deepinfra" --profession "general neurologist" --gender "male" --position "attending" --workplace_study "regional-level institution"
python $CLI measure --qbank $Q_BANK --model "Llama-3-8B-Instruct-Deepinfra" --profession "general neurologist" --gender "female" --position "attending" --workplace_study "regional-level institution"
python $CLI measure --qbank $Q_BANK --model "Llama-3-8B-Instruct-Deepinfra" --profession "general neurologist" --gender "male" --position "resident" --workplace_study "world-class institution"
python $CLI measure --qbank $Q_BANK --model "Llama-3-8B-Instruct-Deepinfra" --profession "general neurologist" --gender "female" --position "resident" --workplace_study "world-class institution"
python $CLI measure --qbank $Q_BANK --model "Llama-3-8B-Instruct-Deepinfra" --profession "general neurologist" --gender "male" --position "resident" --workplace_study "regional-level institution"
python $CLI measure --qbank $Q_BANK --model "Llama-3-8B-Instruct-Deepinfra" --profession "general neurologist" --gender "female" --position "resident" --workplace_study "regional-level institution"
python $CLI measure --qbank $Q_BANK --model "Llama-3-8B-Instruct-Deepinfra" --profession "general neurologist" --gender "male" --position "student" --workplace_study "world-class institution"
python $CLI measure --qbank $Q_BANK --model "Llama-3-8B-Instruct-Deepinfra" --profession "general neurologist" --gender "female" --position "student" --workplace_study "world-class institution"
python $CLI measure --qbank $Q_BANK --model "Llama-3-8B-Instruct-Deepinfra" --profession "general neurologist" --gender "male" --position "student" --workplace_study "regional-level institution"
python $CLI measure --qbank $Q_BANK --model "Llama-3-8B-Instruct-Deepinfra" --profession "general neurologist" --gender "female" --position "student" --workplace_study "regional-level institution"