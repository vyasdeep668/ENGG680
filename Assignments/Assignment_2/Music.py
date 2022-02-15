# Course: ENGG 680 Intro to Digital Engineering
# Assignment #: 2
# Topic: Music Room (2.5pt)
# Name: Deep Vyas
# UCID: 30139014

# MusicRoom module with Instruments
class MusicRoom:
    """Holding a list of instrument objects.

    Attributes:
        instruments: List holding Instrument class objects.
    """

    def __init__(self, instruments):
        self.instruments = instruments

    def play(self, song):
        """Plays song on all instruments.

        song: string
        """

        # TODO: Add your code here
        for instrument in self.instruments:
            print(instrument.kind + " plays: " + instrument.play(song))

    def tune(self):
        """Tunes all instruments that are not currently tuned."""

        # TODO: Add your code here
        for instrument in self.instruments:
            if not instrument.is_tuned:
                instrument.is_tuned = True
                print("Tuning {}".format(str(instrument)))


class Instrument:
    """Parent class for instruments

    Attributes:
        kind: string describing the type of instrument
        brand: string instrument maker/brand
        year: string year instrument was made
        is_tuned: bool, True if currently tuned, False otherwise
    """

    kind = 'Instrument'

    def __init__(self, brand, year):
        self.brand = brand
        self.year = year
        self.is_tuned = True

    def __str__(self):
        """Human readable representation of the instrument."""
        # TODO: Add your code here
        string = "a {} {} {}".format(self.year, self.brand, self.kind)
        return string

    def play(self, song):
        """plays song on instrument.

        Song will 'sound' different if instrument is not tuned.

        song: string

        returns: string representing song played
        """
        # TODO: Add your code here
        if self.is_tuned:
            return song
        else:
            return song.swapcase()


# noinspection PyCompatibility
class Guitar(Instrument):
    """ A Guitar extends Instrument

    Instrument kind is 'Guitar'

    de-tunes after playing a song.
    """

    kind = 'Guitar'

    def __init__(self, brand, year):
        super().__init__(brand, year)

    def play(self, song):
        """plays song and de-tunes.

        song: string
        returns: string representing song played
        """
        # TODO: Add your code here
        res = super().play(song)
        # Guitar, de - tunes after every song.
        self.is_tuned = False
        return res


class Bass(Instrument):
    """ A Bass extends Instrument

    Instrument kind is 'Bass'

    de-tunes after playing two songs.

    Attributes:
        detune_count: integer how many songs until de-tuned (default is 2)
        play_count: integer how many songs played
    """

    kind = 'Bass'
    detune_count = 2

    def __init__(self, brand, year):
        super().__init__(brand, year)
        self.play_count = 0

    def play(self, song):
        """plays song and de-tunes if played detune_count songs.

        song: string
        returns: string representing song played
        """
        # TODO: Add your code here
        res = super().play(song)
        # Bass, de - tunes after playing 2 songs.
        self.play_count = self.play_count + 1
        if self.play_count == self.detune_count:
            self.play_count = 0
            self.is_tuned = False
        return res


class Drums(Instrument):
    """ Drums extends Instrument

    Instrument kind is 'Drums'

    Never de-tunes.
    """

    kind = 'Drums'

    def __init__(self, brand, year):
        super().__init__(brand, year)

    def play(self, song):
        """plays song like Instrument.

        song: string
        returns: string representing song played
        """
        res = super().play(song)
        return res


if __name__ == '__main__':
    # Create instances of Instruments
    my_instruments = [
        Bass("Ibanez", '2001'),
        Guitar("Fender", '1998'),
        Drums("Pearl", '2010')
    ]

    # Instantiate the MusicRoom class
    my_music_room = MusicRoom(my_instruments)

    # Rehearsing
    for i in range(3):
        my_music_room.play('Metallica - Nothing Else Matters')

    # Tune instruments
    my_music_room.tune()

    print("Done tuning\n")

    # Concert
    my_music_room.play('Metallica - Nothing Else Matters')
