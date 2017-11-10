import numpy as np
import requests


def main(event, context):
    a = np.arange(15).reshape(3, 5)
    
    print("Your numpy array:")
    print(a)

    r = requests.get('https://api.github.com/events')
    print(r.text)


if __name__ == "__main__":
    main('', '')