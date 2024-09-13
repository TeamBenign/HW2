"""random module to generate random numbers"""

import subprocess # nosec


def random_array(arr):
    """random function that returns an array of random numbers."""
    for i, _ in enumerate(arr):
        shuffled_num = subprocess.run(
            ["/usr/bin/shuf", "-i1-20", "-n1"],
            capture_output=True, check=True)# nosec
        arr[i] = int(shuffled_num.stdout)
    return arr
