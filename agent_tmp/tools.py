import subprocess

def run_shell(command: str)->str:
    result=subprocess.run(command, shell=True, capture_output=True, text=True)
    return result.stdout or result.stderr


def caluclator(expression: str)->str:
    """
    Evaluate a mathematical expression safely
    Example inputs:
    "45*12"
    "100+200"
    """
    
    try:
        result=eval(expression)
        return str(result)
    except Exception as e:
        return f"Error evaluating expression: {str(e)}"
    
TOOLS={
    "run_shell": run_shell,
    "calculator": caluclator
}

    