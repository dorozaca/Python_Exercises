from collections import Counter


def most_repeating_word(words):
    
    most_repeating_chars_per_word=[]   
    for i in words:
        word_char_counter=Counter(i)
        most_repeating_chars_per_word.append(word_char_counter.most_common(1))

    top_char_per_word_list_only_number=[]
    for i in most_repeating_chars_per_word:
        top_char_per_word_list_only_number.append((i[0])[1])   # Este truco es importante. Asi podemos acceder a elementos especificos dentro de listas que contienen listas y estas a su vez contienen tuplas
    
    for i in enumerate(top_char_per_word_list_only_number):
        if i[1] == max(top_char_per_word_list_only_number):
            return words[i[0]]                                 #recordar que i no regresa un indice sino cada elemento como esta dentro de una sequencia

       

def run():
    words = ['this', 'is', 'an', 'elementary', 'test', 'example' , 'aaaaaaaaaaa']
    print(most_repeating_word(words))

if __name__=='__main__':
    run()