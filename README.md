# movie-rest-api
Django REST framework, Django based api to fetch and provide details about movies.

<dl>
  <dt>List all movies -GET</dt>
  <dd>- http://127.0.0.1:8000/api/</dd><br>
  <dt>Movie Search by ID -GET</dt>
  <dd>- http://127.0.0.1:8000/api/movie/1</dd>
  <dd>- salah.pythonanywhere.com/api/movie/[MOVIE-ID]</dd><br>
  <br>
  <dt>Add movie by Title -POST </dt>
  <dd>- http://127.0.0.1:8000/api/movie/morbius</dd>
  <dd>- salah.pythonanywhere.com/api/movie/[MOVIE-TITLE] **(POST this request with name)</dd><br>
  <br>
  <dt>List All comments -GET </dt>
  <dd>- http://127.0.0.1:8000/api/comment/</dd>
  <dd>- salah.pythonanywhere.com/api/comment/ **(Returns all Movies with comments)</dd><br>
  <br>
  <dt>Add Comment by ID of Movie -POST </dt>
  <dd>- http://127.0.0.1:8000/api/comment/1</dd>
  <dd>- salah.pythonanywhere.com/api/comment/[MOVIE-ID] **(POST to this url with {"comment":"comment data"}) to add comment</dd><br>
  <br>
  <dt>Search comment by Title  -GET </dt>
  <dd>- http://127.0.0.1:8000/api/comment/movie/Titan</dd>
  <dd>- salah.pythonanywhere.com/api/comment/movie/[MOVIE TITLE] **(Return the Title and comment)</dd><br>
  <br>
</dl>