from core.search import GridSearchProblem, breadth_first_search


def main():
    problem = GridSearchProblem()
    print(f"Start: {problem.start}")
    print(f"Goal: {problem.goal}")
    path = breadth_first_search(problem)
    print(f"Path: {path}")
    problem.plotSolution(path)


if __name__ == '__main__':
    main()
