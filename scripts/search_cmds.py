import sys
import subprocess
import re

def search_file(file_path, keywords):
    keywords = [kw.lower() for kw in keywords]
    results = []
    
    with open(file_path, 'r') as f:
        for line_num, line in enumerate(f, start=1):
            lower_line = line.lower()
            # Count how many unique keywords appear in the line (word-boundary aware for accuracy)
            match_count = sum(1 for kw in set(keywords) if re.search(r'\b' + re.escape(kw) + r'\b', lower_line))
            if match_count > 0:
                results.append((match_count, line_num, line.strip()))
    
    # Sort by match_count descending, then by original line_num ascending (preserves file order for ties)
    results.sort(key=lambda x: (-x[0], x[1]))
    
    # Output
    if not results:
        print("No matches found.")
    else:
        prev_count = None
        for count, _, line in results:
            if count != prev_count:
                if prev_count is not None:
                    print()  # Separator between match levels
                print(f"--- Matches with {count} keyword(s) ---")
                prev_count = count
            print(line)

if __name__ == '__main__':
    if len(sys.argv) < 2:
        print("Usage: python cmdsearch.py /path/to/cmds.md keyword1 [keyword2 ...]")
        sys.exit(1)
    file_path = sys.argv[1]
    keywords = sys.argv[2:]

    if not keywords:
        subprocess.call(['vim', file_path])
        sys.exit(0)
    search_file(file_path, keywords)
