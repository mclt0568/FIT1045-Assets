from database import read_data


def average(lst: list[int]) -> float:
  return sum(lst) / len(lst)


def my_app():
  data = read_data() # returns a list
  print("The average of the data is:", average(data))


if __name__ == "__main__":
  my_app()
