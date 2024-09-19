import org.junit.jupiter.api.BeforeEach
import org.junit.jupiter.api.Test
import unam.ciencias.mx.myp.Artist
import java.net.URL
import kotlin.test.assertEquals

class ArtistTest {

    private var artist: Artist = Artist(
        "",
        "Bruno Mars",
        "",
        "",
        URL("https://www.setlist.fm/setlists/bruno-mars-bd5153a.html")
    )

    @BeforeEach
    fun setUp() {
        artist = Artist("", "Bruno Mars", "", "", URL("https://www.setlist.fm/setlists/bruno-mars-bd5153a.html"))
    }

    @Test
    fun testArtist() {
        val s = artist.sayHi("Valeria")
        assertEquals(s, "Hi Valeria, this is Bruno Mars. ;)")
    }

}