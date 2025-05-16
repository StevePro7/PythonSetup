import json

class ParamGrid:
    def __init__(self, C: str, gamma: list):
        self.C: str = C
        self.gamma: list = gamma

    def to_dict(self):
        return {
            'C': self.C,
            'gamma': self.gamma
        }


param_grid_obj = ParamGrid(
    C=[0.001, 0.01, 0.1, 1, 10, 100],
    gamma=[0.001, 0.01, 0.1, 1, 10, 100]
)

param_grid_dict = param_grid_obj.to_dict()
print(param_grid_dict)

param_grid_json = json.dumps(param_grid_dict, indent=4)
print(param_grid_json)