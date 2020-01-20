"""
  OR-tools solution to the N-queens problem.
"""
import sys
from ortools.constraint_solver import pywrapcp
import pika,requests, json


# By default, solve the 8x8 problem.
board_size = 8

def write_queue(queue_name, msg, tache_id, soustache_id):
    dataout = {}
    dataout["tache_id"] = str(tache_id)
    dataout["soustache_id"] = str(soustache_id)
    dataout["result"] = str(msg)
    requests.get("http://172.18.10.1:5000/write_queue/{}/{}/".format(queue_name, json.dumps(dataout)))


def main(tache_id, soustache_id,board_size):
  
  # Creates the solver.
  solver = pywrapcp.Solver("n-queens")
  # Creates the variables.
  # The array index is the column, and the value is the row.
  queens = [solver.IntVar(0, board_size - 1, "x%i" % i) for i in range(board_size)]
  # Creates the constraints.

  # All rows must be different.
  solver.Add(solver.AllDifferent(queens))

  # All columns must be different because the indices of queens are all different.

  # No two queens can be on the same diagonal.
  solver.Add(solver.AllDifferent([queens[i] + i for i in range(board_size)]))
  solver.Add(solver.AllDifferent([queens[i] - i for i in range(board_size)]))
  
  db = solver.Phase(queens, solver.CHOOSE_FIRST_UNBOUND, solver.ASSIGN_MIN_VALUE)
  solver.NewSearch(db)
  
  num_solutions = 0

  while solver.NextSolution():
    # Displays the solution just computed.
    num_solutions += 1

  print("Solutions found:", num_solutions)

  write_queue("dataout", num_solutions, tache_id, soustache_id)
  print()
  print("dataout create in N_queue.py")



if __name__ == "__main__":

  tache_id=0
  soustache_id=0
  
  if len(sys.argv) > 1:
    board_size = int(sys.argv[1])
    tache_id = int(sys.argv[2])
    soustache_id = int(sys.argv[3])
    main(tache_id, soustache_id,board_size)
   
  print("tache ID:", tache_id)
  print("Soustache ID:", soustache_id) 