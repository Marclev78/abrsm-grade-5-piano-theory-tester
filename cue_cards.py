import random
import copy

cueCards = [  # words in grade 5 theory
    {"term": "A tempo", "english": "In time"},
    {"term": "Accelerando (Accel)", "english": "Gradually getting faster"},
    {"term": "Ad libitum (Ad lib.)", "english": "At choice"},
    {"term": "Adagio", "english": "Slow"},
    {"term": "Affettuoso", "english": "Tenderly"},
    {"term": "Agitato", "english": "Agitated"},
    {"term": "Al, alla", "english": "In the style of"},
    {"term": "Alla breve", "english": "With a minim beat"},
    {"term": "Allargando", "english": "Broadening"},
    {"term": "Allegretto", "english": "Fairly quick"},
    {"term": "Allegro", "english": "Fast"},
    {"term": "Allegro assai", "english": "Very fast"},
    {"term": "Allegro moderato", "english": "Moderately fast"},
    {"term": "Amabile", "english": "Amiable, pleasant"},
    {"term": "Andante", "english": "At a walking pace"},
    {"term": "Andantino", "english": "Slightly faster than andante"},
    {"term": "Animato", "english": "Animated, lively"},
    {"term": "Animé", "english": "Animated, lively"},
    {"term": "Appassionato", "english": "With passion"},
    {"term": "Assai", "english": "Very"},
    {"term": "Attacca", "english": "Go immediately to next section"},
    {"term": "Ben", "english": "Well"},
    {"term": "Brio", "english": "Vigour"},
    {"term": "Cantabile", "english": "In a singing style"},
    {"term": "Cantando", "english": "Singing"},
    {"term": "Come", "english": "As, similar to"},
    {"term": "Comodo", "english": "At a comfortable speed"},
    {"term": "Con, col", "english": "With"},
    {"term": "Crescendo (Cresc.)", "english": "Gradually getting louder"},
    {"term": "Da capo (D.C.)", "english": "Repeat from beginning"},
    {"term": "Dal segno (D.S.)", "english": "Repeat from \"S\" sign"},
    {"term": "Deciso", "english": "With determination"},
    {"term": "Decrescendo (Decresc.)   ", "english": "Gradually getting quieter"},
    {"term": "Diminuendo (Dim.)", "english": "Gradually getting quieter"},
    {"term": "Dolce", "english": "Sweet, soft"},
    {"term": "Dolore", "english": "Grief, sorrow"},
    {"term": "Doloroso", "english": "Sorrowful"},
    {"term": "Douce", "english": "Sweet"},
    {"term": "E, ed", "english": "And"},
    {"term": "Energico", "english": "Energetic"},
    {"term": "Espressivo (espress.)", "english": "Expressive"},
    {"term": "Fine", "english": "The end"},
    {"term": "Forte (f)", "english": "Loud"},
    {"term": "Fortepiano (fp)", "english": "Loud, then immediately soft"},
    {"term": "Fortissimo (ff)", "english": "Very Loud"},
    {"term": "Forza", "english": "Force"},
    {"term": "Giocoso", "english": "Playful, merry"},
    {"term": "Grave", "english": "Very slow, solemn"},
    {"term": "Grazioso", "english": "Graceful"},
    {"term": "Langsam", "english": "Slow"},
    {"term": "Largamente", "english": "Broadly"},
    {"term": "Larghetto", "english": "Rather slow"},
    {"term": "Largo", "english": "Slow and stately"},
    {"term": "Lebhaft", "english": "Lively"},
    {"term": "Legato", "english": "Smoothly"},
    {"term": "Leggiero", "english": "Light, nimble"},
    {"term": "Lent", "english": "Slow"},
    {"term": "Lento", "english": "Slow"},
    {"term": "Ma", "english": "But"},
    {"term": "Maestoso", "english": "Majestic"},
    {"term": "Marcato (marc.)", "english": "Emphatic, accented"},
    {"term": "Marcia", "english": "March"},
    {"term": "Mässig", "english": "At a moderate speed"},
    {"term": "Meno", "english": "Less"},
    {"term": "Mesto", "english": "Sad"},
    {"term": "Mezzo", "english": "Half"},
    {"term": "Mezzo forte (mf)", "english": "Moderately loud"},
    {"term": "Mezzo piano (mp)", "english": "Moderately quiet"},
    {"term": "Misterioso", "english": "Mysteriously"},
    {"term": "Moderato", "english": "Moderate speed"},
    {"term": "Modéré", "english": "At a moderate speed"},
    {"term": "Molto", "english": "Very much"},
    {"term": "Morendo", "english": "Dying away"},
    {"term": "Mosso", "english": "Movement"},
    {"term": "Moto", "english": "Movement"},
    {"term": "Niente", "english": "Nothing (silence)"},
    {"term": "Non", "english": "Not"},
    {"term": "Perdendosi", "english": "Dying away"},
    {"term": "Pesante", "english": "Heavy"},
    {"term": "Pianissimo (pp)", "english": "Very quiet"},
    {"term": "Piano (p)", "english": "Quiet"},
    {"term": "Più", "english": "More"},
    {"term": "Poco", "english": "A little"},
    {"term": "Poco a poco", "english": "Little by little"},
    {"term": "Prestissimo", "english": "As fast as possible"},
    {"term": "Presto", "english": "Fast (faster than allegro)"},
    {"term": "Prima, primo", "english": "First"},
    {"term": "Quasi", "english": "As if, resembling"},
    {"term": "Rallentando (Rall.)", "english": "Gradually getting slower"},
    {"term": "Retenu", "english": "Held back"},
    {"term": "Rinforzando (rf, rfz, rinf.)", "english": "Reinforcing"},
    {"term": "Risoluto", "english": "Bold, strong"},
    {"term": "Ritardando (rit., ritard.)", "english": "Gradually getting slower"},
    {"term": "Ritenuto (rit., riten.)", "english": "Held back"},
    {"term": "Ritmico", "english": "Rhythmically"},
    {"term": "Rubato", "english": "With some freedom of time"},
    {"term": "Ruhig", "english": "Peaceful"},
    {"term": "Scherzando", "english": "Playfully, joking"},
    {"term": "Schnell", "english": "Fast"},
    {"term": "Semplice", "english": "Simple, plain"},
    {"term": "Sempre", "english": "Always"},
    {"term": "Senza", "english": "Without"},
    {"term": "Sforzando (sf)", "english": "Forced, accented"},
    {"term": "Sforzato (sfz)", "english": "Forced, accented"},
    {"term": "Simile (sim.)", "english": "In the same way"},
    {"term": "Smorzando (smorz.)", "english": "Dying away in tone and speed"},
    {"term": "Sonoro", "english": "Resonant, with a rich tone"},
    {"term": "Sostenuto", "english": "Sustained"},
    {"term": "Sotto voce", "english": "In an undertone"},
    {"term": "Spirito", "english": "Spirit"},
    {"term": "Staccato (stacc.)", "english": "Detached"},
    {"term": "Stringendo", "english": "Gradually getting faster"},
    {"term": "Subito (sub.)", "english": "Suddenly"},
    {"term": "Tempo", "english": "Speed, time"},
    {"term": "Tenuto", "english": "Held"},
    {"term": "Tranquillo", "english": "Calm"},
    {"term": "Traurig", "english": "Sad"},
    {"term": "Tristamente, Triste", "english": "Sorrowful"},
    {"term": "Troppo", "english": "Too much"},
    {"term": "Vite", "english": "Quick"},
    {"term": "Vivace, vivo", "english": "Lively, quick"}
]

remaining_questions = copy.deepcopy(cueCards)
count = 1
right_answers = 0
wrong_answers = 0
while len(remaining_questions) > 0:
    used_numbers = []

    banana = 0
    if len(remaining_questions) > 1:
        banana = random.randrange(0, len(remaining_questions) - 1)

    right_answer = remaining_questions[banana]
    del remaining_questions[banana]

    print("\033[94m[" + str(count) + "] What does '" + right_answer["term"] + "' mean? Choose:")
    count = count + 1
    right_answer_position = random.randrange(0, 4)

    for i in range(5):
        if i == right_answer_position:
            print("\033[95m(" + str(i + 1) + ") " + right_answer["english"])
        else:
            wrong_answer_number = -1
            wrong_answer = -1
            while wrong_answer_number in used_numbers \
                    or wrong_answer_number == -1 \
                    or wrong_answer["term"] == right_answer["term"]:
                wrong_answer_number = random.randrange(0, len(cueCards) - 1)
                wrong_answer = cueCards[wrong_answer_number]

            used_numbers.append(wrong_answer_number)
            print("\033[95m(" + str(i + 1) + ") " + wrong_answer["english"])

    guess = input("\033[96mAnswer (1, 2, 3, 4, or 5)? : ")

    if guess == str(right_answer_position + 1):
        print("\033[92mYou got the right answer, yay!")
        right_answers = right_answers + 1
    else:
        print("Boo, you suck! Try again. It was:\033[93m " + right_answer["english"])
        wrong_answers = wrong_answers + 1
    print("---")

print("\033[92mFinished. Correct answers: " + str(right_answers) + "/" + str(len(cueCards)))
