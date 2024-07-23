from models import model_dict

def get_model_from_args(model_name):
    return model_dict[model_name]