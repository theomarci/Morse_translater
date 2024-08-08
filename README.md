<img src="https://github.com/theomarci/Morse_translater/blob/main/readme_picture/gif_morse.gif" alt="gif about morse">

<h1 align="center">Morse translation project</h1>

<br>

<h3>Introduction :</h4>

<p>
  I'm happy to show you a little project which translate a morse words or sentences into french or english and vice versa. This is a little project to practice python and revise the base about this programming language. Also, I learn to code test with python.
</p>

<br>

<h3>stack :</h3>

<img src="./readme_picture/python.png" alt="python logo" width="50px">

<br>

<h3>Step by step :</h3>

<h5>step 1:</h5>

<p>
  I've started my project in creating a dictionnary where I saved key and values (morse codes and his significations for each) all in lower case with every alphabetical letters, some special letters like "é" or "ç" and ponctuation, plus for space between words.
</p>

<h5>Step 2 :</h5>

<p>
  I built my first functions named "Morse_translation" whicht take one parameter "morse_text". This function return a string with a translation of the morse code saved in the previous variable. For that, I declared a variable which split the morse code with the python method split(). This method divided a string and store each elements divided in a list. Next, I created an empty list. After that, I looped each element of my first list to reach in the dictionary that fit with the right key and get back the right translation. Then I store this values in the empty list with python method .append(). And finally, where every elements have his translation store in the list, and I used an another method .join(), that transform the list in a string.
</p>

<h5>Step 3 :</h5>

<p>
  Now, I had a function but "Does it work ?". In this step, I didn't built a test with the library pytest. I test my function simply with a set of function call for each I wrote various words and sentences that I ran on my terminal. It was a succeed !<br>
  See : 
</p>

```
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
Morse_translation(morse_text)

#Output
#oh! la la! mais pourpuoi c'est comme ça ? pourquoi l'aventure c'est pas comme chez les elfes, avec des poneys
#gentils et des petits lapins ? pourquoi y a-t-il toujours des gens méchants qui veulent nous tuer ? et comment
#on va faire pour nettoyer nos vètements ?
```
<p>
  The sentence come from the french mp3 adventure : le Donjon de Naheulbeuk. 
</p>

<h5>Step 4 :</h5>

<P>
  Now I did the same steps that the previous to translate a french or english words or sentences to morse but with some difference.<br>
  First, I create an new dictionary but where the key is an alphabetical letters and value his translation. Next I created a new function named "Fr_translation". Inside it, I didn't used the split method but I replaced it with 
  two empty list. "Why ?" you'll tell me. One of them is, like previous step, to store the translation but the other one is to store each elements of my string which stored in the parameter of my function, even space between words. Then, I used the append() method to add on an empty list for each elements. Next, I looped with each elements of the list and reach the right values that I added to my other list. after that, I used the join() method to concatenate each elements in a single string.<br>
  See this example :
</P>

```
fr_text = ("elle se prend pas pour une bouse de troll, celle-là. qu'est-ce qu'on ferait sans elle ? "
           "pour commencer, on arrèterait d'avoir tout le temps des conversations incompréhensibles. "
           "c'est toujours pareil, avec ces bidules déphasés, ses machins cosmoploubiques et ses augmentations de puissance transversale "
           "sur l'orientation pipeautesque de l'énergie de mon cul. si elle n'était pas là, et bien... on aurait pas été téléportés par erreur dans le chateau de gzor, "
           "et je n'aurais pas perdu mon unique point de destin dans une bataille contre la taupe-garous géante! et on serait sortis normalement de la forèt de schlipak, "
           "et on aurait fait l'aventure quand mème, parce que sa magie, elle n'a servi à rien.")
Fr_translation(fr_text)

#output :
#. .-.. .-.. . / ... . / .--. .-. . -. -.. / .--. .- ... / .--. --- ..- .-. / ..- -. . / -... --- ..- ... . / -.. . /
#- .-. --- .-.. .-.. --..-- / -.-. . .-.. .-.. . -...- .-.. .--.- .-.-.- / --.- ..- .----. . ... - -...- -.-. . /
#--.- ..- .----. --- -. / ..-. . .-. .- .. - / ... .- -. ... / . .-.. .-.. . / ..--.. / .--. --- ..- .-. /
#-.-. --- -- -- . -. -.-. . .-. --..-- / --- -. / .- .-. .-. .-..- - . .-. .- .. - / -.. .----. .- ...- --- .. .-. /
#- --- ..- - / .-.. . / - . -- .--. ... / -.. . ... / -.-. --- -. ...- . .-. ... .- - .. --- -. ... /
#.. -. -.-. --- -- .--. .-. ..-.. .... . -. ... .. -... .-.. . ... .-.-.- / -.-. .----. . ... - / - --- ..- .--- --- ..- .-. ... /
#.--. .- .-. . .. .-.. --..-- / .- ...- . -.-. / -.-. . ... / -... .. -.. ..- .-.. . ... / -.. ..-.. .--. .... .- ... ..-.. ... --..-- /
#... . ... / -- .- -.-. .... .. -. ... / -.-. --- ... -- --- .--. .-.. --- ..- -... .. --.- ..- . ... / . - / ... . ... /
#.- ..- --. -- . -. - .- - .. --- -. ... / -.. . / .--. ..- .. ... ... .- -. -.-. . / - .-. .- -. ... ...- . .-. ... .- .-.. . /
#... ..- .-. / .-.. .----. --- .-. .. . -. - .- - .. --- -. / .--. .. .--. . .- ..- - . ... --.- ..- . / -.. . /
#.-.. .----. ..-.. -. . .-. --. .. . / -.. . / -- --- -. / -.-. ..- .-.. .-.-.- / ... .. / . .-.. .-.. . / -. .----. ..-.. - .- .. - / .--. .- ... /
#.-.. .--.- --..-- / . - / -... .. . -. .-.-.- .-.-.- .-.-.- / --- -. / .- ..- .-. .- .. - / .--. .- ... / ..-.. - ..-.. /
#- ..-.. .-.. ..-.. .--. --- .-. - ..-.. ... / .--. .- .-. / . .-. .-. . ..- .-. / -.. .- -. ... / .-.. . / -.-. .... .- - . .- ..- / -.. . /
#--. --.. --- .-. --..-- / . - / .--- . / -. .----. .- ..- .-. .- .. ... / .--. .- ... / .--. . .-. -.. ..- / -- --- -. / ..- -. .. --.- ..- . /
#.--. --- .. -. - / -.. . / -.. . ... - .. -. / -.. .- -. ... / ..- -. . / -... .- - .- .. .-.. .-.. . / -.-. --- -. - .-. . / .-.. .- /
#- .- ..- .--. . -...- --. .- .-. --- ..- ... / --. ..-.. .- -. - . -.-.-----. / . - / --- -. / ... . .-. .- .. - / ... --- .-. - .. ... /
#-. --- .-. -- .- .-.. . -- . -. - / -.. . / .-.. .- / ..-. --- .-. .-..- - / -.. . / ... -.-. .... .-.. .. .--. .- -.- --..-- / . - / --- -. /
#.- ..- .-. .- .. - / ..-. .- .. - / .-.. .----. .- ...- . -. - ..- .-. . / --.- ..- .- -. -.. / -- .-..- -- . --..-- / .--. .- .-. -.-. . /
#--.- ..- . / ... .- / -- .- --. .. . --..-- / . .-.. .-.. . / -. .----. .- / ... . .-. ...- .. / .--.- / .-. .. . -. .-.-.-
```

<h5>Step 5 :</h5>

<p>
  In this step, I decided to create a repository, clone on my local, copy all files and pastes in my repo. Then, I created the readme and wrote some information in my main file.
</p>

<h5>Step 6 :</h5>

<p>
  To finish, this tiny project, I decided to learn the unit test in python and in particular the framework Pytest. The beginning was chaotic but after some research I resolve my problems about my installation. Then, I use the Pytest documentation to write my first line of code to test my functions. It's just the beginning so I don't want to write a lot of test code for any case. An another problem, I think, I must to write test first before to code my projects.  
</p>

<h3>Conclusion :</h3>

<p>
  This little project isn't difficult for me but it's important to practice sometimes the base and learn new thing, like Pytest. 
</p>
