import json, random

with open("words.json", "r", encoding='utf-8') as f: words = json.load(f)
lenght = 5
b = list('абвгдеёжзийклмнопрстуфхцчшщъыьэюя')
l = [b[:] for _ in range(lenght)]
ll = set()
def correct(word):
	for i in range(lenght):
		if word[i] not in l[i]:
			return False
	for i in ll:
		if i not in list(word):
			return False
	return True

while True:
	wordd = []
	for word in words:
		if correct(word):
			wordd.append(word)
	if not wordd:
		print("Слово не найдено!")
		break
	word = random.choice(wordd)
	if len(wordd) == 1:
		print(f"{word}. Вы выйграли!")
		break
	print(f"{word} + {len(wordd)-1} слов ещё")
	print("0 - черное 1 - желтое 2 - зеленое")
	c = list(map(int,input().split()))
	if len(c) == 1: 
		words.remove(word)
		continue
	if len(c) != lenght: continue
	for i in range(len(c)):
		if c[i] == 0:
			if word[i] not in ll:
				for j in range(len(l)):
					if l[j].count(word[i]):
						l[j].remove(word[i])
		if c[i] == 1:
			ll.add(word[i])
			if l[i].count(word[i]):
				l[i].remove(word[i])
		if c[i] == 2:
			ll.add(word[i])
			l[i] = [word[i]]





