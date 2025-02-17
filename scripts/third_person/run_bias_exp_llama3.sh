#!/bin/bash
Q_BANK="my_address"

python ../cli.py measure --qbank $Q_BANK --model "Llama-3-8B-Instruct-Deepinfra" --profession "general neurologist"
python ../cli.py measure --qbank $Q_BANK --model "Llama-3-8B-Instruct-Deepinfra" --profession "general neurologist" --gender "male"

python ../cli.py measure --qbank $Q_BANK --model "Llama-3-8B-Instruct-Deepinfra" --profession "general neurologist" --gender "female"

python ../cli.py measure --qbank $Q_BANK --model "Llama-3-8B-Instruct-Deepinfra" --profession "general neurologist" --gender "male" --position "attending"
python ../cli.py measure --qbank $Q_BANK --model "Llama-3-8B-Instruct-Deepinfra" --profession "general neurologist" --gender "female" --position "attending"

python ../cli.py measure --qbank $Q_BANK --model "Llama-3-8B-Instruct-Deepinfra" --profession "general neurologist" --gender "male" --position "student"
python ../cli.py measure --qbank $Q_BANK --model "Llama-3-8B-Instruct-Deepinfra" --profession "general neurologist" --gender "female" --position "student"

python ../cli.py measure --qbank $Q_BANK --model "Llama-3-8B-Instruct-Deepinfra" --profession "general neurologist" --gender "male" --position "resident"
python ../cli.py measure --qbank $Q_BANK --model "Llama-3-8B-Instruct-Deepinfra" --profession "general neurologist" --gender "female" --position "resident"

python ../cli.py measure --qbank $Q_BANK --model "Llama-3-8B-Instruct-Deepinfra" --profession "general neurologist" --gender "male" --workplace_study "world-class institution"
python ../cli.py measure --qbank $Q_BANK --model "Llama-3-8B-Instruct-Deepinfra" --profession "general neurologist" --gender "female" --workplace_study "world-class institution"

python ../cli.py measure --qbank $Q_BANK --model "Llama-3-8B-Instruct-Deepinfra" --profession "general neurologist" --gender "male" --workplace_study "regional-level institution"
python ../cli.py measure --qbank $Q_BANK --model "Llama-3-8B-Instruct-Deepinfra" --profession "general neurologist" --gender "female" --workplace_study "regional-level institution"

python ../cli.py measure --qbank $Q_BANK --model "Llama-3-8B-Instruct-Deepinfra" --profession "general neurologist" --position "attending"
python ../cli.py measure --qbank $Q_BANK --model "Llama-3-8B-Instruct-Deepinfra" --profession "general neurologist" --position "resident"
python ../cli.py measure --qbank $Q_BANK --model "Llama-3-8B-Instruct-Deepinfra" --profession "general neurologist" --position "student"

python ../cli.py measure --qbank $Q_BANK --model "Llama-3-8B-Instruct-Deepinfra" --profession "general neurologist" --position "attending" --workplace_study "world-class institution"
python ../cli.py measure --qbank $Q_BANK --model "Llama-3-8B-Instruct-Deepinfra" --profession "general neurologist" --position "attending" --workplace_study "regional-level institution"
python ../cli.py measure --qbank $Q_BANK --model "Llama-3-8B-Instruct-Deepinfra" --profession "general neurologist" --position "resident" --workplace_study "world-class institution"
python ../cli.py measure --qbank $Q_BANK --model "Llama-3-8B-Instruct-Deepinfra" --profession "general neurologist" --position "resident" --workplace_study "regional-level institution"
python ../cli.py measure --qbank $Q_BANK --model "Llama-3-8B-Instruct-Deepinfra" --profession "general neurologist" --position "student" --workplace_study "world-class institution"
python ../cli.py measure --qbank $Q_BANK --model "Llama-3-8B-Instruct-Deepinfra" --profession "general neurologist" --position "student" --workplace_study "regional-level institution"

python ../cli.py measure --qbank $Q_BANK --model "Llama-3-8B-Instruct-Deepinfra" --profession "general neurologist" --workplace_study "world-class institution"
python ../cli.py measure --qbank $Q_BANK --model "Llama-3-8B-Instruct-Deepinfra" --profession "general neurologist" --workplace_study "regional-level institution"

python ../cli.py measure --qbank $Q_BANK --model "Llama-3-8B-Instruct-Deepinfra" --profession "general neurologist" --gender "male" --position "attending" --workplace_study "world-class institution"
python ../cli.py measure --qbank $Q_BANK --model "Llama-3-8B-Instruct-Deepinfra" --profession "general neurologist" --gender "female" --position "attending" --workplace_study "world-class institution"
python ../cli.py measure --qbank $Q_BANK --model "Llama-3-8B-Instruct-Deepinfra" --profession "general neurologist" --gender "male" --position "attending" --workplace_study "regional-level institution"
python ../cli.py measure --qbank $Q_BANK --model "Llama-3-8B-Instruct-Deepinfra" --profession "general neurologist" --gender "female" --position "attending" --workplace_study "regional-level institution"
python ../cli.py measure --qbank $Q_BANK --model "Llama-3-8B-Instruct-Deepinfra" --profession "general neurologist" --gender "male" --position "resident" --workplace_study "world-class institution"
python ../cli.py measure --qbank $Q_BANK --model "Llama-3-8B-Instruct-Deepinfra" --profession "general neurologist" --gender "female" --position "resident" --workplace_study "world-class institution"
python ../cli.py measure --qbank $Q_BANK --model "Llama-3-8B-Instruct-Deepinfra" --profession "general neurologist" --gender "male" --position "resident" --workplace_study "regional-level institution"
python ../cli.py measure --qbank $Q_BANK --model "Llama-3-8B-Instruct-Deepinfra" --profession "general neurologist" --gender "female" --position "resident" --workplace_study "regional-level institution"
python ../cli.py measure --qbank $Q_BANK --model "Llama-3-8B-Instruct-Deepinfra" --profession "general neurologist" --gender "male" --position "student" --workplace_study "world-class institution"
python ../cli.py measure --qbank $Q_BANK --model "Llama-3-8B-Instruct-Deepinfra" --profession "general neurologist" --gender "female" --position "student" --workplace_study "world-class institution"
python ../cli.py measure --qbank $Q_BANK --model "Llama-3-8B-Instruct-Deepinfra" --profession "general neurologist" --gender "male" --position "student" --workplace_study "regional-level institution"
python ../cli.py measure --qbank $Q_BANK --model "Llama-3-8B-Instruct-Deepinfra" --profession "general neurologist" --gender "female" --position "student" --workplace_study "regional-level institution"