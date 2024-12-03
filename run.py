#!/usr/bin/env python3
import sys
sys.dont_write_bytecode = True

import os
import argparse
import importlib.util
import logging
import textwrap
import time

from importlib import import_module



def read_input(file_name: str) -> list[str]:
  with open(file_name, "r") as f:
    data = [line.strip() for line in f.readlines()]
  return data

def load_module_from_path(module_path, module_name):
  spec = importlib.util.spec_from_file_location(module_name, module_path)
  module = importlib.util.module_from_spec(spec)
  spec.loader.exec_module(module)
  return module


if __name__ == "__main__":
  parser = argparse.ArgumentParser(description="advent of code", formatter_class=argparse.ArgumentDefaultsHelpFormatter)
  parser.add_argument("--year", type=int, help="<year>", required=True)
  parser.add_argument("--day", type=int, help="<day>", required=False)
  parser.add_argument("--part", type=int, help="<1/2>", required=False)
  parser.add_argument("--example", action="store_true", default=False, help="<true/false>")
  parser.add_argument("--new", type=int, help="<day>", required = False)
  parser.add_argument("--debug", action="store_true", default=False, help="<true/false>", required=False)
  args = parser.parse_args()

  year = args.year

  # logging
  if args.debug:
    red_color_code = '\033[91m'
    reset_color_code = '\033[0m'
    logging.basicConfig(level=logging.DEBUG, format=f"{red_color_code}%(message)s{reset_color_code}")

  # create new directory for the specified year/day
  if args.new:
    if not os.path.isdir(f"./{year}"):
      print(f"create the {year} directory first")
      exit(0)

    new_day = args.new
    new_dir_name = f"day_0{new_day}" if (new_day // 10) < 1 else f"day_{new_day}"
    new_dir_full_path = f"./{year}/{new_dir_name}"

    if os.path.exists(new_dir_full_path):
      print(f"{new_dir_full_path} already exists")
      exit(0)

    os.makedirs(new_dir_full_path)

    files_to_create = ["input.txt", "example_1.txt", "example_2.txt"]

    for file in files_to_create:
      with open(f"{new_dir_full_path}/{file}", "w"):
        pass

    # copy template code to new directory
    with open("./templates/main.py", "r") as f:
        template_code = f.read()

    with open(f"{new_dir_full_path}/main.py", "w") as f:
      f.write(template_code)

    print(f"created {new_dir_full_path}")

  # run specified day's code
  if args.day:
    day = f"day_0{args.day}" if (args.day // 10) < 1 else f"day_{args.day}"
    dir_name = f"./{year}/{day}"

    if not os.path.isdir(dir_name):
      print(f"{dir_name} does not exist")
      exit(0)

    if not args.part or (args.part != 1 and args.part != 2):
      print("specify either part 1 or 2 to run")
      exit(0)

    input_file = f"{dir_name}/example_{args.part}.txt" if args.example else f"{dir_name}/input.txt"

    if not os.path.isfile(input_file):
      print(f"input file {input_file} does not exist")
      exit(0)

    main_module = load_module_from_path(f"{dir_name}/main.py", "main")
    part_func = getattr(main_module, f"part_{args.part}")

    input_data = read_input(input_file)

    start_time = time.perf_counter()
    result = part_func(input_data)
    end_time = time.perf_counter()

    msg = f"Year {year} Day {args.day} Part {args.part} result (example): {result}" if args.example else f"Year {year} Day {args.day} Part {args.part} result: {result}"

    print("------------------------------------")
    print(msg)
    print(f"Finished in {round(end_time - start_time, 3)} seconds")
    print("------------------------------------")
