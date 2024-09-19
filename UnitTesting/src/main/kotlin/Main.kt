package unam.ciencias.mx.myp

fun main() {
    val artists = QueryMaker().queryArtistByName("Karol G")
    for (artist in artists) {
        println(artist.sayHi("Fernando"))
    }
}