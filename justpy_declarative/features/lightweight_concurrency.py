from threading import Thread


def concurr(func):
    """
    Examples:
        @concurr
        def f1(name, cnt):
            for i in range(cnt):
                print(f'{name}: {i}')
        
        f1('task1', 3)
        f1('task2', 7)
        f1('task3', 5)
    """
    
    def wrap(*args, **kwargs):
        thread = Thread(
            target=func,
            args=args,
            kwargs=kwargs
        )
        thread.start()
        return thread
    
    return wrap
