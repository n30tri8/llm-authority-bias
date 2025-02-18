# Who are LLMs’ Cognitive Authorities? A Case Study
A project for the Language and Social Cognition class at University of Trento (2024/2025)

# Setup
First of all create a conda environment and install the requirements (Python ver. == 3.8)
```bash
conda create --name llm_authority_bias python=3.8
pip install -r requirements.txt
```

# Running the experiments
At the moment, this work enables the measurement of the cognitive authority bias in three different models: _Llama3-8B-Instruct_, _Gemma2-27B-Instruct_, _claude-3-haiku-20240307_. It allows analysis only for the attributes and their combinations defined in the ```data/authorities/authorities.csv``` file.

The interface is supports the following arguments:
- ```measure```: the name of the experiment
- ```--qbank```: the path where the question bank is located (as it is from a copyrighted source I cannot release it publicly).
- ```--model```: the model name, as specified in the ```backends/model_registry.json``` file.
- ```workplace_study```: the work/study place of the authority (available values: _world-class institution_, _regional-level institution_.
- ```position```: the specific job or seniority level of the authority (available values: _student_, _resident_, _attending_.
- ```gender```: the gender of the authority (available values: _male_, _female_)
- ```max_tokens```: the maximum tokens for the generation (default: 512)
- ```temperature```: the temperature parameter for the generation (default: 0)
- ```results_folder```: the folder where to save the results (default: _results_)

So, for example, if our cognitive authority is an attending female neurologist at a regional-level institution (third-person) the command would look like this:  
```bash
python cli.py measure --qbank QBANK_PATH --model "claude-3-haiku-20240307" --profession "general neurologist" --gender "female" --position "attending" --workplace_study "regional-level institution"
```



# Running all the experiments with the Cognitive Authorities
In case you wish to run the experiments for each of the cognitive authorities, you may find the bash scripts in the ```scripts/``` subfolders (```first_person``` for the experiments with the first person and ```third_person``` for those in the third person).
