with open('othello.txt', mode='r', encoding='utf8') as prose_file:

    prose_text = prose_file.read() #text from poem saved to this variable now

prose_lines = prose_text.splitlines() # prose lines is a list of the lines from text

new_prose_lines = [] #empty var list



for i in range(len(prose_lines)):

    prose_lines[i] = prose_lines[i].strip()

    if i%5 == 0:
        new_prose_lines.append( f'{prose_lines[i]:<86}{i:>4}')
    else:
        new_prose_lines.append(f'{prose_lines[i]:<52}')

new_prose_text = '\n'.join(new_prose_lines)

with open('formattedothello.txt', mode='w', encoding='utf8') as prose_format:
    prose_format.write(new_prose_text)




#musterloesung linenumber
#poem_file = open("poem.txt", encoding="utf-8")
#poem_text = poem_file.read()
#poem_file.close()

#first difference: save poem to text file and open as read only file

#poem_lines = poem_text.splitlines()
#new_poem_lines = []
#for i in range(len(poem_lines)):
 #   new_poem_lines.append(f"{poem_lines[i]:<78}{i+1:>2}")

#new_poem_text = "\n".join(new_poem_lines)

#new_poem_file = open("poem-out.txt", encoding="utf-8", mode="w")
#new_poem_file.write("\n".join(new_poem_lines))
