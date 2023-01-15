#!/usr/bin/python3
"""append json"""
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file
import sys


def main():
    """main entry"""
    with open('add_item.json', 'a') as fp:
        fp.close()
    my_list = load_from_json_file('add_item.json')
    my_list.extend(sys.argv[1:])
    save_to_json_file(my_list, 'add_item.json')

if __name__ == '__main__':
    main()
