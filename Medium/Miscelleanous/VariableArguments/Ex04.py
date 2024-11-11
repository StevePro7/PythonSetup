def log_message(level, *args, **kwargs):
    print(f"[{level.upper()}] ", end="")
    for message in args:
        print(message, end=" ")
    if kwargs:
        print("\nAdditional Info:")
        for key, value in kwargs.items():
            print(f"  {key}: {value}")
    print()

log_message("info", "This is an info message.")
log_message("warning", "This is a warning.", "Check the system status.")
log_message("error", "An error occurred!", code=500, description="Server error")
