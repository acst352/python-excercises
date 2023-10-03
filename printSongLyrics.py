# Make a program that displays the lyrics of a song.

# Create a dictionary to store songs and their lyrics
songs = {
    "Cinco ratoncitos": """
        Cinco ratoncitos de colita gris,
        mueven las orejas, mueven la nariz,
        abren los ojitos, comen sin cesar,
        por si viene el gato, que los comerá,
        comen un quesito, y a su casa van,
        cerrando la puerta, a dormir se van.
    """,
    "Todos los patitos": """
        Todos los patitos
        se fueron a nadar
        y el más pequeñito
        se quiso quedar

        su mamá enfadada
        le quiso regañar
        y el pobre patito
        se puso a llorar 

        Los patitos en el agua
        meneaban la colita
        y decían uno al otro
        ay! que agua tan fresquita.

        Los patitos en el agua
        meneaban la colita
        y decían uno al otro
        ay! que agua tan fresquita.
    """,
    "Que llueva": """
        Que llueva, que llueva,
        la virgen de la cueva
        Los pajaritos cantan,
        las nubes se levantan
        Que sí, que no,
        que caiga un chaparrón
        con azúcar y turrón.

        Que siga lloviendo,
        los pájaros corriendo
        Florezca la pradera,
        al sol de primavera
        Que sí, que no,
        que caiga un caparrón
        Con azúcar y turrón

        Y que rompan los cristales
        de la estación

        Que llueva, que llueva,
        la virgen de la cueva
        Los pajaritos cantan,
        las nubes se levantan
        Que sí, que no,
        que caiga un caparrón
        con agua y con jabón,
        arriba del colchón
        Y que no me moje yo.
    """,
}

# Query a specific song
song_name = input("Enter the name of the song: ")

if song_name in songs:
    print(songs[song_name])
else:
    print("The song is not in the database.")