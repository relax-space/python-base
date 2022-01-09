
'''
说明: LogInFile只会在文件中留日志, LogInFileAndConsole 不进在文件中,而且在控制台也会留日志
'''

from datetime import datetime
from functools import wraps


class LogInFile:
    def __init__(self, path='data/data.log'):
        self.path = path

    def __call__(self, func):
        @wraps(func)
        def wrap(*args, **kwargs):
            log = f'{datetime.now()} {func.__name__} is called.\n'
            with open(self.path, 'a', encoding='utf-8') as f:
                f.write(log)
            self.console(log)
            res = func(*args, **kwargs)
            return res
        return wrap

    def console(self, log):
        pass


@LogInFile()
def req1():
    return 1


class LogInFileAndConsole(LogInFile):
    def __init__(self, path='data/data.log'):
        super().__init__(path)

    def console(self, log):
        print(log)


@LogInFileAndConsole()
def req2():
    return 2


if __name__ == '__main__':
    print('请在data/data.log中查看日志')
    print(req1())
    print('==========')
    print(req2())
