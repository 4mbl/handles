import os
import platforms.github as github
import platforms.npm as npm


def process_input(input_dir: str = os.path.join(os.path.dirname(__file__),
                                                'secret')):

    usernames = []
    for file_name in os.listdir(input_dir):
        file_path = os.path.join(input_dir, file_name)
        with open(file_path, encoding='UTF-8') as f:
            for line in f:
                if line == "\n":
                    continue
                if file_name.endswith('.txt'):
                    usernames.append(line.strip())
                elif file_name.endswith('.csv'):
                    line = line.split(';')
                    usernames.append(line[0].rstrip())

    return usernames


def main():
    usernames = process_input()
    print(f'github : {github.are_available(usernames)}')
    print(f'npm : {npm.are_available(usernames)}')


if __name__ == '__main__':
    main()