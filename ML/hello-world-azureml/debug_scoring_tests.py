#!/usr/bin/env python3








import os
import sys
import json
import http
from pathlib import Path

# Setup paths and environment
project_root = Path(__file__).parent
app_dir = project_root / "app"
sys.path.insert(0, str(app_dir))
os.environ["AZUREML_MODEL_DIR"] = str(project_root / "model")

def debug_scoring_init():
    """


    """
    print("init")


    #
    import app.scoring as scoring




    scoring.init()



    return scoring

def debug_scoring_run(scoring_module):
    """

    """
    print("test")



    test_cases = [
        # {
        #     "name": "Simple Name Test",
        #     "input": '{"name": "Alice"}',
        #     "description": "Test with a simple name"
        # },
        # {
        #     "name": "Simple Name Test",
        #     "input": '{"name": "Alice"}',
        #     "description": "Test with a simple name"
        # },
        # {
        #     "name": "Simple Name Test",
        #     "input": '{"name": "Alice"}',
        #     "description": "Test with a simple name"
        # },
        # {
        #     "name": "Simple Name Test",
        #     "input": '{"name": "Alice"}',
        #     "description": "Test with a simple name"
        # },
        {
            "name": "Simple Name Test",
            "input": '{"name": "Alice"}',
            "description": "Test with a simple name"
        }
    ]

    results = []

    for i, test_case in enumerate(test_cases, 1):
        print(f'{test_case["name"]}')





        try:
            #
            response = scoring_module.run('{"sleep": 3}')



            if response.status_code == http.HTTPStatus.OK:
                response_data = json.loads(response.data)
                results.append({
                    "test": "success"
                })














        except Exception as e:
            print(f"{e}")
            results.append({
                "test": "failure"
            })

    return results

def main():
    try:
        scoring_module = debug_scoring_init()

        results = debug_scoring_run(scoring_module)
        print(results)

    except Exception as e:
        print(f"Error {e}")
        import traceback
        traceback.print_exc()

if __name__ == "__main__":
    main()