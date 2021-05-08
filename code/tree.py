# https://pythonspot.com/python-tree/
#import numpy as np
#import pandas as pd
#import matplotlib.pyplot as plt

class Tree(object):
    def __init__(self):
        self.left = None
        self.right = None
        self.data = None

root = Tree()
root.data = "root"
root.left = Tree()
root.left.data = "left"
root.right = Tree()
root.right.data = "right"

print(root.left.data)
