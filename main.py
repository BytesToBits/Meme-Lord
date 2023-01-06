import argparse
from core.MemeBot import MemeBot

if __name__ == "__main__":

  parser = argparse.ArgumentParser()
  parser.add_argument('--dev', dest='dev', action='store_true')

  args = parser.parse_args()

  is_dev = args.dev

  MemeBot(is_dev)