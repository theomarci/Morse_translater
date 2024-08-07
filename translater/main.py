import module_morse
import module_fr_into_morse

def Traductor(morse_text):
    split_text = morse_text.split(" ")
    trad_morse = []

    for i in split_text:
        morse = module_morse.MORSE_CODE[i]
        trad_morse.append(morse)
    
    string_trad = ''.join(trad_morse)
    print(string_trad)
    return

def Fr_traduction (fr_text):
    letter_list = []
    text = []

    for i in fr_text:
        letter_list.append(i)
    
    for item in letter_list:
        in_morse = module_fr_into_morse.FR_TO_MORSE[item]
        text.append(in_morse)

    string_in_morse = ' '.join(text)
    print(string_in_morse)

    return

morse_text = ".--- .----. .- .."

Traductor(morse_text)

morse_text = "-.-. --- -. -. .- .-. -.. -.-.-----. / - ..- / . ... - / -.-. .... .. .- -. - -.-.-----."
Traductor( morse_text)

morse_text = """...- . ..- -..- / - ..- / . - .-. . / -- .- / - . -- --- .. -. ..--.."""
Traductor(morse_text)

morse_text = """-.-. --- -- -- . - / ...- .- ... / - ..- ..--.."""
Traductor(morse_text)

morse_text = """.. / .-.. --- ...- . / -.-- --- ..- / ... --- / -- ..- -.-. .... -.-.-----."""
Traductor(morse_text)

morse_text = ("--- .... -.-.-----. / .-.. .- / .-.. .- -.-.-----. /"
              " -- .- .. ... / .--. --- ..- .-. .--. ..- --- .. / "
              "-.-. .----. . ... - / -.-. --- -- -- . / -.-.. .- / "
              "..--.. / .--. --- ..- .-. --.- ..- --- .. / .-.. .----. .- ...- . -. - ..- .-. . / "
              "-.-. .----. . ... - / .--. .- ... / -.-. --- -- -- . / ---- . --.. / .-.. . ... / "
              ". .-.. ..-. . ... --..-- / .- ...- . -.-. / -.. . ... / .--. --- -. . -.-- ... / --. . -. - .. .-.. ... / "
              ". - / -.. . ... / .--. . - .. - ... / .-.. .- .--. .. -. ... / ..--.. / .--. --- ..- .-. --.- ..- --- .. / "
              "-.-- / .- -....- - -....- .. .-.. / - --- ..- .--- --- ..- .-. ... / -.. . ... / --. . -. ... / -- ..-.. ---- .- -. - ... / "
              "--.- ..- .. / ...- . ..- .-.. . -. - / -. --- ..- ... / - ..- . .-. / ..--.. / "
              ". - / -.-. --- -- -- . -. - / --- -. / ...- .- / ..-. .- .. .-. . / "
              ".--. --- ..- .-. / -. . - - --- -.-- . .-. / -. --- ... / ...- .-..- - . -- . -. - ... / ..--..")
Traductor(morse_text)

fr_text = "j'ai eu un coup de foudre!"
Fr_traduction(fr_text)

fr_text = "you're so kind!"
Fr_traduction(fr_text)

fr_text = ("elle se prend pas pour une bouse de troll, celle-là. qu'est-ce qu'on ferait sans elle ? "
           "pour commencer, on arrèterait d'avoir tout le temps des conversations incompréhensibles. "
           "c'est toujours pareil, avec ces bidules déphasés, ses machins cosmoploubiques et ses augmentations de puissance transversale "
           "sur l'orientation pipeautesque de l'énergie de mon cul. si elle n'était pas là, et bien... on aurait pas été téléportés par erreur dans le chateau de gzor, "
           "et je n'aurais pas perdu mon unique point de destin dans une bataille contre la taupe-garous géante! et on serait sortis normalement de la forèt de schlipak, "
           "et on aurait fait l'aventure quand mème, parce que sa magie, elle n'a servi à rien.")
Fr_traduction(fr_text)