define n = Character("Narrador")

transform floating_map:
    linear 3.0 yoffset 10
    linear 3.0 yoffset -10
    repeat

transform small_icon:
    zoom 0.15
    alpha 0.8

image bg_guerra = Movie(
    play="Videos/CampoBatalla.webm",
    loop=True,
    size=(config.screen_width, config.screen_height)
)
image bg_disparo = Movie(
    play="Videos/Disparo.webm",
    loop=True,
    size=(config.screen_width, config.screen_height)
)
image bg_impacto = Movie(
    play="Videos/Impacto.webm",
    loop=True,
    size=(config.screen_width, config.screen_height)
)
image bg_destello = Movie(
    play="Videos/destellos.webm",
    loop=True,
    size=(config.screen_width, config.screen_height)
)
image bg_masacre = Movie(
    play="Videos/masacre.webm",
    loop=True,
    size=(config.screen_width, config.screen_height)
)
image bg_soldadoNota = Movie(
    play="Videos/SoldadoNota.webm",
    loop=True,
    size=(config.screen_width, config.screen_height)
)
image bg_tomandoNota = Movie(
    play="Videos/TomandoNota.webm",
    loop=True,
    size=(config.screen_width, config.screen_height)
)
image bg_levantar = Movie(
    play="Videos/Levantar.webm",
    loop=True,
    size=(config.screen_width, config.screen_height)
)
image bg_tumbas = Movie(
    play="Videos/Tumbas.webm",
    loop=True,
    size=(config.screen_width, config.screen_height)
)

image banderaTumbas = "tumbaBandera.png"

label start:

    play music "musica_batalla.ogg" fadein 2.0

    # Escena 1
    scene bg_guerra with fade
    window show
    n "Estás en el campo de batalla, defendiendo de los ataques enemigos."
    n "Luchas junto a tus compañeros con armas viejas y poca munición."
    hide black

    scene bg_disparo with fade
    window show
    n "De repente, un soldado enemigo fija su mirada en ti. El fogonazo de su rifle corta la penumbra."
    hide black

    scene bg_impacto with fade
    window show
    n "El estruendo retumba en tus oídos… el dolor atraviesa tu pecho como fuego."
    hide black

    scene bg_destello with fade
    window show
    n "El mundo se apaga...."
    hide black
     
    # Escena 3
    scene bg_masacre with fade
    window show
    n "Abres los ojos, pero ya no son ojos de carne. Tus manos tiemblan, translúcidas, fantasmales."
    n "Has dejado el cuerpo atrás, y sin embargo sigues aquí, en medio de la guerra."
    n "El suelo está sembrado de cuerpos sin vida, hermanos caídos..."
    n "El aire es denso, la bruma lo cubre todo… pero aún puedes sentir la esperanza que dejaron en su último aliento."
    hide black
    # Video 4
    scene bg_soldadoNota with fade
    window show
    n "Entre tantos cuerpos, uno atrae tu mirada. Su mano aferrada a un papel manchado de suciedad, resiste incluso a la muerte."
    hide black

    # Video 5
    scene bg_tomandoNota with fade
    window show
    n "Extiendes tu mano espectral y tomas la nota."
    n "El papel se ilumina bajo tu tacto, como si reconociera tu espíritu."
    n "\"Los días cada vez son más duros, lucha tras lucha y muerte tras muerte...\""
    n "\"No sueño con otro día de vida… sueño con un futuro soberano.\""
    hide black

    # Video 6
    scene bg_levantar with fade
    window show
    n "Tus rodillas se clavan en la tierra. La rabia arde en tu pecho, más fuerte que el miedo."
    n "Comprendes que no has vuelto para descansar, sino para luchar desde la memoria."
    hide black

    scene bg_tumbas with fade
    window show
    n "Cuando levantas la mirada, el campo se transforma."
    n "Un sendero de tumbas se abre frente a ti, cada una marcada por un marco vacío..."
    n "Flores frescas reposan sobre ellas, y en cada pétalo palpita la gratitud de un pueblo."
    n "No hay olvido en estas cruces mudas."
    n "Aquí viven los guerreros que dieron su vida por la libertad de Nicaragua..."
    n "Aunque sus cuerpos no fueran hallados, aunque sus nombres se perdieran en la bruma..."
    n "Siguen vivos en el corazón de su patria… como raíces, como orgullo eterno."
    hide black

    scene banderaTumbas with fade
    n "QUIEN NO CONOCE SU HISTORIA ESTA CONDENADO A REPETIRLA..."
    hide v8

    stop music fadeout 2.0
    play music "audio/menu.mp3" fadein 2.0
    call screen mapa_menu

label historia1:
    scene bg city with fade
    "Aquí empieza la primera historia..."
    return

label historia2:
    scene bg jungle with fade
    "Aquí empieza la segunda historia..."
    return

# Pantalla del mapa
screen mapa_menu():
    tag menu 

    add Movie(play="lago.webm", loop=True) xysize(1.0, 1.0) 
    add "menu.png" at floating_map xalign 0.5 yalign 0.5

    imagebutton:
        idle "icono1.png"
        xpos 800
        ypos 250
        at small_icon
        action Jump("historia1")

    imagebutton:
        idle "icono2.png"
        xpos 700
        ypos 500
        at small_icon
        action Jump("historia2")




