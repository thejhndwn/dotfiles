import sys
import os
import re
import subprocess
from datetime import datetime, timedelta
from glob import glob

def main():
    print('running plan command...')
    print()

    # Environment and directories
    dotfiles_root = os.environ.get('DOTFILES_ROOT', os.path.expanduser('~'))
    planner_dir = os.path.join(dotfiles_root, 'plan')
    highlights_dir = os.path.join(planner_dir, 'highlights')
    notes_dir = os.path.join(planner_dir, 'notes')
    todo_dir = os.path.join(planner_dir, 'todo')
    goals_dir = os.path.join(planner_dir, 'goals')

    # Dates
    today = datetime.now()
    today_date = today.strftime('/%Y/%m/%d')
    tomorrow_date = (today + timedelta(days=1)).strftime('/%Y/%m/%d')
    today_year = today.strftime('/%Y')

    todays_todo_file = os.path.join(todo_dir, today_date + '.md')
    todays_highlights_file = os.path.join(highlights_dir, today_year + '.md')
    todays_notes_file = os.path.join(notes_dir, today_date + '.md')
    todays_goals_file = os.path.join(goals_dir, today_year + '.md')
    tomorrows_todo_file = os.path.join(todo_dir, tomorrow_date + '.md')

    def handle_missing_todo(file_path):
        # Find the last entry
        todo_files = sorted(glob(os.path.join(todo_dir, '*.md')))
        if todo_files:
            last_entry = todo_files[-1]
            print(f"last planner entry: {last_entry}")
            # Copy unfinished todos (lines not starting with - [X] or - [x])
            with open(last_entry, 'r') as src, open(file_path, 'w') as dest:
                for line in src:
                    if not re.match(r'^-\s*\[[Xx]\]', line.strip()):
                        dest.write(line)
        # Open in nvim
        subprocess.call(['nvim', file_path])

    args = sys.argv[1:]
    if not args or args[0] in ('help', '--help'):
        print("  todo        Show today's todos")
        return

    command = args[0]
    subargs = args[1:]

    if command == 'todo':
        if not subargs:
            if os.path.exists(todays_todo_file):
                print("file exists, open file")
                with open(todays_todo_file, 'r') as f:
                    print(f.read())
            else:
                print("today's file doesn't exist, make new one")
                handle_missing_todo(todays_todo_file)
        elif subargs[0] in ('tom', '-t', '--t', 't'):
            if os.path.exists(tomorrows_todo_file):
                print("file exists, open file")
                subprocess.call(['nvim', tomorrows_todo_file])
            else:
                print("today's file doesn't exist, make new one")
                handle_missing_todo(tomorrows_todo_file)
        elif subargs[0] in ('v', '-v', '--v'):
            subprocess.call(['nvim', todays_todo_file])
        elif subargs[0] in ('mark', 'm', '-m', '--mark'):
            if len(subargs) < 2 or not subargs[1]:
                # TODO: enter mark mode
                print('entering todo completion marker mode')
                subprocess.call(['plan-marker', todays_todo_file])
            else:
                mark_arg = subargs[1]
                if mark_arg.isdigit():
                    # TODO: check if the todo item exists, make todo items getter
                    # if it does then remove and exit, if it doesn't then reply
                    print('entered specific marker mode')
                else:
                    print(f"unknown command: {mark_arg}")
        elif subargs[0] in ('new', 'n', '-n', '--new'):
            if len(subargs) < 2:
                print("Missing subcommand for 'new'")
                return
            new_sub = subargs[1]
            insert_text = ' '.join(subargs[2:]) if len(subargs) > 2 else ''
            if new_sub in ('today', 't', '-t', '--t', '--today'):
                # TODO: insert next text in today's todo
                print(f"let's insert {insert_text}")
            elif new_sub in ('project', 'p', '-p', '--p', '--project'):
                # TODO: insert next text in projects todo
                pass
            elif new_sub in ('quick', 'q', '-q', '--q', '--quick'):
                # TODO: same
                pass
            elif new_sub in ('future', 'f', '-f', '--f', '--future'):
                # TODO: same
                pass
            else:
                # TODO: insert into misc, but make sure it stops random commands
                pass
        else:
            print(f"Unknown subcommand for todo: {subargs[0]}")
    elif command == 'goals':
        if not subargs:
            if os.path.exists(todays_goals_file):
                with open(todays_goals_file, 'r') as f:
                    print(f.read())
            else:
                print("Goals file does not exist.")
        else:
            subprocess.call(['nvim', todays_goals_file])
    elif command == 'highlights':
        if not subargs:
            if os.path.exists(todays_highlights_file):
                with open(todays_highlights_file, 'r') as f:
                    print(f.read())
            else:
                print("Highlights file does not exist.")
        elif subargs[0] == '-v':
            subprocess.call(['nvim', todays_highlights_file])
        else:
            highlight_text = ' '.join(subargs)
            timestamp = today.strftime("[%Y-%m-%d]")
            with open(todays_highlights_file, 'a') as f:
                f.write(f"{timestamp} {highlight_text}\n")
    elif command == 'notes':
        if not os.path.exists(todays_notes_file):
            open(todays_notes_file, 'a').close()  # touch equivalent
        if not subargs:
            with open(todays_notes_file, 'r') as f:
                print(f.read())
        elif subargs[0] == '-v':
            subprocess.call(['nvim', todays_notes_file])
        elif subargs[0] == '-l':
            note_text = ' '.join(subargs[1:])
            timestamp = today.strftime("%Y-%m-%d %H:%M:%S")
            with open(todays_notes_file, 'a') as f:
                f.write(f"[{timestamp}][learn] {note_text}\n")
        else:
            note_text = ' '.join(subargs)
            timestamp = today.strftime("%Y-%m-%d %H:%M:%S")
            with open(todays_notes_file, 'a') as f:
                f.write(f"[{timestamp}] {note_text}\n")
    else:
        print(f"Unknown command: {command}")
        print("What are you trying to do :/")

if __name__ == '__main__':
    main()
