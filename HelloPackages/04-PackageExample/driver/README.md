## License

Copyright 2019 (c)iON|UL.com. All rights reserved.

## Code to serve models

This code wraps the entire prediction pipeline. 

## Example usage

    from workflows.simple_workflow import SimpleWorkflow

    if __name__ == "__main__":

        workflow = SimpleWorkflow(my_config, my_log_file)

        content = 'blah blah blah'
        predictions = workflow.process(content)
    
        print(predictions)

Any questions, contact James.Cogley@outlook.com