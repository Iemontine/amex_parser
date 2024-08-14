from datetime import datetime

with open('in.txt', 'r') as f:
    data = f.read()
    with open('out.txt', 'w') as f:
        data = data.replace('\nCredit\n\n', '\n')
        data = data.replace('\n\n', '\n')
        f.write(data)

with open('out.txt', 'r') as infile:
    lines = infile.readlines()

def format_date(date_str, year=2023):
    try:
        date_obj = datetime.strptime(f"{date_str} {year}", "%b %d %Y")
        formatted_date = date_obj.strftime("%m-%d-%Y")
        return formatted_date
    except ValueError:
        if '29' in date_str and 'Feb' in date_str:
            return f"02-29-{year}"
        else:
            raise ValueError(f"Date format for '{date_str}' does not exist in year {year}.")

reformatted_lines = []
i = 0
while i < len(lines):
    date = lines[i].strip()

    date = format_date(date)
    description = lines[i+1].strip()
    amount = lines[i+2].strip()
    
    reformatted_line = f"{date}\t{description}\t{amount}"
    reformatted_lines.append(reformatted_line)
    
    i += 3

with open('out.txt', 'w') as outfile:
    outfile.write('\n'.join(reformatted_lines[::-1]))