from time import strftime
from json import dump, load
from os.path import realpath, dirname
from random import choice
from typing import List, Dict

this_file_path = realpath(dirname(__file__))
WORKOUT_FILE = f"{this_file_path}/workouts.json"

def get_current_workouts() -> List[str]:
  todays_day = strftime("%w")
  workouts = None
  current_workouts = None
  with open(WORKOUT_FILE, "r+") as workout_file:
    workouts = load(workout_file)
    current_workouts = workouts["current_workouts"]

    if todays_day == "0":
      all_workouts = workouts["all_workouts"]
      current_workouts = all_workouts

      update_current_workouts(current_workouts)

  return current_workouts

def update_current_workouts(current_workouts: List[str]) -> None:
  with open(WORKOUT_FILE, "r+") as workout_file:
    workouts = load(workout_file)

    workouts["current_workouts"] = current_workouts

    workout_file.seek(0)
    dump(workouts, workout_file)
    workout_file.truncate()

def choose_workout() -> str:
  current_workouts = get_current_workouts()
  workout = choice(current_workouts)

  current_workouts.remove(workout)
  update_current_workouts(current_workouts)

  return workout

if __name__ == "__main__":
  print(choose_workout())