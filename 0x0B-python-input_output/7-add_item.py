#!/usr/bin/python3
"""append json"""
import sys
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file


def main():
    """main entry"""
    try:
        with open('add_item.json', 'r') as fp:
            rd = fp.read()
            fp.close()
    except FileNotFoundError:
        with open('add_item.json', 'w') as fp:
            fp.write('[]')
            fp.close()
    my_list = load_from_json_file('add_item.json')
    my_list.extend(sys.argv[1:])
    save_to_json_file(my_list, 'add_item.json')


if __name__ == '__main__':
    main()
