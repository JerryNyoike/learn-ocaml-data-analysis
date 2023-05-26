from pprint import pprint
from pathlib import Path
from dotenv import dotenv_values

config = dotenv_values('.env')

def main():
    solution_paths = list(filter(lambda path: 'hw' in path.name, list(Path(config.get('SOLUTION_DIR')).iterdir())))
    submission_paths = list(filter(lambda path: 'hw' in path.name, list(Path(config.get('SUB_DIR')).iterdir())))
    solution_paths.sort()
    submission_paths.sort()

    # ensure we are using the correct solution directory
    for hw_path in submission_paths[0:1]:
        for question_path in list(filter(lambda n: n.is_dir() and 'q' in n.name, hw_path.iterdir())):
            for student_submissions in question_path.joinpath('student_submissions').iterdir():
                print('> {}'.format(student_submissions.name))


if __name__ == '__main__':
    main()
