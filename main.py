from app.search import breadth_first_search, GridSearchProblem


def main():
    problem = GridSearchProblem()
    print(f"Start: {problem.start}")
    print(f"Goal: {problem.goal}")
    path = breadth_first_search(problem)
    print(f"Path: {path}")


if __name__ == '__main__':
    main()
