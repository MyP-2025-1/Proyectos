package unam.ciencias.mx.myp

import com.squareup.okhttp.OkHttpClient
import com.squareup.okhttp.Request
import java.util.ArrayList
import org.json.JSONObject
import java.net.URL

private const val API_KEY: String = "_KCLafXF5_dwU5wIMw3ILIjEd7gdRWs0ZkPj"
private const val BASE_URL: String = "https://api.setlist.fm/rest/1.0/"

class QueryMaker {

    private val client = OkHttpClient()

    private fun buildRequest(path: String): Request{
        return Request.Builder()
            .url(BASE_URL+path)
            .addHeader("Accept","application/json")
            .addHeader("x-api-key", API_KEY)
            .build()
        //val response = client.newCall(request).execute()
        //println(response.body().string())<

    }

    fun queryArtistByName(name: String): List<Artist> {
        val request: Request = buildRequest("search/artists/?artistName=$name")
        val response = client.newCall(request).execute()
        val jsonResponse = JSONObject(response.body()?.string())
        val artists: ArrayList<Artist> = ArrayList()
        for (json in jsonResponse.getJSONArray("artist")) {
            json as JSONObject
            artists.add(
                Artist(mbid = json.get("mbid").toString(),
                    name = json.get("name").toString(),
                    sortName = json.get("sortName").toString(),
                    disambiguation = json.get("disambiguation").toString(),
                    url = URL(json.get("url").toString())
                ))
        }
        return artists
    }
}