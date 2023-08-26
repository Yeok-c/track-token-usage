# track-token-usage
# Track langchain / OpenAI token usage minimalistically.
  - Sums up the token costs for any OpenAI model in all your langchain calls wrapped in get_openai_callback()
  - Displays it to you when your program exits
  - Can be logged to textfile otherwise

# Example output when called
```
Total tokens: 7919
Prompt tokens: 7448
Completion tokens: 471
Total cost: 0.024228
```

# Example usage
```
# Import packages
from track_usage import TokenTrack
from langchain.callbacks import get_openai_callback

#Example usage 1.
class YourClass(TokenTrack):
    def __init__(self):
        pass

    def your_function(self):
        with get_openai_callback() as cb:        
            your_langchain_function_here()
        self.update_usage(cb)

    def whenever_you_want_to_check():
        self.print_usage()


Example usage 2.
class YourClass():
    def __init__(self):
        self.tt = TokenTrack()

    def your_function(self):
        with get_openai_callback() as cb:
            your_langchain_function_here()
        self.tt.update_usage(cb)

    def whenever_you_want_to_check():
        self.tt.print_usage()

```
