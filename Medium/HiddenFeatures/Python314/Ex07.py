import sys
import threading
import time
from typing import Any, Callable, Optional

class ExternalDebugger:
    """Example implementation of the new external debugger interface"""
    
    def __init__(self):
        self.active = False
        self.breakpoints = set()
        self.call_stack = []
        
    def attach(self) -> bool:
        """Attach debugger to the current process"""
        if hasattr(sys, 'set_external_debugger'):
            # Register our debugger hooks
            sys.set_external_debugger(self._debug_hook)
            self.active = True
            print("External debugger attached")
            return True
        return False
    
    def detach(self) -> bool:
        """Detach debugger from the current process"""
        if hasattr(sys, 'set_external_debugger'):
            sys.set_external_debugger(None)
            self.active = False
            self.call_stack.clear()
            print("External debugger detached")
            return True
        return False
    
    def set_breakpoint(self, filename: str, line_number: int):
        """Set a breakpoint at specific file and line"""
        self.breakpoints.add((filename, line_number))
        print(f"Breakpoint set at {filename}:{line_number}")
    
    def _debug_hook(self, frame, event: str, arg: Any) -> Optional[Callable]:
        """Internal debug hook called by the Python interpreter"""
        if not self.active:
            return None
            
        filename = frame.f_code.co_filename
        line_number = frame.f_lineno
        function_name = frame.f_code.co_name
        
        if event == 'call':
            self.call_stack.append({
                'function': function_name,
                'filename': filename,
                'line': line_number,
                'thread_id': threading.get_ident()
            })
            
        elif event == 'line':
            # Check if we hit a breakpoint
            if (filename, line_number) in self.breakpoints:
                print(f"BREAKPOINT HIT: {filename}:{line_number} in {function_name}")
                print(f"Call stack depth: {len(self.call_stack)}")
                print(f"Local variables: {list(frame.f_locals.keys())}")
                
        elif event == 'return':
            if self.call_stack:
                self.call_stack.pop()
                
        return self._debug_hook

# Example usage of the external debugger
def example_function(x: int, y: int) -> int:
    """Function to demonstrate debugging capabilities"""
    result = x + y
    intermediate = result * 2
    final_result = intermediate - 1
    return final_result

def another_function():
    """Another function to show call stack tracking"""
    return example_function(10, 20)

# Demonstrate the external debugger
debugger = ExternalDebugger()

# Attach debugger and set breakpoints
if debugger.attach():
    # Set breakpoint in our example function
    debugger.set_breakpoint(__file__, 45)  # Line with 'intermediate = result * 2'
    
    # Run some code that will trigger the debugger
    print("Running code with debugger attached...")
    result = another_function()
    print(f"Function result: {result}")
    
    # Detach when done
    debugger.detach()
else:
    print("External debugger interface not available in this Python version")