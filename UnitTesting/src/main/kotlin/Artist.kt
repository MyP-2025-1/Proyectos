package unam.ciencias.mx.myp

import java.net.URL

class Artist(
    private val mbid: String,
    private val name: String,
    private val sortName: String,
    private val disambiguation: String,
    private val url: URL
) {

    fun sayHi(name: String): String {
        return "Hi $ , this is ${this.name}. ;)"
    }

}