class TokenTrack():
    def __init__(self):
        '''
        Example usage 1.
        During initialization:
            class YourClass(TokenTrack):
            
        In your functions:
            with get_openai_callback() as cb:        
                your_langchain_function_here()
            self.update_usage(cb)
            
        Whenever you want to check:
            self.print_usage()

        
        Example usage 2.
        During initialization:
            self.tt = TokenTrack()
    
        In your functions:
            with get_openai_callback() as cb:
                your_langchain_function_here()
            self.tt.update_usage(cb)
            
        Whenever you want to check:
            self.tt.print_usage()
        
        '''
        self.cb = None
        
        
    def __del__(self):
        self.print_usage()
        
    def update_usage(self, cb):
        if self.cb is None:
            self.cb = cb
            return
        else:
            self.cb.total_tokens += cb.total_tokens
            self.cb.prompt_tokens += cb.prompt_tokens
            self.cb.completion_tokens += cb.completion_tokens
            self.cb.total_cost += cb.total_cost
    
    def print_usage(self):
        print(f'Total tokens: {self.cb.total_tokens}')
        print(f'Prompt tokens: {self.cb.prompt_tokens}')
        print(f'Completion tokens: {self.cb.completion_tokens}')
        print(f'Total cost: {self.cb.total_cost}')
        
        