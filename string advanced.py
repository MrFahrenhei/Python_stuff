# advanced strings
print("advanced strings:")
my_name = "Heath"
print(my_name[0])  # first initial
print(my_name[-1])  # last letter

sentence = "This is a sentence."

print(sentence[:4])  # first word
print(sentence[-9:-1])  # last word


print(sentence.split())  # split sentence by delimiter (space)

sentence_split = sentence.split()
sentence_join = ' '.join(sentence_split)
print(sentence_join)
print('\n'.join(sentence_split))


def favorite_book(title, author):
    fav = "meu livro favorito e \"{}\", wich is written by {}.".format(
        title, author)
    return fav


print(favorite_book("The Great Gatsby", "F. Scoot Fitzgerald"))
