from multiprocessing import Process, Queue
from dashboard.main import Dashboard

def run():

    window = Dashboard()
    window.mainloop()

if __name__ == "__main__":

    run()