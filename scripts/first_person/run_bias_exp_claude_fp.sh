#!/bin/bash
CLI="../../cli.py"
Q_BANK="my_qbank_path"

python $CLI measure --qbank $Q_BANK --model "claude-3-haiku-20240307" --profession "general neurologist" --first_person
python $CLI measure --qbank $Q_BANK --model "claude-3-haiku-20240307" --profession "general neurologist" --gender "male" --first_person

python $CLI measure --qbank $Q_BANK --model "claude-3-haiku-20240307" --profession "general neurologist" --gender "female" --first_person

python $CLI measure --qbank $Q_BANK --model "claude-3-haiku-20240307" --profession "general neurologist" --gender "male" --position "attending" --first_person
python $CLI measure --qbank $Q_BANK --model "claude-3-haiku-20240307" --profession "general neurologist" --gender "female" --position "attending" --first_person

python $CLI measure --qbank $Q_BANK --model "claude-3-haiku-20240307" --profession "general neurologist" --gender "male" --position "student" --first_person
python $CLI measure --qbank $Q_BANK --model "claude-3-haiku-20240307" --profession "general neurologist" --gender "female" --position "student" --first_person

python $CLI measure --qbank $Q_BANK --model "claude-3-haiku-20240307" --profession "general neurologist" --gender "male" --position "resident" --first_person
python $CLI measure --qbank $Q_BANK --model "claude-3-haiku-20240307" --profession "general neurologist" --gender "female" --position "resident" --first_person

python $CLI measure --qbank $Q_BANK --model "claude-3-haiku-20240307" --profession "general neurologist" --gender "male" --workplace_study "world-class institution" --first_person
python $CLI measure --qbank $Q_BANK --model "claude-3-haiku-20240307" --profession "general neurologist" --gender "female" --workplace_study "world-class institution" --first_person

python $CLI measure --qbank $Q_BANK --model "claude-3-haiku-20240307" --profession "general neurologist" --gender "male" --workplace_study "regional-level institution" --first_person
python $CLI measure --qbank $Q_BANK --model "claude-3-haiku-20240307" --profession "general neurologist" --gender "female" --workplace_study "regional-level institution" --first_person

python $CLI measure --qbank $Q_BANK --model "claude-3-haiku-20240307" --profession "general neurologist" --position "attending" --first_person
python $CLI measure --qbank $Q_BANK --model "claude-3-haiku-20240307" --profession "general neurologist" --position "resident" --first_person
python $CLI measure --qbank $Q_BANK --model "claude-3-haiku-20240307" --profession "general neurologist" --position "student" --first_person

python $CLI measure --qbank $Q_BANK --model "claude-3-haiku-20240307" --profession "general neurologist" --position "attending" --workplace_study "world-class institution" --first_person
python $CLI measure --qbank $Q_BANK --model "claude-3-haiku-20240307" --profession "general neurologist" --position "attending" --workplace_study "regional-level institution" --first_person
python $CLI measure --qbank $Q_BANK --model "claude-3-haiku-20240307" --profession "general neurologist" --position "resident" --workplace_study "world-class institution" --first_person
python $CLI measure --qbank $Q_BANK --model "claude-3-haiku-20240307" --profession "general neurologist" --position "resident" --workplace_study "regional-level institution" --first_person
python $CLI measure --qbank $Q_BANK --model "claude-3-haiku-20240307" --profession "general neurologist" --position "student" --workplace_study "world-class institution" --first_person
python $CLI measure --qbank $Q_BANK --model "claude-3-haiku-20240307" --profession "general neurologist" --position "student" --workplace_study "regional-level institution" --first_person

python $CLI measure --qbank $Q_BANK --model "claude-3-haiku-20240307" --profession "general neurologist" --workplace_study "world-class institution" --first_person
python $CLI measure --qbank $Q_BANK --model "claude-3-haiku-20240307" --profession "general neurologist" --workplace_study "regional-level institution" --first_person

python $CLI measure --qbank $Q_BANK --model "claude-3-haiku-20240307" --profession "general neurologist" --gender "male" --position "attending" --workplace_study "world-class institution" --first_person
python $CLI measure --qbank $Q_BANK --model "claude-3-haiku-20240307" --profession "general neurologist" --gender "female" --position "attending" --workplace_study "world-class institution" --first_person
python $CLI measure --qbank $Q_BANK --model "claude-3-haiku-20240307" --profession "general neurologist" --gender "male" --position "attending" --workplace_study "regional-level institution" --first_person
python $CLI measure --qbank $Q_BANK --model "claude-3-haiku-20240307" --profession "general neurologist" --gender "female" --position "attending" --workplace_study "regional-level institution" --first_person
python $CLI measure --qbank $Q_BANK --model "claude-3-haiku-20240307" --profession "general neurologist" --gender "male" --position "resident" --workplace_study "world-class institution" --first_person
python $CLI measure --qbank $Q_BANK --model "claude-3-haiku-20240307" --profession "general neurologist" --gender "female" --position "resident" --workplace_study "world-class institution" --first_person
python $CLI measure --qbank $Q_BANK --model "claude-3-haiku-20240307" --profession "general neurologist" --gender "male" --position "resident" --workplace_study "regional-level institution" --first_person
python $CLI measure --qbank $Q_BANK --model "claude-3-haiku-20240307" --profession "general neurologist" --gender "female" --position "resident" --workplace_study "regional-level institution" --first_person
python $CLI measure --qbank $Q_BANK --model "claude-3-haiku-20240307" --profession "general neurologist" --gender "male" --position "student" --workplace_study "world-class institution" --first_person
python $CLI measure --qbank $Q_BANK --model "claude-3-haiku-20240307" --profession "general neurologist" --gender "female" --position "student" --workplace_study "world-class institution" --first_person
python $CLI measure --qbank $Q_BANK --model "claude-3-haiku-20240307" --profession "general neurologist" --gender "male" --position "student" --workplace_study "regional-level institution" --first_person
python $CLI measure --qbank $Q_BANK --model "claude-3-haiku-20240307" --profession "general neurologist" --gender "female" --position "student" --workplace_study "regional-level institution" --first_person