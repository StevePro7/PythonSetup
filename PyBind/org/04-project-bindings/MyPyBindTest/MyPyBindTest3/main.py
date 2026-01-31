# example.py
import mycore

def main():
    # Create a Processor with scale=3
    p = mycore.Processor(3)

    # Call the C++ process() method
    result = p.process(10)

    print("Processor(3).process(10) =", result)

if __name__ == "__main__":
    main()
