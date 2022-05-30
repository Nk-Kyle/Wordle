from interface import *
from preprocess import *
from colorama import Fore
import pickle

with open('resources/tree.pkl', 'rb') as f:
    loaded_dict = pickle.load(f)
    print(loaded_dict['ZYMIC'][str([Fore.GREEN,Fore.WHITE,Fore.GREEN,Fore.WHITE, Fore.WHITE])])