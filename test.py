import time


def loop_func(status):
    for i in range(1, 20, 1):
        if status.status_var.get() == 'Status: None':
            break
        print(f'{i}')
        time.sleep(1)