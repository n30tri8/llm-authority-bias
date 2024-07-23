#!/bin/bash

python ../experiments/measure_authority_bias.py --qbank "../question_bank/neuro/question_bank_with_model_answers.csv" --model "claude-3-haiku-20240307" --subspecialty "general"

python ../experiments/measure_authority_bias.py --qbank "../question_bank/neuro/question_bank_with_model_answers.csv" --model "claude-3-haiku-20240307" --subspecialty "general" --gender "male"

python ../experiments/measure_authority_bias.py --qbank "../question_bank/neuro/question_bank_with_model_answers.csv" --model "claude-3-haiku-20240307" --subspecialty "general" --gender "female"

python ../experiments/measure_authority_bias.py --qbank "../question_bank/neuro/question_bank_with_model_answers.csv" --model "claude-3-haiku-20240307" --subspecialty "general" --gender "male" --position "attending"
python ../experiments/measure_authority_bias.py --qbank "../question_bank/neuro/question_bank_with_model_answers.csv" --model "claude-3-haiku-20240307" --subspecialty "general" --gender "female" --position "attending"

python ../experiments/measure_authority_bias.py --qbank "../question_bank/neuro/question_bank_with_model_answers.csv" --model "claude-3-haiku-20240307" --subspecialty "general" --gender "male" --position "student"
python ../experiments/measure_authority_bias.py --qbank "../question_bank/neuro/question_bank_with_model_answers.csv" --model "claude-3-haiku-20240307" --subspecialty "general" --gender "female" --position "student"

python ../experiments/measure_authority_bias.py --qbank "../question_bank/neuro/question_bank_with_model_answers.csv" --model "claude-3-haiku-20240307" --subspecialty "general" --gender "male" --position "resident"
python ../experiments/measure_authority_bias.py --qbank "../question_bank/neuro/question_bank_with_model_answers.csv" --model "claude-3-haiku-20240307" --subspecialty "general" --gender "female" --position "resident"

python ../experiments/measure_authority_bias.py --qbank "../question_bank/neuro/question_bank_with_model_answers.csv" --model "claude-3-haiku-20240307" --subspecialty "general" --gender "male" --workplace_study "world-class medical institution"
python ../experiments/measure_authority_bias.py --qbank "../question_bank/neuro/question_bank_with_model_answers.csv" --model "claude-3-haiku-20240307" --subspecialty "general" --gender "female" --workplace_study "world-class medical institution"

python ../experiments/measure_authority_bias.py --qbank "../question_bank/neuro/question_bank_with_model_answers.csv" --model "claude-3-haiku-20240307" --subspecialty "general" --gender "male" --workplace_study "regional-level clinic"
python ../experiments/measure_authority_bias.py --qbank "../question_bank/neuro/question_bank_with_model_answers.csv" --model "claude-3-haiku-20240307" --subspecialty "general" --gender "female" --workplace_study "regional-level clinic"

python ../experiments/measure_authority_bias.py --qbank "../question_bank/neuro/question_bank_with_model_answers.csv" --model "claude-3-haiku-20240307" --subspecialty "general" --position "attending"
python ../experiments/measure_authority_bias.py --qbank "../question_bank/neuro/question_bank_with_model_answers.csv" --model "claude-3-haiku-20240307" --subspecialty "general" --position "resident"
python ../experiments/measure_authority_bias.py --qbank "../question_bank/neuro/question_bank_with_model_answers.csv" --model "claude-3-haiku-20240307" --subspecialty "general" --position "student"

python ../experiments/measure_authority_bias.py --qbank "../question_bank/neuro/question_bank_with_model_answers.csv" --model "claude-3-haiku-20240307" --subspecialty "general" --position "attending" --workplace_study "world-class medical institution"
python ../experiments/measure_authority_bias.py --qbank "../question_bank/neuro/question_bank_with_model_answers.csv" --model "claude-3-haiku-20240307" --subspecialty "general" --position "attending" --workplace_study "regional-level clinic"
python ../experiments/measure_authority_bias.py --qbank "../question_bank/neuro/question_bank_with_model_answers.csv" --model "claude-3-haiku-20240307" --subspecialty "general" --position "resident" --workplace_study "world-class medical institution"
python ../experiments/measure_authority_bias.py --qbank "../question_bank/neuro/question_bank_with_model_answers.csv" --model "claude-3-haiku-20240307" --subspecialty "general" --position "resident" --workplace_study "regional-level clinic"
python ../experiments/measure_authority_bias.py --qbank "../question_bank/neuro/question_bank_with_model_answers.csv" --model "claude-3-haiku-20240307" --subspecialty "general" --position "student" --workplace_study "medical school recognized as the best in the world"
python ../experiments/measure_authority_bias.py --qbank "../question_bank/neuro/question_bank_with_model_answers.csv" --model "claude-3-haiku-20240307" --subspecialty "general" --position "student" --workplace_study "medical school associated with a University of regional importance"

python ../experiments/measure_authority_bias.py --qbank "../question_bank/neuro/question_bank_with_model_answers.csv" --model "claude-3-haiku-20240307" --subspecialty "general" --workplace_study "world-class medical institution"
python ../experiments/measure_authority_bias.py --qbank "../question_bank/neuro/question_bank_with_model_answers.csv" --model "claude-3-haiku-20240307" --subspecialty "general" --workplace_study "regional-level clinic"

python ../experiments/measure_authority_bias.py --qbank "../question_bank/neuro/question_bank_with_model_answers.csv" --model "claude-3-haiku-20240307" --subspecialty "general" --gender "male" --position "attending" --workplace_study "world-class medical institution"
python ../experiments/measure_authority_bias.py --qbank "../question_bank/neuro/question_bank_with_model_answers.csv" --model "claude-3-haiku-20240307" --subspecialty "general" --gender "female" --position "attending" --workplace_study "world-class medical institution"
python ../experiments/measure_authority_bias.py --qbank "../question_bank/neuro/question_bank_with_model_answers.csv" --model "claude-3-haiku-20240307" --subspecialty "general" --gender "male" --position "attending" --workplace_study "regional-level clinic"
python ../experiments/measure_authority_bias.py --qbank "../question_bank/neuro/question_bank_with_model_answers.csv" --model "claude-3-haiku-20240307" --subspecialty "general" --gender "female" --position "attending" --workplace_study "regional-level clinic"
python ../experiments/measure_authority_bias.py --qbank "../question_bank/neuro/question_bank_with_model_answers.csv" --model "claude-3-haiku-20240307" --subspecialty "general" --gender "male" --position "resident" --workplace_study "world-class medical institution"
python ../experiments/measure_authority_bias.py --qbank "../question_bank/neuro/question_bank_with_model_answers.csv" --model "claude-3-haiku-20240307" --subspecialty "general" --gender "female" --position "resident" --workplace_study "world-class medical institution"
python ../experiments/measure_authority_bias.py --qbank "../question_bank/neuro/question_bank_with_model_answers.csv" --model "claude-3-haiku-20240307" --subspecialty "general" --gender "male" --position "resident" --workplace_study "regional-level clinic"
python ../experiments/measure_authority_bias.py --qbank "../question_bank/neuro/question_bank_with_model_answers.csv" --model "claude-3-haiku-20240307" --subspecialty "general" --gender "female" --position "resident" --workplace_study "regional-level clinic"
python ../experiments/measure_authority_bias.py --qbank "../question_bank/neuro/question_bank_with_model_answers.csv" --model "claude-3-haiku-20240307" --subspecialty "general" --gender "male" --position "student" --workplace_study "medical school recognized as the best in the world"
python ../experiments/measure_authority_bias.py --qbank "../question_bank/neuro/question_bank_with_model_answers.csv" --model "claude-3-haiku-20240307" --subspecialty "general" --gender "female" --position "student" --workplace_study "medical school recognized as the best in the world"
python ../experiments/measure_authority_bias.py --qbank "../question_bank/neuro/question_bank_with_model_answers.csv" --model "claude-3-haiku-20240307" --subspecialty "general" --gender "male" --position "student" --workplace_study "medical school associated with a University of regional importance"
python ../experiments/measure_authority_bias.py --qbank "../question_bank/neuro/question_bank_with_model_answers.csv" --model "claude-3-haiku-20240307" --subspecialty "general" --gender "female" --position "student" --workplace_study "medical school associated with a University of regional importance"