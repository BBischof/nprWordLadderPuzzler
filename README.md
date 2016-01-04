# NPR Puzzler Solution

## Orignal Problem Statement

This is a variation on the old word ladder puzzle. The object is to change WHOLE to HEART by either adding or subtracting one letter at a time, making a new, common, uncapitalized word at each step.

For example, you can change RED to ROSE in five steps. Starting with RED, you could add a U, making RUED; drop the D, leaving RUE; add an S, making RUSE; add an O, making ROUSE, and then drop the U, leaving ROSE.

Changing or rearranging letters is not allowed, neither are plurals or verbs formed by adding -S. No word in the chain can have fewer than three letters.

How many steps are needed to change WHOLE to HEART? I have my best answer. We'll compare results next week.

## Approach

Take a standard list of english words, read in words, generate a graph where nodes are words and edges between two words exist if one word is simple one letter removal from the other. For example:

```
camp -> cap
```
by removing the "m" so these would have an edge.

Thus, a word latter is simply the shortest path between two nodes.

## Specifics

I use 
```
cat /usr/share/dict/words | awk '{print length, $0}' | sort -n -s | cut -d" " -f2- | awk '{print tolower($0)}' | awk '!a[$0]++'
```
to create a length sorted list of lowercase words with no duplicates.

I like the list to be length sorted ascendingly because it is easier to build the dictionary this way.

I build the dictionary by removing each letter in the incoming line, and checking if the other letters form a word that is already in my dictionary. Since the incoming words are length sorted, if they're in the list, they'll already be in the dictionary. I then create a edge if so. Otherwise, I just add the new word as a node with no edges(this is to maintain that the graph has all words.) Finally, I run shortest path and print the length.

## Usage

The script takes two command line arguments: the two words you would like to find a ladder between. Order of the words doesn't matter since direction in this case is irrelevant.

E.g.:
```
python wordLadderGraph.py life death
```

Sample Output:
```
['life', 'ife', 'fe', 'e', 'ea', 'ear', 'hear', 'heart', 'hearth', 'earth', 'dearth', 'death'] 12
['life', 'ife', 'ie', 'e', 'ea', 'ear', 'hear', 'heart', 'hearth', 'earth', 'dearth', 'death'] 12
['life', 'lie', 'ie', 'e', 'ea', 'ear', 'hear', 'heart', 'hearth', 'earth', 'dearth', 'death'] 12
['life', 'ife', 'fe', 'e', 'er', 'ear', 'hear', 'heart', 'hearth', 'earth', 'dearth', 'death'] 12
['life', 'ife', 'ie', 'e', 'er', 'ear', 'hear', 'heart', 'hearth', 'earth', 'dearth', 'death'] 12
['life', 'lie', 'ie', 'e', 'er', 'ear', 'hear', 'heart', 'hearth', 'earth', 'dearth', 'death'] 12
['life', 'lifer', 'lier', 'ler', 'er', 'ear', 'hear', 'heart', 'hearth', 'earth', 'dearth', 'death'] 12
['life', 'lie', 'lier', 'ler', 'er', 'ear', 'hear', 'heart', 'hearth', 'earth', 'dearth', 'death'] 12
['life', 'lifer', 'lier', 'ler', 'lear', 'ear', 'hear', 'heart', 'hearth', 'earth', 'dearth', 'death'] 12
['life', 'lie', 'lier', 'ler', 'lear', 'ear', 'hear', 'heart', 'hearth', 'earth', 'dearth', 'death'] 12
['life', 'ife', 'fe', 'e', 'er', 'her', 'hear', 'heart', 'hearth', 'earth', 'dearth', 'death'] 12
['life', 'ife', 'ie', 'e', 'er', 'her', 'hear', 'heart', 'hearth', 'earth', 'dearth', 'death'] 12
['life', 'lie', 'ie', 'e', 'er', 'her', 'hear', 'heart', 'hearth', 'earth', 'dearth', 'death'] 12
['life', 'lifer', 'lier', 'ler', 'er', 'her', 'hear', 'heart', 'hearth', 'earth', 'dearth', 'death'] 12
['life', 'lie', 'lier', 'ler', 'er', 'her', 'hear', 'heart', 'hearth', 'earth', 'dearth', 'death'] 12
['life', 'ife', 'fe', 'e', 'he', 'her', 'hear', 'heart', 'hearth', 'earth', 'dearth', 'death'] 12
['life', 'ife', 'ie', 'e', 'he', 'her', 'hear', 'heart', 'hearth', 'earth', 'dearth', 'death'] 12
['life', 'lie', 'ie', 'e', 'he', 'her', 'hear', 'heart', 'hearth', 'earth', 'dearth', 'death'] 12
['life', 'ife', 'ie', 'hie', 'he', 'her', 'hear', 'heart', 'hearth', 'earth', 'dearth', 'death'] 12
['life', 'lie', 'ie', 'hie', 'he', 'her', 'hear', 'heart', 'hearth', 'earth', 'dearth', 'death'] 12
['life', 'lifer', 'lier', 'ler', 'hler', 'her', 'hear', 'heart', 'hearth', 'earth', 'dearth', 'death'] 12
['life', 'lie', 'lier', 'ler', 'hler', 'her', 'hear', 'heart', 'hearth', 'earth', 'dearth', 'death'] 12
['life', 'ife', 'fe', 'e', 'ea', 'eat', 'heat', 'heart', 'hearth', 'earth', 'dearth', 'death'] 12
['life', 'ife', 'ie', 'e', 'ea', 'eat', 'heat', 'heart', 'hearth', 'earth', 'dearth', 'death'] 12
['life', 'lie', 'ie', 'e', 'ea', 'eat', 'heat', 'heart', 'hearth', 'earth', 'dearth', 'death'] 12
['life', 'ife', 'fe', 'fet', 'feat', 'eat', 'heat', 'heart', 'hearth', 'earth', 'dearth', 'death'] 12
['life', 'ife', 'fe', 'e', 'he', 'het', 'heat', 'heart', 'hearth', 'earth', 'dearth', 'death'] 12
['life', 'ife', 'ie', 'e', 'he', 'het', 'heat', 'heart', 'hearth', 'earth', 'dearth', 'death'] 12
['life', 'lie', 'ie', 'e', 'he', 'het', 'heat', 'heart', 'hearth', 'earth', 'dearth', 'death'] 12
['life', 'ife', 'ie', 'hie', 'he', 'het', 'heat', 'heart', 'hearth', 'earth', 'dearth', 'death'] 12
['life', 'lie', 'ie', 'hie', 'he', 'het', 'heat', 'heart', 'hearth', 'earth', 'dearth', 'death'] 12
['life', 'ife', 'fe', 'e', 'ea', 'eat', 'heat', 'heath', 'hearth', 'earth', 'dearth', 'death'] 12
['life', 'ife', 'ie', 'e', 'ea', 'eat', 'heat', 'heath', 'hearth', 'earth', 'dearth', 'death'] 12
['life', 'lie', 'ie', 'e', 'ea', 'eat', 'heat', 'heath', 'hearth', 'earth', 'dearth', 'death'] 12
['life', 'ife', 'fe', 'fet', 'feat', 'eat', 'heat', 'heath', 'hearth', 'earth', 'dearth', 'death'] 12
['life', 'ife', 'fe', 'e', 'he', 'het', 'heat', 'heath', 'hearth', 'earth', 'dearth', 'death'] 12
['life', 'ife', 'ie', 'e', 'he', 'het', 'heat', 'heath', 'hearth', 'earth', 'dearth', 'death'] 12
['life', 'lie', 'ie', 'e', 'he', 'het', 'heat', 'heath', 'hearth', 'earth', 'dearth', 'death'] 12
['life', 'ife', 'ie', 'hie', 'he', 'het', 'heat', 'heath', 'hearth', 'earth', 'dearth', 'death'] 12
['life', 'lie', 'ie', 'hie', 'he', 'het', 'heat', 'heath', 'hearth', 'earth', 'dearth', 'death'] 12
['life', 'ife', 'fe', 'e', 'er', 'ber', 'bert', 'berth', 'erth', 'earth', 'dearth', 'death'] 12
['life', 'ife', 'ie', 'e', 'er', 'ber', 'bert', 'berth', 'erth', 'earth', 'dearth', 'death'] 12
['life', 'lie', 'ie', 'e', 'er', 'ber', 'bert', 'berth', 'erth', 'earth', 'dearth', 'death'] 12
['life', 'lifer', 'lier', 'ler', 'er', 'ber', 'bert', 'berth', 'erth', 'earth', 'dearth', 'death'] 12
['life', 'lie', 'lier', 'ler', 'er', 'ber', 'bert', 'berth', 'erth', 'earth', 'dearth', 'death'] 12
['life', 'ife', 'fe', 'e', 'be', 'ber', 'bert', 'berth', 'erth', 'earth', 'dearth', 'death'] 12
['life', 'ife', 'ie', 'e', 'be', 'ber', 'bert', 'berth', 'erth', 'earth', 'dearth', 'death'] 12
['life', 'lie', 'ie', 'e', 'be', 'ber', 'bert', 'berth', 'erth', 'earth', 'dearth', 'death'] 12
['life', 'ife', 'fe', 'e', 'be', 'bet', 'bert', 'berth', 'erth', 'earth', 'dearth', 'death'] 12
['life', 'ife', 'ie', 'e', 'be', 'bet', 'bert', 'berth', 'erth', 'earth', 'dearth', 'death'] 12
['life', 'lie', 'ie', 'e', 'be', 'bet', 'bert', 'berth', 'erth', 'earth', 'dearth', 'death'] 12
['life', 'ife', 'fe', 'e', 'be', 'bet', 'beth', 'berth', 'erth', 'earth', 'dearth', 'death'] 12
['life', 'ife', 'ie', 'e', 'be', 'bet', 'beth', 'berth', 'erth', 'earth', 'dearth', 'death'] 12
['life', 'lie', 'ie', 'e', 'be', 'bet', 'beth', 'berth', 'erth', 'earth', 'dearth', 'death'] 12
['life', 'ife', 'fe', 'e', 'ye', 'yet', 'yeth', 'yerth', 'erth', 'earth', 'dearth', 'death'] 12
['life', 'ife', 'ie', 'e', 'ye', 'yet', 'yeth', 'yerth', 'erth', 'earth', 'dearth', 'death'] 12
['life', 'lie', 'ie', 'e', 'ye', 'yet', 'yeth', 'yerth', 'erth', 'earth', 'dearth', 'death'] 12
['life', 'ife', 'fe', 'e', 'ye', 'yet', 'yeth', 'yerth', 'yearth', 'earth', 'dearth', 'death'] 12
['life', 'ife', 'ie', 'e', 'ye', 'yet', 'yeth', 'yerth', 'yearth', 'earth', 'dearth', 'death'] 12
['life', 'lie', 'ie', 'e', 'ye', 'yet', 'yeth', 'yerth', 'yearth', 'earth', 'dearth', 'death'] 12
```