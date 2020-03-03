from notebook import Notebook, Note
from menu import Menu


note = Note('I am Steve Jobs!', 'Steve Jobs')
notebook = Notebook()
print("Created note: 'I am Steve Jobs!'")
print("Created notebook.")

print("\nIs notebook an object?", isinstance(notebook, object))
print("Is note an object?", isinstance(note, object))
print("Is notebook.new_note('Elon Musk', 'Elon') an object?",
      isinstance(notebook.new_note('Elon Musk'), object))
print("Is notebook.search('Elon') an object?",
      isinstance(notebook.search('Elon'), object))
print("Is notebook.__init__() an object?", isinstance(notebook.__init__(),
                                                      object))
print("Is notebook.__str__() a string?", isinstance(notebook.__str__(), str))
print("Is note.memo a string?", isinstance(note.memo, str))
print("Is notebook an object of class Notebook?", isinstance(notebook,
                                                             Notebook))

print("\nIs the word 'Steve' in note?", note.match('I'))
print("Is the word 'love' in note?", note.match('love'))

print("\nAdding new notes to the notebook...")
notebook.new_note('You are not Steve Jobs!', 'answer 1')
notebook.new_note('I am.', 'answer 2')
for note in notebook.notes:
    print('Memo: {}, Tag: {}.'.format(note.memo, note.tags))

print("\nModifying memo of the first note:")
notebook.modify_memo(notebook.notes[0].id, 'Nice boy')
for note in notebook.notes:
    print('Memo: {}, Tag: {}.'.format(note.memo, note.tags))

print("\nModifying tag of the first note:")
notebook.modify_tags(notebook.notes[0].id, 'Boy')
for note in notebook.notes:
    print('Memo: {}, Tag: {}.'.format(note.memo, note.tags))

print("\nSearching the word 'I' in the notebook:")
for note in notebook.search("I"):
    print(note.memo)

print("\nList of attributes and methods of note:\n", dir(note))
print("\nList of attributes and methods of notebook:\n", dir(notebook))
print("\nList of attributes and methods of notebook.new_note('Elon Musk'):\n",
      dir(notebook.new_note('Elon Musk')))
print("\nList of attributes and methods of notebook.search('Elon'):\n",
      dir(notebook.search('Elon')))
print("\nList of attributes and methods of notebook.__init__():\n",
      dir(notebook.__init__()))
print("\nList of attributes and methods of notebook.__str__():\n",
      dir(notebook.__str__()))
print("\nList of attributes and methods of note.memo:\n", dir(note.memo))
print("\nList of attributes and methods of menu:\n", dir(Menu))
