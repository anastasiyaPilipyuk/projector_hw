from random import randint
import csv

# Task 1
# generating 26 files with written there random value
for i in range(ord('A'), ord('Z')+1):
    with open(f"temp_files/{chr(i)}.txt", mode='w') as file:
        file.write(str(randint(1, 100)))

# summary file for collect name and value of files from previous part
with open("temp_files/summary.txt", 'w') as sum_file:
    for i in range(ord('A'), ord('Z')+1):
        with open(f"temp_files/{chr(i)}.txt", mode='r', encoding='UTF-8') as file:
            sum_file.writelines(f"{chr(i)}.txt: {str(file.read())}\n")

# Task 2
text = '''Тому що ніколи тебе не вирвеш,
ніколи не забереш,
тому що вся твоя свобода
складається з меж,
тому що в тебе немає
жодного вантажу,
тому що ти ніколи не слухаєш,
оскільки знаєш і так,
що я скажу,'''

# Create file with some content.
with open("temp_files/lyrics.txt", "w", encoding="UTF-8") as file:
    file.write(text)
    
# Create second file and copy content of the first file to the second file in upper case.
with open("temp_files/lyrics.txt", "r", encoding="UTF-8") as file_from, \
        open("temp_files/lyrics_copy.txt", "w", encoding="UTF-8") as file_to:
    file_to.write(file_from.read().upper())


# Task 3

# tuple with player's names
players = ("Josh", "Luke", "Kate", "Mark", "Mary")

list_games = []
headers = ('Player name', 'Score')

# generate list with random game score
for player in players:
    i = 0
    while i < 100:
        list_games.append({headers[0]: player, headers[1]: randint(0, 1000)})
        i += 1

# write created dictionary into cvs file
with open('temp_files/games_results.csv', mode='w', newline='') as file:
    writer = csv.DictWriter(file, fieldnames=headers)
    writer.writeheader()
    writer.writerows(list_games)

# read from cvs file into dictionary with key as player name
dict_high_scores = {}
with open('temp_files/games_results.csv', mode='r') as file:
    reader = csv.DictReader(file)
    for row in reader:
        name = row[headers[0]]
        score = int(row[headers[1]])
        if name in dict_high_scores.keys():
            if int(dict_high_scores[name]) < score:
                dict_high_scores[name] = score
        else:
            dict_high_scores[name] = score

# sort dictionary be value
sorted_high_scores = dict(sorted(dict_high_scores.items(), key=lambda item: item[1], reverse=True))

# write resulting cvs file
with open('temp_files/high_scores.csv', mode='w', newline='') as file:
    writer = csv.writer(file, delimiter=',')
    writer.writerow(headers)
    writer.writerows(sorted_high_scores.items())
